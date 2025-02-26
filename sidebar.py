import streamlit as st

def show_sidebar():
    st.sidebar.title("📖 Class Navigation")

    # Top-level navigation
    st.sidebar.markdown("[Home](#)")
    st.sidebar.markdown("[About the Course](#)")
    st.sidebar.markdown("### Bookmarks & Apps")
    st.sidebar.markdown("[Class Management Apps](#)")
    st.sidebar.markdown("### Class Workbook Contents")

    # ✅ Getting to Know Each Other (Always Visible)
    st.sidebar.markdown("📒 **Getting to Know Each Other**")

    # ✅ Part I Introduction (Always Visible)
    st.sidebar.markdown("📒 **Part I Introduction**")

    # ✅ Part II: English Vowels (Collapsible)
    with st.sidebar.expander("📕 **Part II English Vowels**", expanded=False):
        st.markdown("- 📕 [Lessons 1-4](#)")
        st.markdown("- 📕 [Lessons 5-7](#)")
        st.markdown("- 📕 [Lessons 8-9](#)")

    # ✅ Part III: English Prosody (Collapsible)
    with st.sidebar.expander("📗 **Part III English Prosody**", expanded=False):
        st.markdown("- 📗 [Lesson 10](#)")
