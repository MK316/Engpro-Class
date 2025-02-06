import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Lesson 1", "💧 Lesson 2", "💧 Lesson 3", "💧 Lesson 4"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 1: Pronouncing English vowels")
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")

