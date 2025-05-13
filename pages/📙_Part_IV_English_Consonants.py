import streamlit as st
import streamlit.components.v1 as components


# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 IPA online", "💧 App2", "💧 App3"])

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
    st.markdown("### 🌐 Embedded Web Page")
    url = "https://ipa.typeit.org/full/"  # Replace with the actual URL you want to embed
    components.iframe(url, width=800, height=600)
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
