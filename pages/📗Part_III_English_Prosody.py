import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 App1", "💧 App2", "💧 App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 🐾 Table of contents ")
    st.markdown("""
    1. **Lesson 10**: Stress in words  
    2. **Lesson 11**: Accents in English  
    3. **Lesson 12**: Rhythm and intonation in English  
    4. **Lesson 13**: Thought grouping  
    """)
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
