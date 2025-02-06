import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 App1", "💧 App2", "💧 App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 🐾 Table of contents")
    st.markdown("""
    - **Lesson 14**: Introduction  
    - **Lesson 15**: face / phrase ; pressure / pleasure ; church / pledger  
    - **Lesson 16**: English plural form, possessive, third person singular -s(es) pronunciation  
    - **Lesson 17**: pie / bye ; tie / dye ; chi / guy  
    - **Lesson 18**: fine / vine ; thing / there
    - **Lesson 19**: r / l distinction
    - **Lesson 20**: Consonant clusters: strike, wasps, helped
    """)
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
