import streamlit as st
from gtts import gTTS
import random
from io import BytesIO
import os

# Create four tabs
tabs = st.tabs(["💧 Lesson 14", "💧 Lesson 15", "💧 Lesson 16", "💧 Lesson 17"])

# Content for each tab
# Sample dataset of irregular words
with tabs[0]:
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
    
    st.markdown("### 📒 Lesson 14:")
    st.markdown("#### 🗣️ Irregularity of English Words: Sound and Spelling")
    
    # Initialize session state
    if "current_word" not in st.session_state:
        st.session_state.current_word = None
    if "audio_data" not in st.session_state:
        st.session_state.audio_data = None
    if "show_spelling" not in st.session_state:
        st.session_state.show_spelling = False
    
    # Start button: choose word + generate audio
    if st.button("▶️ Start"):
        st.session_state.current_word = random.choice(word_data)
        st.session_state.show_spelling = False  # Reset spelling flag
    
        try:
            tts = gTTS(st.session_state.current_word["word"])
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.session_state.audio_data = audio_fp.read()  # store audio bytes in session
            st.audio(st.session_state.audio_data, format="audio/mp3")
        except Exception as e:
            st.session_state.audio_data = None
            st.error("❌ Failed to generate audio. Check internet or rate limits.")
            st.exception(e)
    
    # Replay audio if already generated
    if st.session_state.audio_data and not st.session_state.show_spelling:
        st.audio(st.session_state.audio_data, format="audio/mp3")
    
    # Show Spelling button
    if st.session_state.current_word:
        if st.button("🔤 Show Spelling"):
            st.session_state.show_spelling = True
    
    # Display spelling if toggled
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
