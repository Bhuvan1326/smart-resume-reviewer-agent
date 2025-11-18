import json
import sys 

from agents.resume_parser import ResumeParser
from agents.jd_analyzer import JDAnalyzer
from agents.skill_matcher import SkillMatcher
from agents.scoring_agent import ScoringAgent
from agents.summary_agent import SummaryAgent


def main():
    print("\n=== Smart Resume Reviewer ===\n")

    # -----------------------------
    # 1. Setup & User Input
    # -----------------------------
    print("Loading data...")
    print("\n--- Input Setup ---")

    # NEW: Get the resume filename from the user
    resume_filename = input("Enter the Resume Filename (e.g., my_resume.pdf): ")
    # Construct the full path, assuming all resumes are in the 'data' folder
    resume_path = f"data/{resume_filename}"

    print("\n--- Job Description Input ---")
    
    # Get the Job Title from the user
    job_title = input("Enter the target Job Title: ")
    
    # Get the Job Description Text from the user (handles multi-line paste)
    print("Paste the Job Description text below. Press Ctrl+Z then Enter to finish:")
    
    # Use sys.stdin.read() for robust multi-line paste handling
    try:
        jd_text = sys.stdin.read()
    except EOFError:
        jd_text = ""
    
    jd_text = jd_text.strip()
    
    # Create the JD data structure, which is needed later for the final report
    jd_data = {"title": job_title, "description": jd_text, "company": "User Input"}
    
    # Error check the inputs
    if not jd_text.strip():
        print("❌ ERROR: Job description cannot be empty. Exiting.")
        return

    # -----------------------------
    # 2. Initialize all agents
    # -----------------------------
    resume_parser = ResumeParser()
    jd_analyzer = JDAnalyzer()
    skill_matcher = SkillMatcher()
    score_agent = ScoringAgent()
    summary_agent = SummaryAgent()

    # -----------------------------
    # Step 1 → Parse Resume
    # -----------------------------
    print(f"\nParsing Resume from: {resume_path}...")
    # NOTE: The resume_path is now dynamic based on user input
    resume_data = resume_parser.parse_resume(resume_path)

    if "error" in resume_data:
        print("❌ Resume parsing failed:", resume_data["error"])
        # Important: The user may have entered a wrong filename here.
        return
    
    # Store the raw text for the Scoring and Summary agents later
    resume_raw_text = resume_data.get("raw_text", "")
    if not resume_raw_text:
         print("❌ Resume parsing failed: Could not extract raw text.")
         return

    # -----------------------------
    # Step 2 → Analyze Job Description (Uses jd_text from user input)
    # -----------------------------
    print("Analyzing Job Description...")
    jd_result = jd_analyzer.analyze(jd_text)
    jd_keywords = jd_result["keywords"]

    # -----------------------------
    # Step 3 → Match Skills
    # -----------------------------
    print("Matching Skills...")

    resume_skills = resume_data.get("skills", [])
    
    match_result = skill_matcher.match(jd_keywords, resume_skills)

    matched = match_result["matched_skills"]
    match_score = match_result["score"]
    
    # Calculate missing keywords for subsequent agents and limit the list size
    all_missing = list(set(jd_keywords) - set(matched))
    missing_keywords = all_missing[:15]

    # -----------------------------
    # Step 4 → Calculate Score
    # -----------------------------
    print("Calculating Score...")
    
    final_score, scoring_breakdown = score_agent.calculate_score(
        match_score, 
        missing_keywords, 
        resume_raw_text
    )
    
    # -----------------------------
    # Step 5 → Generate Summary
    # -----------------------------
    print("Generating Summary...")
    
    summary = summary_agent.generate_summary(
        job_title, 
        final_score,
        missing_keywords, 
        resume_raw_text
    )

    # -----------------------------
    # Final Output
    # -----------------------------
    print("\n=== REVIEW SUMMARY ===\n")
    print(summary)

    # Save final report
    report = {
        "job_title": job_title,
        "company": jd_data.get("company", "N/A"),
        "resume_details": resume_data,
        "job_keywords": jd_keywords,
        "matched_skills": matched,
        "missing_keywords": missing_keywords,
        "match_score": match_score,
        "final_score": final_score,
        "scoring_breakdown": scoring_breakdown,
        "summary": summary
    }

    with open("review_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\nReport saved to review_report.json")


if __name__ == "__main__":
    main()