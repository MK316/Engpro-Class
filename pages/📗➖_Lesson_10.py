import streamlit as st

# Create four tabs
tabs = st.tabs(["❄️ Lesson 10", "❄️ App 1", "❄️ App2", "❄️ App3", ])

# Content for each tab
with tabs[0]:
    st.markdown("#### 📚 Word stress in English ")
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
