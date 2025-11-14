# 🧠 AI Resume Screening Tool (NLP + Embeddings + Streamlit)

An intelligent Resume Screening Tool that compares a candidate's resume with a job description using NLP, semantic embeddings, and cosine similarity. Instead of keyword matching, this model understands the *meaning* of text using Sentence-BERT.

---

## 🚀 Features

- 📄 Upload resume (PDF)
- 📝 Paste job description
- 🔍 Extract key skills using spaCy NER
- 🔢 Generate SBERT embeddings
- 📊 Calculate similarity score using cosine similarity
- 🎯 HR-friendly clean UI (Streamlit)
- 🌐 Deployable on Streamlit / Render / HuggingFace / Vercel

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| NLP Model | Sentence-BERT (all-MiniLM-L6-v2) |
| Framework | Streamlit |
| Text Parsing | pdfplumber |
| NER | spaCy |
| Similarity | Cosine Similarity |
| Deployment | Streamlit Cloud / Vercel / Render / HF |

---

## 📁 Project Structure

resume-screening/
│
├── app.py # Streamlit UI
├── model.py # Embeddings, similarity, skill extraction
├── utils.py # PDF reading & cleaning helpers
├── requirements.txt
└── README.md


---

## 🔧 Installation

### Step 1 — Clone repo
```bash
git clone https://github.com//resume-screening.git
cd resume-screening

python -m venv .venv
.\.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py

