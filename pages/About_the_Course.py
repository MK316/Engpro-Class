import streamlit as st
import requests

# Include custom CSS to justify text in the markdown
st.markdown("""
<style>
.justify-text p {
    text-align: justify;
    text-justify: inter-word;
}
</style>
""", unsafe_allow_html=True)

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Course Overview", "🍓 Schedule", "🍏 Evaluation", "🍒 Assignments", "🍋 Links"])

# Content for the Course Overview tab
with tabs[0]:
    st.header("Course Overview")
    
    st.markdown("""
    <div class="justify-text">


    This course is designed to enhance participants' proficiency in the English language, with a specific emphasis on developing clear and intelligible pronunciation. It features a comprehensive series of activities focused on improving both speaking and listening skills. These structured exercises are aimed at fostering a deeper understanding of phonetic nuances and improving communicative clarity.

    Participants will engage with a wide range of authentic materials, including TED Talks and online videos, which serve as foundational tools for practicing language comprehension and spoken English. The integration of digital resources and advanced AI technologies enhances the learning experience, allowing for innovative approaches to language acquisition and application.

    The curriculum includes an in-depth study of key linguistic features of English, with a special focus on pronunciation. Instruction covers the International Phonetic Alphabet (IPA) and delves into the significance of stress and intonation in effective communication. This theoretical knowledge is complemented by practical applications, ensuring a holistic approach to mastering English pronunciation.

    Assignments are strategically designed to reinforce the concepts taught, providing participants with opportunities to apply their knowledge in practical settings. By the end of the course, participants will have acquired a thorough understanding of English pronunciation, equipping them with the essential skills to teach English proficiently and confidently in various educational environments.
    </div>
    """, unsafe_allow_html=True)

# Code for other tabs...
