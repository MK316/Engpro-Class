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

    This course is specifically designed for future English teachers, aiming to enhance their English language proficiency with an emphasis on developing clear and intelligible pronunciation. It includes a series of targeted activities that improve speaking and listening skills, complemented by a variety of authentic materials such as TED Talks and online videos, enhanced by digital resources and advanced AI technologies.
    
    The curriculum provides an in-depth study of English linguistic features, focusing on pronunciation. Instruction covers the International Phonetic Alphabet (IPA) and the importance of stress and intonation in communication. Practical applications complement this theoretical knowledge, fostering a holistic approach to mastering English pronunciation.

    Assignments are crafted to reinforce learned concepts and encourage the development of teaching methodologies. By the course's end, participants will not only master English pronunciation but also be equipped with effective strategies to teach these skills in various educational settings.
    </div>
    """, unsafe_allow_html=True)

# Code for other tabs...
