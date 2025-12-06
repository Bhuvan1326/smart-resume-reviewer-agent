import streamlit as st
from agents.resume_parser import ResumeParser
from agents.jd_analyzer import get_keywords_for_job
from agents.skill_matcher import SkillMatcher
from agents.scoring_agent import ScoringAgent
from agents.summary_agent import SummaryAgent

st.set_page_config(page_title="Smart Resume Reviewer", page_icon="🔍")

st.title("Smart Resume Reviewer 🔍")
st.write("Upload your resume and enter a Job Title to check how well it matches.")

job_title = st.text_input("Enter Job Title (e.g., Full Stack Developer, Data Analyst, Python Developer)")

uploaded_file = st.file_uploader("Upload Resume (PDF only)", type=["pdf"])

if uploaded_file and job_title:
    
  
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    
    parser = ResumeParser()
    
  
    resume_data = parser.parse_resume("temp_resume.pdf")

    if not resume_data or resume_data.get("error"):
        st.error("Could not parse your resume. Please try another file.")
        st.stop()

 
    resume_text = resume_data.get("raw_text", "")
    resume_skills = [skill.lower() for skill in resume_data.get("skills", [])]


    job_keywords = get_keywords_for_job(job_title)

    if not job_keywords:
        st.warning("No predefined keywords found for this job title. Try another job title.")
        st.stop()

    st.subheader(f"Keywords for {job_title.title()}")
    st.write(", ".join(job_keywords))

    # -----------------------------------------------
    # Matching Logic
    # -----------------------------------------------
    matched_keywords = [kw for kw in job_keywords if kw.lower() in resume_text.lower()]
    missing_keywords = [kw for kw in job_keywords if kw.lower() not in resume_text.lower()]

    match_score = int((len(matched_keywords) / len(job_keywords)) * 100)

    # -----------------------------------------------
    # Output Section
    # -----------------------------------------------
    st.subheader("Resume Match Score")
    st.progress(match_score)
    st.write(f"**Match Score: {match_score}%**")

    st.subheader("Matched Keywords")
    if matched_keywords:
        st.success(", ".join(matched_keywords))
    else:
        st.write("No job-related keywords found.")

    st.subheader("Missing Keywords")
    if missing_keywords:
        st.error(", ".join(missing_keywords))
    else:
        st.success("Your resume covers all the required keywords!")

    st.subheader("Feedback")
    if match_score < 50:
        st.write("🔸 Your resume needs improvement. Add more job-related keywords.")
    elif 50 <= match_score < 80:
        st.write("🟡 Good resume, but you can still improve by adding missing keywords.")
    else:
        st.write("🟢 Your resume looks strong for this job role!")

else:
    st.info("Please enter a job title and upload a resume.")