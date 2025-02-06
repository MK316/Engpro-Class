import streamlit as st

# Create four tabs
tabs = st.tabs(["Basics 1", "Basics 2", "Basics 3", "Basics 4"])

# Content for each tab
with tabs[0]:
    st.header("Basics 1")
    st.write("Content for Basics 1 goes here.")

with tabs[1]:
    st.header("Basics 2")
    st.write("Content for Basics 2 goes here.")

with tabs[2]:
    st.header("Basics 3")
    st.write("Content for Basics 3 goes here.")

with tabs[3]:
    st.header("Basics 4")
    st.write("Content for Basics 4 goes here.")
