import streamlit as st
from model import get_similarity, extract_skills
from utils import extract_text_from_pdf

st.title("Resume Screening Tool (Embeddings + NLP)")

uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_text = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if uploaded_resume and jd_text:
        resume_text = extract_text_from_pdf(uploaded_resume)

        score = get_similarity(resume_text, jd_text)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)
        matched = list(set(resume_skills) & set(jd_skills))
        missing = list(set(jd_skills) - set(resume_skills))

        st.subheader(f"Match Score: {score}%")
        st.write("Matched Skills:", matched)
        st.write("Missing Skills:", missing)
