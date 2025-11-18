# 📄 Smart Resume Reviewer — Multi-Agent AI System

A multi-agent AI-powered tool that analyzes resumes the way a recruiter does — but **faster, more accurately, and without bias**.

It extracts resume content, compares it with the job description, performs skill matching, computes a score, and generates a recruiter-style summary.

---

## 🚀 1. Problem Statement

Recruiters often face challenges such as:

- ⏳ Time-consuming manual screening  
- ❌ Human bias  
- 🧩 Skill mismatch between resume & job description  
- 🔍 Inconsistent evaluation  
- 📄 ATS systems failing due to formatting issues  

**Smart Resume Reviewer Agent** solves these problems by providing:

✔ AI-based resume understanding  
✔ Contextual skill matching  
✔ Candidate scoring  
✔ Recruiter-style summary generation  

---

## 🤖 2. Why Agents?

A single AI model cannot perform the entire HR evaluation workflow.  
This system uses **multiple specialized agents**, similar to an HR team:

1. Resume Parsing Agent  
2. Job Description Analyzer Agent  
3. Skill Matching & Gap Analysis Agent  
4. Scoring Agent  
5. Summary Agent  

Agents communicate with each other and complete the workflow intelligently.

---

## 🏗️ 3. System Architecture

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

## 🤖 4. Agent Responsibilities

### **Resume Parser Agent**
- Extracts text from PDF/DOCX  
- Identifies experience, skills, education, projects  

### **Job Description Analyzer**
- Extracts required skills  
- Maps job responsibilities  

### **Skill Matcher**
- Compares resume vs job description  
- Finds missing or weak skills  
- Produces similarity score  

### **Scoring Agent**
Scores based on:
- Skill match  
- Experience relevance  
- Education  
- Projects  
- Formatting (ATS compatibility)  

### **Summary Agent**
Generates:
- Strengths  
- Weaknesses  
- Gaps  
- Final recommendation  

---

## 🧪 5. How It Works

### Step-by-step Process

1️⃣ User provides:  
- Resume (PDF or text)  
- Job description (text or JSON)

2️⃣ Agents start working:  
- Resume Parser → extracts sections  
- JD Analyzer → finds required skills  
- Skill Matcher → compares and scores  
- Scoring Agent → generates final score  
- Summary Agent → produces recruiter-style summary  

### Example Output

```
Match Score: 76%
Strengths: Python, SQL, Flask
Gaps: Cloud, NLP
Final Recommendation: Good candidate for interview
```

---

## 🛠️ 6. Tech Stack

- Python  
- PyPDF2 / pdfplumber  
- python-docx  
- NLTK  
- scikit-learn  
- JSON  

---

## 📥 7. Installation & Setup

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

---

## 📌 8. Future Improvements

- Bulk resume ranking  
- Bias detection & fairness layer  
- Industry-specific analysis agents  
- ATS platform integration  
- Resume rewriting agent  
- Job Description Generator Agent  
- Full Web UI Dashboard  

---

## 👨‍💻 9. Author

**Bhuvan Patil**  
AI & Software Development Enthusiast  

---

