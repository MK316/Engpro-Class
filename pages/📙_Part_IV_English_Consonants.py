import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 App1", "💧 App2", "💧 App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 🐾 Table of contents")
    st.markdown("""
    1. **Lesson 14**: Introduction  
    2. **Lesson 15**: face / phrase ; pressure / pleasure ; church / pledger  
    3. **Lesson 16**: English plural form, possessive, third person singular -s(es) pronunciation  
    4. **Lesson 17**: pie / bye ; tie / dye ; chi / guy  
    5. **Lesson 18**: fine / vine ; thing / there
    6. **Lesson 19**: r / l distinction
    7. **Lesson 20**: Consonant clusters: strike, wasps, helped
    """)
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
