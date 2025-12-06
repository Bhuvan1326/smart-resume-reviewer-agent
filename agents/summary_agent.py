class SummaryAgent:
    """
    Generates a clean recruiter-style summary based on:
    - Skill match score
    - Missing skills
    - Job title
    - Extracted resume insights
    """

    def generate_summary(self, job_title, final_score, missing_keywords, resume_text):
        """
        Creates a human-readable summary for the recruiter.
        """

        experience_years = self.estimate_experience(resume_text) 
        top_skills = self.extract_top_skills(resume_text)

      
        if missing_keywords:
           
            missing_skills_formatted = "\n* " + "\n* ".join(missing_keywords)
        else:
            missing_skills_formatted = "None — strong alignment"
        
        summary = f"""
📌 Recruiter Summary — Smart Resume Reviewer Agent

Job Title: {job_title}
Match Score: {final_score}%

The candidate shows approximately {experience_years} years of experience
based on the resume content and demonstrates familiarity with the following 
observable skills: {", ".join(top_skills) if top_skills else "Not clearly visible"}.

Missing / Weak Skills:  
{missing_skills_formatted} 

Recommendation:  
This candidate may be considered for further evaluation if the missing skills 
are not critical. Overall alignment can improve with clearer skill representation 
and additional project details.
"""

        return summary

    # ---------------------------------------------------------------------
    # Simple logic functions (works offline)
    # ---------------------------------------------------------------------

    def estimate_experience(self, text) -> str:
        """
        Basic heuristic:
        Count occurrences of 'year', 'years', 'yr', etc.
        """

        keywords = ["year", "years", "yr", "experience"]
        count = 0

        for w in keywords:
            count += text.lower().count(w)

        # crude conversion (returns a string)
        if count == 0:
            return "0-1"
        elif count == 1:
            return "1-2"
        elif count == 2:
            return "2-3"
        else:
            return "3+"  # 3 or more occurrences -> assume 3+ years

    def extract_top_skills(self, text):
        """
        Very simple keyword extraction.
        """

        common_skills = [
            "python", "java", "sql", "excel", "c++",
            "flask", "django", "javascript", "react",
            "machine learning", "data analysis", "html", "css"
        ]

        found = []

        text_lower = text.lower()
        for skill in common_skills:
            if skill in text_lower:
                found.append(skill)

        return found[:5]