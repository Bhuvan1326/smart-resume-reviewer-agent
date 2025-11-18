class ScoringAgent:
    """
    Generates a final candidate score based on:
    - Keyword match score (already computed)
    - Missing keywords
    - Resume quality (experience, skills, formatting)
    - Simple ATS compliance checks
    """
    def calculate_score(self, keyword_match_score_raw, missing_keywords, resume_text):
        """
        Calculates and returns final_score, scoring_breakdown
        """

        # 1. Experience score (0–30)
        experience_score = self.experience_points(resume_text)

        # 2. Skill score (0–30)
        skill_score = self.skill_points(resume_text)

        # 3. ATS formatting score (0–20)
        ats_score = self.ats_compliance(resume_text)

        # 4. JD keyword match score (your model gives 0–100 → convert to 0–20)
        # We use the renamed argument here
        jd_match_points = keyword_match_score_raw * 0.20  # 20% weight

        # 5. Penalty for missing skills (-10 max)
        penalty = min(len(missing_keywords) * 2, 10)

        # FINAL SCORE  
        final_score = (
            experience_score +
            skill_score +
            ats_score +
            jd_match_points -
            penalty
        )

        final_score = max(0, min(100, int(final_score)))  # clamp 0–100

        breakdown = {
            "experience_score": experience_score,
            "skill_score": skill_score,
            "ats_score": ats_score,
            "jd_match_weighted": int(jd_match_points),
            "missing_skill_penalty": penalty,
            "final_score": final_score
        }

        return final_score, breakdown

    # -------------------------------------------------------------------
    # Sub-scoring functions (No changes needed here)
    # -------------------------------------------------------------------

    def experience_points(self, text):
        """
        Very simple heuristic:
        Count occurrences of "year" or "experience".
        """
        count = text.lower().count("year") + text.lower().count("experience")

        if count == 0:
            return 5    # low confidence
        elif count == 1:
            return 10
        elif count == 2:
            return 15
        elif count == 3:
            return 20
        else:
            return 30    # assume strong experience

    def skill_points(self, text):
        """
        Assign points based on common skill detection.
        """

        common_skills = [
            "python", "java", "sql", "excel",
            "flask", "django", "c++",
            "machine learning", "data analysis",
            "javascript", "react"
        ]

        score = 0
        text = text.lower()

        for skill in common_skills:
            if skill in text:
                score += 2  # each skill = +2 pts

        return min(score, 30)

    def ats_compliance(self, text):
        """
        Basic ATS checks:
        - Contains sections like education/experience
        - No too many special characters
        """

        text_lower = text.lower()

        points = 0

        if "education" in text_lower:
            points += 5

        if "experience" in text_lower:
            points += 5

        if "skills" in text_lower:
            points += 5

        # Penalize unstructured resumes
        special_chars = text.count("#") + text.count("*") + text.count("•")
        if special_chars < 20:
            points += 5  

        return min(points, 20)