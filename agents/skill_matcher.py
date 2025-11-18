class SkillMatcher:
    def match(self, jd_keywords: list, resume_skills: list) -> dict: 

        matched = [
            kw for kw in jd_keywords 
            if kw.lower() in [s.lower() for s in resume_skills] # Check if JD keyword is in extracted skills
        ]
        
        # Calculate score and return report (rest of your logic can be simplified)
        score = 0
        if jd_keywords:
            score = int((len(matched) / len(jd_keywords)) * 100)

        return {
            "matched_skills": matched,
            "score": score
        }