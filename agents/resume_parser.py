import re
from utils.pdf_processor import extract_text_from_pdf


class ResumeParser:
    """
    Extracts useful information from a resume PDF:
    - name
    - email
    - phone
    - skills (keyword based)
    """

    def __init__(self):
        # Common skills list
        self.skill_keywords = [
            "python", "java", "c++", "html", "css", "javascript",
            "sql", "excel", "power bi", "machine learning",
            "data analysis", "communication", "leadership",
            "teamwork", "aws", "cloud", "django", "flask"
        ]

    def extract_skills(self, text):
        text = text.lower()
        found_skills = []

        for skill in self.skill_keywords:
            if skill in text:
                found_skills.append(skill)

        return list(set(found_skills))

    def extract_email(self, text):
        match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        return match.group(0) if match else None

    def extract_phone(self, text):
        match = re.search(r"\b[6-9]\d{9}\b", text)  # Indian phone pattern
        return match.group(0) if match else None

    def extract_name(self, text):
        # Naive name extractor: first line + capital words
        first_line = text.split("\n")[0]
        possible_name = " ".join([w for w in first_line.split() if w.istitle()])

        return possible_name if len(possible_name.split()) >= 2 else "Unknown"

    def parse_resume(self, pdf_path):
        text = extract_text_from_pdf(pdf_path)

        if not text:
            return {"error": "Could not extract text"}

        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "skills": self.extract_skills(text),
            "raw_text": text,
        }


# Test module
if __name__ == "__main__":
    parser = ResumeParser()
    result = parser.parse_resume("data/sample_resume.pdf")

    print("\nParsed Resume Data:\n")
    for key, value in result.items():
        print(f"{key}: {value}")
