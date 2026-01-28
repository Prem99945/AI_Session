🧠 Smart Resume Skill Analyzer

A simple and interactive Streamlit web app that analyzes resume text, identifies known technical skills, and suggests relevant skills to learn next. Perfect for beginners learning Python + Streamlit and for showcasing a mini AI-style project.

🚀 Features

📄 Paste resume text directly into the app

🔍 Automatically detects core technical skills

⭐ Suggests complementary skills based on detected skills

🎯 Provides basic career guidance

⚡ Fast, lightweight, and beginner-friendly UI

🛠️ Technologies Used

Python 3

Streamlit

Basic text processing & logic

📂 Project Structure
streamlit/
│
├── streamlit_proj1.py   # Main Streamlit application
└── README.md            # Project documentation

▶️ How to Run the App
1️⃣ Activate your virtual environment
.\pyautoguiEnv1\Scripts\activate

2️⃣ Install Streamlit (if not installed)
pip install streamlit

3️⃣ Run the application
streamlit run streamlit_proj1.py


The app will automatically open in your browser 🌐
(Default: http://localhost:8501)

🧪 How It Works

User pastes resume text into the text area

App scans the text for predefined core skills

Matching skills are displayed under Skills Found

Related skills are suggested under Suggested Skills

A basic career tip is shown based on detected skills

📚 Skill Database Used
Python  → Flask, Django, Data Science, Automation
Java    → Spring Boot, Microservices, System Design
Selenium → Playwright, Test Automation
HTML    → CSS, JavaScript, React
SQL     → Advanced SQL, Data Analytics

💡 Example Input
I have experience in Python, Selenium, and SQL.
I have worked on automation and backend projects.

🎯 Future Enhancements (Ideas)

Upload resume PDF/DOCX

Use NLP for smarter skill extraction

Add job role recommendations

Skill match percentage

Export analysis as PDF

📌 Learning Outcome

This project helps you practice:

Streamlit UI components

Conditional logic

Python dictionaries & sets

Real-world mini-app structure
