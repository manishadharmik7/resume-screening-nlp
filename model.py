from sentence_transformers import SentenceTransformer, util

import subprocess
import sys

# Load Sentence-Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

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