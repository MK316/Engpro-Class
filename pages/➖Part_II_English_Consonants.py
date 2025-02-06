import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Lesson 1", "💧 Lesson 2", "💧 Lesson 3", "💧 Lesson 4", "💧 Lesson 5", "💧 Lesson 6", "💧 Lesson 7", "💧 Lesson 8","💧 Lesson 9"])

# Content for each tab
with tabs[0]:
    st.markdown("### Pronouncing English vowels")
with tabs[1]:
    st.markdown("### Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### Vowel pair in ‘bed’ and ‘bad’")
with tabs[4]:
    st.markdown("### Vowel [ɑ] and spelling confusion")
with tabs[5]:
    st.markdown("### Vowels in ‘but’, ‘bought’, ‘boat’")
with tabs[6]:
    st.markdown("### Diphthong vowels in English")
with tabs[7]:
    st.markdown("### Unstressed vowel (schwa vowel) as in ‘ago’, ‘upon’, ‘company’")
with tabs[8]:
    st.markdown("### R-colored vowels as in ‘perfect’ and ‘percent’")


