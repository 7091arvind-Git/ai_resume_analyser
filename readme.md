🚀 AI Resume Analyzer

An AI-powered Resume Analyzer built using Python, Streamlit, and NLP techniques. The application analyzes resumes, detects skills, compares them with job descriptions, and provides a match score along with improvement suggestions.

🌐 Live Demo

Try the deployed application:

👉 https://7091arvind-git-ai-resume-analyser-app-ervxkv.streamlit.app/

✨ Features

📄 Upload Resume (PDF)

🔍 Extract Resume Text Automatically

✅ Detect Technical Skills

📊 Resume Score Analysis

🎯 Recommended Skills to Learn

💼 Job Description Matching

🤖 TF-IDF Based Similarity Scoring

📈 Resume Improvement Suggestions

🌐 Deployed on Streamlit Cloud

🛠️ Tech Stack

Python

Streamlit

Pandas

PDFPlumber

Scikit-Learn

TF-IDF Vectorization

Cosine Similarity

📂 Project Structure

ai_resume_analyser/
│
├── app.py
├── skills.csv
├── requirements.txt
└── README.md

⚙️ Installation

Clone the repository:

git clone https://github.com/7091arvind-Git/ai_resume_analyser.git

Move into the project directory:

cd ai_resume_analyser

Install dependencies:

pip install -r requirements.txt

Run the application:

streamlit run app.py

🚀 How It Works

Upload a PDF Resume.

Resume text is extracted automatically using PDFPlumber.

Technical skills are detected using a predefined skills database.

A resume score is calculated based on the detected skills and resume content.

Paste a Job Description.

TF-IDF Vectorization converts the resume and job description text into numerical vectors.

Cosine Similarity calculates the Job Match Score.

The application provides recommended skills and improvement suggestions.

🧠 NLP Used

This project uses traditional NLP techniques for resume and job-description analysis.

Text Extraction: PDFPlumber extracts text from PDF resumes.

TF-IDF: Converts text into numerical feature vectors.

Cosine Similarity: Measures similarity between resume content and the job description.

Skill Extraction: Matches resume content against a predefined technical skills database.

📸 Screenshot

Add a screenshot of the deployed application here.

🔮 Future Enhancements

AI-powered Resume Feedback

Resume Ranking System

Multiple Resume Comparison

Advanced NLP Skill Extraction

Course Recommendations

Resume Keyword Optimization

👨‍💻 Author

Arvind Yadav

CSE (AI & ML) Student

GitHub: https://github.com/7091arvind-Git

⭐ If you found this project useful, consider giving it a star.
