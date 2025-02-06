import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 App1", "💧 App2", "💧 App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 🐾 Table of contents ")
    st.markdown("""
    - **Lesson 1**: Pronouncing English vowels  
    - **Lesson 2**: Stress and rhythm in English  
    - **Lesson 3**: Consonant articulation  
    - **Lesson 4**: Connected speech patterns  
    - **Lesson 5**: Vowel [ɑ] and spelling confusion
    - **Lesson 6**: Vowels in ‘but’, ‘bought’, ‘boat’
    - **Lesson 7**: Diphthong vowels in English
    - **Lesson 8**: Unstressed vowel (schwa vowel) as in ‘ago’, ‘upon’, ‘company’
    - **Lesson 9**: R-colored vowels as in ‘perfect’ and ‘percent’

    """)
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
