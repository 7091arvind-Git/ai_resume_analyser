import streamlit as st
import pdfplumber
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200
)


def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text

    return text.lower()


if uploaded_file:

    # Extract resume text
    resume_text = extract_text(uploaded_file)

    # Load skills
    skills_df = pd.read_csv("skills.csv")
    skill_list = skills_df["skill"].tolist()

    found_skills = []

    for skill in skill_list:
        if skill.lower() in resume_text:
            found_skills.append(skill)

    # Resume Score
    score = int(
        (len(found_skills) / len(skill_list)) * 100
    )

    st.subheader("Resume Score")
    st.progress(score)
    st.write(f"Score: {score}%")

    # Detected Skills
    st.subheader("Detected Skills")

    if found_skills:
        for skill in found_skills:
            st.success(skill)

    # Missing Skills
    missing_skills = list(
        set(skill_list) - set(found_skills)
    )

    st.subheader("Missing Skills")

    for skill in missing_skills:
        st.warning(skill)

    # Job Description Match Score
    if job_description:

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform(
            [resume_text, job_description.lower()]
        )

        similarity = cosine_similarity(
            vectors[0:1],
            vectors[1:2]
        )[0][0]

        match_score = int(similarity * 100)

        st.subheader("Job Match Score")
        st.progress(match_score)
        st.write(f"Match Score: {match_score}%")

        st.subheader("Suggestions")

        if match_score < 50:
            st.error(
                "Your resume needs improvement for this role."
            )

        elif match_score < 75:
            st.warning(
                "Good match, but add more relevant skills."
            )

        else:
            st.success(
                "Excellent match for this role!"
            )