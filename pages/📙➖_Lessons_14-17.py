import streamlit as st
from gtts import gTTS
import random
from io import BytesIO

# Create four tabs
tabs = st.tabs(["💧 Lesson 14", "💧 Lesson 15", "💧 Lesson 16", "💧 Lesson 17"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 14: ")


    
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
    
    st.markdown("#### 🗣️ Irregularity of English Words: Sound and Spelling")
    
    # Use session state to persist selected word
    if "current_word" not in st.session_state:
        st.session_state.current_word = None
    
    # Start button
    try:
        tts = gTTS(st.session_state.current_word["word"])
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format="audio/mp3")
    except Exception as e:
        st.error("❌ Failed to generate audio. Please check your internet connection or try again later.")
        st.exception(e)

    
    # If word is selected, offer to show spelling
    if st.session_state.current_word:
        if st.button("🔤 Show Spelling"):
            word = st.session_state.current_word["word"]
            ipa = st.session_state.current_word["ipa"]
            st.markdown(f"**Word**: `{word}`  \n**IPA**: /{ipa}/")






with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
