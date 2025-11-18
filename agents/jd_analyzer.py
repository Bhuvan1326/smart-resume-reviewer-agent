import re 
from typing import List, Dict

class JDAnalyzer:
    """
    Analyzes the Job Description (JD) text and extracts key terms
    """
    
    stopwords = {"the", "and", "of", "to", "a", "in", "for", "with", "on", "is"}

    def analyze(self, jd_text: str) -> Dict:
        
        text_lower = jd_text.lower()
        
        tokens = re.findall(r'[a-z0-9]+', text_lower)

        keywords = set()
        for token in tokens:
            if token not in self.stopwords and len(token) > 1:
                keywords.add(token)
            
        return {
            "keywords": list(keywords)
        }