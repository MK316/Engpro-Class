import streamlit as st
from gtts import gTTS
import random
from io import BytesIO
import os

# Create four tabs
tabs = st.tabs(["💧 Lesson 14", "💧 Lesson 15", "💧 Lesson 16", "💧 Lesson 17"])

# Content for each tab
# Sample dataset of irregular words
word_data = [
    {"word": "said", "ipa": "sɛd"},
    {"word": "busy", "ipa": "bɪzi"},
    {"word": "one", "ipa": "wʌn"},
    {"word": "two", "ipa": "tu"},
    {"word": "done", "ipa": "dʌn"},
    {"word": "love", "ipa": "lʌv"},
    {"word": "move", "ipa": "muv"},
    {"word": "once", "ipa": "wʌns"},
    {"word": "colonel", "ipa": "kɝnəl"},
    {"word": "island", "ipa": "aɪlənd"},
    {"word": "knife", "ipa": "naɪf"},
    {"word": "hour", "ipa": "aʊɚ"},
    {"word": "answer", "ipa": "ænsɚ"},
    {"word": "listen", "ipa": "lɪsən"},
    {"word": "choir", "ipa": "kwaɪɚ"},
    {"word": "though", "ipa": "ðoʊ"},
    {"word": "through", "ipa": "θru"},
    {"word": "cough", "ipa": "kɔf"},
    {"word": "bought", "ipa": "bɔt"},
    {"word": "enough", "ipa": "ɪnʌf"},
]

# 📒 Content for Lesson 14 tab
with tabs[0]:
    st.markdown("### 📒 Lesson 14:")
    st.markdown("#### 🗣️ Irregularity of English Words: Sound and Spelling")

    # Initialize session state
    if "current_word" not in st.session_state:
        st.session_state.current_word = None
    if "show_spelling" not in st.session_state:
        st.session_state.show_spelling = False

    # Start button
    if st.button("▶️ Start"):
        st.session_state.current_word = random.choice(word_data)
        st.session_state.show_spelling = False  # Reset spelling display
        word = st.session_state.current_word["word"]
        try:
            # Use pre-generated mp3 file stored in "audio" folder
            st.audio(f"audio/{word}.mp3", format="audio/mp3")
        except FileNotFoundError:
            st.error(f"❌ Audio file for '{word}' not found.")

    # Show spelling button
    if st.session_state.current_word:
        if st.button("🔤 Show Spelling"):
            st.session_state.show_spelling = True

    if st.session_state.current_word and st.session_state.show_spelling:
        word = st.session_state.current_word["word"]
        ipa = st.session_state.current_word["ipa"]
        st.markdown(f"**Word**: `{word}`  \n**IPA**: /{ipa}/")
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
