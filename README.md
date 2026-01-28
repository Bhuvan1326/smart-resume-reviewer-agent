# 📄 Smart Resume Reviewer — Multi-Agent AI System

A multi-agent AI-powered tool that analyzes resumes the way a recruiter does — but **faster, more accurately, and without bias**.

It extracts resume content, compares it with the job description, performs skill matching, computes a score, and generates a recruiter-style summary.

---

## 1. Problem Statement

Recruiters often face challenges such as:

- Time-consuming manual screening 
- Human bias 
- Skill mismatch between resume & job description 
- Inconsistent evaluation 
- ATS systems failing due to formatting issues 

**Smart Resume Reviewer Agent** solves these problems by providing:

✔ AI-based resume understanding 
✔ Contextual skill matching 
✔ Candidate scoring 
✔ Recruiter-style summary generation 

---

## 2. Why Agents?

A single AI model cannot perform the entire HR evaluation workflow. 
This system uses **multiple specialized agents**, similar to an HR team:

1. Resume Parsing Agent 
2. Job Description Analyzer Agent 
3. Skill Matching & Gap Analysis Agent 
4. Scoring Agent 
5. Summary Agent 

Agents communicate with each other and complete the workflow intelligently.

---

##  3. System Architecture

```
smart-resume-reviewer/
│
├── main.py                  # Main orchestrator agent
├── agents/                  # All sub-agents
│   ├── resume_parser.py
│   ├── jd_analyzer.py
│   ├── skill_matcher.py
│   ├── scoring_agent.py
│   └── summary_agent.py
│
├── utils/
│   └── pdf_processor.py     # PDF/DOCX loader
│
├── data/
│   ├── sample_resume.pdf
│   └── sample_job_desc.json
│
├── requirements.txt
└── README.md
```

---

## 4. Key Features

* **Dynamic Role Matching:** The system prompts the user for the **Job Title** and **Job Description** at runtime, allowing it to evaluate candidates for any role, from 'Senior Python Developer' to 'Full Stack Developer'.
* **Weighted Scoring:** The final match score integrates keyword matching, experience points, and ATS compliance factors for a holistic evaluation.
* **Robust Input Handling:** The script uses `sys.stdin.read()` to reliably accept large, multi-line job descriptions pasted directly into the terminal.
* **Privacy Focus:** A `.gitignore` ensures that sensitive resume data (`data/*.pdf`) and transient output (`review_report.json`) are never committed to the repository.

---

## 5. How It Works

### Step-by-step Process

1️.User runs `main.py` and provides:
- Resume filename (e.g., `candidate_a.pdf`)
- Job description text

2️. Agents start working:
- **JD Analyzer** extracts required skills (e.g., Python, React, AWS).
- **Resume Parser** extracts all text and skills from the PDF.
- **Skill Matcher** compares the two lists and calculates the similarity score.
- **Scoring Agent** computes the final score based on all factors.
- **Summary Agent** generates a final, actionable summary for the recruiter.  

### Example Output

```
Match Score: 76%
Strengths: Python, SQL, Flask
Gaps: Cloud, NLP
Final Recommendation: Good candidate for interview
```

---

## 6. Tech Stack

- Python  
- PyPDF2 / pdfplumber  
- python-docx  
- NLTK  
- scikit-learn  
- JSON  

---

## 7. Installation & Setup

### Create Virtual Environment
```
python -m venv venv
```

### Activate (Windows)
```
venv\Scripts\activate
```

### Install Dependencies
```
pip install -r requirements.txt
```

### Run the Program
```
python main.py
```

![1765035731543](https://github.com/user-attachments/assets/edc96af3-80fb-46ea-b768-c46324d3538c)


![1765035731349](https://github.com/user-attachments/assets/9fc72718-bbd2-4b86-860a-5d1758284430)


---

## 8. Future Improvements

- Bulk resume ranking  
- Bias detection & fairness layer  
- Industry-specific analysis agents  
- ATS platform integration  
- Resume rewriting agent  
- Job Description Generator Agent  
- Full Web UI Dashboard  

---

## 9. Author

**Bhuvan Patil**  
AI & Software Development Enthusiast  

---

=======
# smart-resume-reviewer-agent
The Smart Resume Reviewer is a multi-agent system that scores resumes against any job description, providing a match percentage, skill gap analysis, and a recruiter summary. It uses specialized agents for parsing, keyword analysis, skill matching, and final score calculation.
