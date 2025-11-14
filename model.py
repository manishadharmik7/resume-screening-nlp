from sentence_transformers import SentenceTransformer, util
import spacy
import subprocess
import sys

# Load Sentence-Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load spaCy model (auto-download if missing)
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

skill_keywords = [
    "python", "sql", "machine learning", "deep learning",
    "tensorflow", "keras", "pytorch", "docker", "git",
    "pandas", "numpy", "nlp", "aws", "spark"
]

def get_embedding(text):
    return model.encode(text, convert_to_tensor=True)

def get_similarity(resume_text, jd_text):
    emb1 = get_embedding(resume_text)
    emb2 = get_embedding(jd_text)
    score = util.cos_sim(emb1, emb2).item()
    return round(score * 100, 2)

def extract_skills(text):
    text = text.lower()
    found = [skill for skill in skill_keywords if skill in text]
    return list(set(found))
