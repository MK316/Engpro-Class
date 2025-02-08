import streamlit as st

# Create four tabs
tabs = st.tabs(["📗 Lesson 11", "❄️ App1", "❄️ App2", "❄️ App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 11: Accents in English")
    st.write("In addition to word stress, which is assigned to individual syllables, English words can also receive accents within a sentence. This combination of stress and accent leads to greater emphasis. For instance, stressed syllables are naturally more emphasized than unstressed ones. Moreover, stressed syllables in accented words are even stronger and longer than those in unaccented words.")
    st.write("Example) My **younger** brother ate **ten** chocolate **cookies.**")


    st.markdown("##### 1. New information is usually accented with a high pitch")

    st.write("My name is Jane Smith. (H* vs. L* carry different meanings)")
    st.markdown("##### 2. The final key word within a sentence receives the most emphasis in English.")
    

with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
