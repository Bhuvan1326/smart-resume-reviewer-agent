from typing import List, Dict
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

class KeywordMatcher:
    def __init__(self):
        self.stop_words = set(stopwords.words("english"))

    def simple_tokenize(self, text: str) -> List[str]:
        """Tokenizes text using regex (no need for NLTK punkt)."""
        tokens = re.findall(r"\b[a-zA-Z0-9]+\b", text.lower())
        return [word for word in tokens if word not in self.stop_words]

    def extract_keywords(self, text: str) -> List[str]:
        return self.simple_tokenize(text)

    def calculate_match_score(self, jd_text: str, resume_text: str) -> Dict:
        """Calculates keyword-based similarity using TF-IDF + Cosine Similarity."""

        documents = [jd_text, resume_text]
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform(documents)

        # Cosine similarity
        cosine_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
        match_score = int(cosine_sim * 100)

        # Keyword analysis
        jd_keywords = self.extract_keywords(jd_text)
        resume_keywords = self.extract_keywords(resume_text)

        missing_keywords = list(set(jd_keywords) - set(resume_keywords))

        report = {
            "match_score": match_score,
            "missing_keywords": missing_keywords[:5],
            "executive_summary": (
                f"The resume has a **{match_score}%** keyword similarity match "
                f"to the job description."
            ),
            "improvements": [
                "Increase the density of key phrases found in the JD.",
                f"Ensure the following terms are visible: {', '.join(missing_keywords[:3])}."
            ],
        }

        return report
