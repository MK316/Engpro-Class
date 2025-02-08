import streamlit as st

# Create four tabs
tabs = st.tabs(["📗 Lesson 11", "❄️ App1", "❄️ App2", "❄️ App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 11: ")
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
