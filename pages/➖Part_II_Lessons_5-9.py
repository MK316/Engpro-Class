import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Lesson 5", "💧 Lesson 6", "💧 Lesson 7", "💧 Lesson 8","💧 Lesson 9"])

# Content for each tab
with tabs[0]:
    st.markdown("### Lesson 5: Vowel [ɑ] and spelling confusion")
with tabs[1]:
    st.markdown("### Lesson 6: Vowels in ‘but’, ‘bought’, ‘boat’")
with tabs[2]:
    st.markdown("### Lesson 7: Diphthong vowels in English")
with tabs[3]:
    st.markdown("### Lesson 8: Unstressed vowel (schwa vowel) as in ‘ago’, ‘upon’, ‘company’")
with tabs[4]:
    st.markdown("### Lesson 9: R-colored vowels as in ‘perfect’ and ‘percent’")

