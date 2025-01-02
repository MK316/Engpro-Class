import streamlit as st
import requests

# Create tabs for different sections of the course
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Course Overview", "Schedule", "Evaluation", "Assignments", "Links"])

# Content for the Course Overview tab
with tabs[0]:
    st.header("Course Overview")
    
    st.markdown("""
    **Course Overview**

    This course is designed to enhance participants' proficiency in the English language, with a specific emphasis on developing clear and intelligible pronunciation. It features a comprehensive series of activities focused on improving both speaking and listening skills. These structured exercises are aimed at fostering a deeper understanding of phonetic nuances and improving communicative clarity.

    Participants will engage with a wide range of authentic materials, including TED Talks and online videos, which serve as foundational tools for practicing language comprehension and spoken English. The integration of digital resources and advanced AI technologies enhances the learning experience, allowing for innovative approaches to language acquisition and application.

    The curriculum includes an in-depth study of key linguistic features of English, with a special focus on pronunciation. Instruction covers the International Phonetic Alphabet (IPA) and delves into the significance of stress and intonation in effective communication. This theoretical knowledge is complemented by practical applications, ensuring a holistic approach to mastering English pronunciation.

    Assignments are strategically designed to reinforce the concepts taught, providing participants with opportunities to apply their knowledge in practical settings. By the end of the course, participants will have acquired a thorough understanding of English pronunciation, equipping them with the essential skills to teach English proficiently and confidently in various educational environments.
    """)

# Content for the Schedule tab
with tab2:
    st.caption("Spring 2025")
    # URL of the raw markdown file on GitHub
    markdown_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/README.md"
    
    try:
        response = requests.get(markdown_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")

# Content for the Evaluation tab
with tab3:
    st.header("Evaluation")
    st.write("Describe the evaluation criteria and grading methods. Include information on exams, projects, participation, etc.")

# Content for the Assignments tab
with tab4:
    st.header("Assignments")
    st.write("List the assignments for the course here. Provide due dates, requirements, submission guidelines, etc.")

# Content for the Downloads tab
with tab5:
    st.header("Links")
    st.write("Provide online resources here. This could include syllabi, lecture slides, reading materials, additional resources, etc.")
