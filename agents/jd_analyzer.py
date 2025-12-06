import re

class JDAnalyzer:
    """
    This class is no longer used for JD text.
    Keywords are now provided based on Job Title.
    """

    def analyze(self, jd_text: str):
        return {"keywords": []}


def get_keywords_for_job(job_title: str):
    job_title = job_title.lower().strip()

    predefined_keywords = {
        "full stack developer": [
            "javascript", "react", "nodejs", "express", "html", "css",
            "api", "mongodb", "sql", "python", "django", "git", "rest"
        ],

        "frontend developer": [
            "javascript", "react", "html", "css", "redux", "typescript",
            "ui", "ux", "tailwind", "bootstrap"
        ],

        "backend developer": [
            "python", "java", "nodejs", "api", "sql", "mongodb",
            "django", "flask", "spring", "microservices"
        ],

        "python developer": [
            "python", "django", "flask", "api", "scripting",
            "automation", "sql", "git", "oop"
        ],

        "data analyst": [
            "python", "excel", "sql", "pandas", "numpy",
            "power bi", "tableau", "data cleaning",
            "visualization", "statistics"
        ],

        "machine learning engineer": [
            "python", "tensorflow", "pytorch", "sklearn",
            "pandas", "numpy", "ml", "deep learning", "nlp"
        ]
    }

    return predefined_keywords.get(job_title, [])
