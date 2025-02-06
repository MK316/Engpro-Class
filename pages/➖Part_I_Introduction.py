import streamlit as st

# Create four tabs
tabs = st.tabs(["📗 Basics 1", "📗 Basics 2", "📗 Basics 3", "📗 Basics 4"])

# Content for each tab
with tabs[0]:
    st.markdown("### Basics 1: Understanding English Sounds")

    # GitHub raw URLs for the MP3 files with descriptions
    audio_files = {
        "1. Unique set of sounds:": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-01.mp3",
            "desc": "Every language has its own unique set of sounds. When learning a second language, the first step is figuring out which sounds are familiar—similar to the ones in our native language—and which ones are completely new. Once we know that, we can focus on practicing the new sounds by learning how to shape our mouth and move our tongue in the right way."
        },
        "2. Speech gestures...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-02.mp3",
            "desc": "Even small changes in how we shape our mouth or move our tongue can make a big difference in how sounds are produced and understood. These changes might completely change the meaning of a word, make speech sound accented, or sometimes have no effect on the actual sounds—but they can still impact things like tone and expressiveness. "
        },
        "3. How we approach...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-03.mp3",
            "desc": "In this course, we'll learn how to pronounce individual English sounds by understanding how they’re made and practicing them. We’ll also work on putting sounds together to form words and using tone and rhythm to communicate naturally with English speakers."
        },
        "4. Letters and sounds...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-04.mp3",
            "desc": "Here's a question: Do we really need to learn IPA symbols? Isn't knowing how to spell words enough? Note that English spelling can be pretty tricky—it often doesn't tell us much about how words are actually pronounced. For example, let's take the word sigh. How many letters does it have? Now, how many different sounds do you hear?"
        },
    }

    # Display each title with description and playable audio
    for title, data in audio_files.items():
        st.subheader(title)
        st.write(data["desc"])  # Add description under each title
        st.audio(data["url"], format="audio/mp3")
import streamlit as st

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

    # Button to show the worksheet image
    if st.button("Show example worksheet"):
        worksheet_url = "https://github.com/MK316/Engpro-Class/raw/main/images/P1-04example.png"
        st.image(worksheet_url, caption="Example Worksheet (p.14)", use_container_width=True)

    
with tabs[1]:
    st.header("Basics 2")
    st.write("Content for Basics 2 goes here.")

with tabs[2]:
    st.header("Basics 3")
    st.write("Content for Basics 3 goes here.")

with tabs[3]:
    st.header("Basics 4")
    st.write("Content for Basics 4 goes here.")
