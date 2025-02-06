import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 App1", "💧 App2", "💧 App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 🐾 Table of contents")
    st.markdown("""
    1. **Lesson 14**: Pronouncing English vowels  
    2. **Lesson 15**: Stress and rhythm in English  
    3. **Lesson 16**: Consonant articulation  
    4. **Lesson 17**: Connected speech patterns  
    5. **Lesson 18**: Vowel [ɑ] and spelling confusion
    6. **Lesson 19**: Vowels in ‘but’, ‘bought’, ‘boat’
    7. **Lesson 20**: Diphthong vowels in English
    """)
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
