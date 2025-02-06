import streamlit as st

# Create four tabs
tabs = st.tabs(["📗 Basics 1", "📗 Basics 2", "📗 Basics 3", "📗 Basics 4"])

# Content for each tab
with tabs[0]:
    st.header("Basics 1: Understanding English Sounds")

    # GitHub raw URLs for the MP3 files with descriptions
    audio_files = {
        "1: Unique set of sounds:": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-01.mp3",
            "desc": "Every language has its own set of sounds. Let's explore how English differs from other languages."
        },
        "2: Speech gestures...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-02.mp3",
            "desc": "Small changes in mouth shape and tongue position can greatly affect pronunciation and meaning."
        },
        "3: How we approach...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-03.mp3",
            "desc": "How can we train our ears and mouths to master new sounds in English? Let's find out!"
        },
    }

    # Display each title with description and playable audio
    for title, data in audio_files.items():
        st.subheader(title)
        st.write(data["desc"])  # Add description under each title
        st.audio(data["url"], format="audio/mp3")
with tabs[1]:
    st.header("Basics 2")
    st.write("Content for Basics 2 goes here.")

with tabs[2]:
    st.header("Basics 3")
    st.write("Content for Basics 3 goes here.")

with tabs[3]:
    st.header("Basics 4")
    st.write("Content for Basics 4 goes here.")
