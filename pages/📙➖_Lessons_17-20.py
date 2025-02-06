import streamlit as st

# Create four tabs
tabs = st.tabs(["💧 Lesson 17", "💧 Lesson 18", "💧 Lesson 19", "💧 Lesson 20"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 17: ")
with tabs[1]:
    st.markdown("### 📒 Lesson 18: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 19: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 20: ")
