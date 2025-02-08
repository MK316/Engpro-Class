import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 App   1", "💧 App2", "💧 App3", "💧 App4"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒App1 ")
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
