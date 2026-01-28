import streamlit as st

st.set_page_config(page_title="Resume Skill Analyzer", page_icon="🧠")

st.title("🧠 Smart Resume Skill Analyzer")
st.write("Paste your resume text below and get instant insights 🚀")

# Skill database
SKILL_DB = {
    "python": ["Flask", "Django", "Data Science", "Automation"],
    "java": ["Spring Boot", "Microservices", "System Design"],
    "selenium": ["Playwright", "Test Automation"],
    "html": ["CSS", "JavaScript", "React"],
    "sql": ["Advanced SQL", "Data Analytics"]
}

resume_text = st.text_area(
    "📄 Paste your resume here",
    height=200,
    placeholder="Example: I have experience in Python, Selenium and SQL..."
)

if st.button("🔍 Analyze Resume"):
    if not resume_text.strip():
        st.warning("Please paste resume text first!")
    else:
        resume_lower = resume_text.lower()
        found_skills = []
        suggested_skills = set()

        for skill in SKILL_DB:
            if skill in resume_lower:
                found_skills.append(skill)
                suggested_skills.update(SKILL_DB[skill])

        st.success("✅ Analysis Complete")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🟢 Skills Found")
            if found_skills:
                for s in found_skills:
                    st.write("✔️", s.capitalize())
            else:
                st.write("No matching skills found")

        with col2:
            st.subheader("🚀 Suggested Skills")
            if suggested_skills:
                for s in suggested_skills:
                    st.write("⭐", s)
            else:
                st.write("Add more core skills to get suggestions")

        st.subheader("🎯 Career Tip")
        if "python" in found_skills:
            st.info("You are on a great path for Backend / Automation roles!")
        elif "java" in found_skills:
            st.info("Strong foundation for enterprise backend development!")
        else:
            st.info("Consider learning Python or Java to boost opportunities!")
