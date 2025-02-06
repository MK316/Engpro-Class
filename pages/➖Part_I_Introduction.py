import streamlit as st

# Create four tabs
tabs = st.tabs(["📗 Basics 1", "📗 Basics 2", "📗 Basics 3", "📗 Basics 4"])

# Content for each tab
with tabs[0]:
    st.header("Basics 1: Understanding English sounds")

    # GitHub raw URLs for the MP3 files
    audio_files = {
        "1: Unique set of sounds:": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-01.mp3",
        "2: Speech gestures...": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-02.mp3",
        "3: How we approach...": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-03.mp3",
    }

    # Display each word with its playable audio
    for word, url in audio_files.items():
        st.subheader(word)
        st.audio(url, format="audio/mp3")

with tabs[1]:
    st.header("Basics 2")
    st.write("Content for Basics 2 goes here.")

with tabs[2]:
    st.header("Basics 3")
    st.write("Content for Basics 3 goes here.")

with tabs[3]:
    st.header("Basics 4")
    st.write("Content for Basics 4 goes here.")
