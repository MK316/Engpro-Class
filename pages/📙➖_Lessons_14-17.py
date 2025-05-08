import streamlit as st
from gtts import gTTS
import random
from io import BytesIO

# Create four tabs
tabs = st.tabs(["💧 Lesson 14", "💧 Lesson 15", "💧 Lesson 16", "💧 Lesson 17"])

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

# Lesson content in the first tab
with tabs[0]:
    st.markdown("## 📒 Lesson 14: Irregular Sound-Spelling Words")
    st.markdown("#### [1] In English, spelling and sound correspondence often follows a one-to-many relationship.")
    st.write("Since the spelling does not represent an exact sound that the letter represents, it is helpful to use the International Phonetic Alphabet (IPA) to understand English pronunciation better.")
    
    # Initialize session state
    if "current_word" not in st.session_state:
        st.session_state.current_word = None
    if "audio_data" not in st.session_state:
        st.session_state.audio_data = None
    if "show_spelling" not in st.session_state:
        st.session_state.show_spelling = False

    # ▶️ Start button
    if st.button("▶️ Show me a sample word"):
        st.session_state.current_word = random.choice(word_data)
        st.session_state.show_spelling = False
        word = st.session_state.current_word["word"]

        try:
            tts = gTTS(text=word, lang='en')
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.session_state.audio_data = audio_fp.read()
        except Exception as e:
            st.session_state.audio_data = None
            st.error("❌ Failed to generate audio. This may be due to a rate limit or internet issue.")
            st.exception(e)

    # 🔊 Play audio if available
    if st.session_state.audio_data:
        st.audio(st.session_state.audio_data, format="audio/mp3")
    st.markdown("---")
    
    # ▶️ Show spelling button
    if st.session_state.current_word:
        if st.button("▶️ Display Spelling and Transcription (IPA)"):
            st.session_state.show_spelling = True
    
    # Show IPA spelling

    if st.session_state.current_word and st.session_state.show_spelling:
        word = st.session_state.current_word["word"]
        ipa = st.session_state.current_word["ipa"]
        st.markdown(
            f"""
            <div style="font-size: 36px; color: #787882;font-weight: bold;">⚪ Word: {word}</div>
            <div style="font-size: 36px; color: #121ab0;">⚪ IPA: /{ipa}/</div>
            """,
            unsafe_allow_html=True
        )
    st.markdown("---")
    st.markdown("#### [2] 🎧 Consonants grouped by voicing, place of articulation, and manner of articulation")

    word_pairs = [
        ("pie and bye", "He says bye now."),
        ("teen and dean", "He is a dean of the department."),
        ("Kate and gate", "Let's meet up at the gate nine."),
        ("leaf and leave", "He said, leave us alone."),
        ("breath and breathe", "He said, breathe again."),
        ("face and phase", "We are in the phase one."),
        ("pressure and pleasure", "It's my pleasure."),
        ("batch and badge", "He earned the badge by himself."),
    ]

    def generate_audio(word):
        try:
            tts = gTTS(text=word, lang='en')
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            return audio_fp.read()
        except Exception as e:
            st.error(f"⚠️ Could not generate audio for '{word}'.")
            return None

    for w1, w2 in word_pairs:
        st.markdown(f"**🔹 {w1}** & **{w2}**")
        col1, col2 = st.columns(2)
        with col1:
            audio1 = generate_audio(w1)
            if audio1:
                st.audio(audio1, format="audio/mp3")
        with col2:
            audio2 = generate_audio(w2)
            if audio2:
                st.audio(audio2, format="audio/mp3")
        st.write("---")


# Other lesson tabs
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
