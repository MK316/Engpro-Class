import streamlit as st
from gtts import gTTS
import io
import time

# Create tabs
tabs = st.tabs(["Lesson8", "Lesson9", "Listening"])

# Lesson 8 Content
with tabs[0]:
    st.markdown("### 📒 Lesson 8: Unstressed vowel (schwa vowel) as in ‘ago’, ‘upon’, ‘company’")

    # Introduction
    st.markdown("### Understanding Iambic and Trochaic Foot")
    st.write("English words follow different rhythmic patterns. The **iambic foot** consists of a weak (short) syllable followed by a strong (long) syllable, while the **trochaic foot** follows a strong-weak pattern.")

    # User selection for foot type
    foot_type = st.radio("Choose a rhythm pattern:", ["Iambic (Weak-Strong)", "Trochaic (Strong-Weak)"])

    # Examples of Iambic and Trochaic Words
    word_patterns = {
        "Iambic (Weak-Strong)": [
            "about", "around", "again", "asleep", "today"
        ],
        "Trochaic (Strong-Weak)": [
            "happy", "doctor", "mother", "table", "yellow"
        ]
    }

    selected_words = word_patterns[foot_type]
    words_text = ", ".join(selected_words)
    st.markdown("---")
    st.markdown(f"#### 1. 🎧 Listen to {foot_type} Words")

    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    st.write(f"**Words:** {words_text}")
    if st.button(f"Play All {foot_type} Words"):
        audio_data = generate_audio(words_text)
        st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("---")
    # Rhythmic Beat Practice
    st.markdown(f"#### 2. 🎧 Practice {foot_type} with Beats")
    st.write("Tap along with the beats to feel the rhythm pattern!")

    if st.button("Start Beat Practice"):
        if foot_type == "Iambic (Weak-Strong)":
            st.write("🎵 ago | away | along | amaze| contain")
            time.sleep(0.5)
            # Use a pre-recorded audio file for melody beats
            beat_audio_url = "https://github.com/MK316/Engpro-Class/raw/main/audio/iambic.wav"
            st.audio(beat_audio_url, format='audio/wav')
            for _ in range(5):
                st.write("• (weak)   ➝   ● (strong)")
                time.sleep(1)
        else:
            st.write("🎵 soda | nation | zebra | papa | open")
            time.sleep(0.5)
            # Use a pre-recorded audio file for melody beats
            beat_audio_url = "https://github.com/MK316/Engpro-Class/raw/main/audio/trochaic.wav"
            st.audio(beat_audio_url, format='audio/wav')
            for _ in range(5):
                st.write("● (strong)   ➝   • (weak)")
                time.sleep(1.5)


# Placeholder for Lesson 9
with tabs[1]:
    st.markdown("### 📒 Lesson 9: R-colored vowels as in ‘perfect’ and ‘percent’")

# Placeholder for Listening
with tabs[2]:
    st.markdown("### 🎧 Listening Practice")
    st.write("- Lesson 8")
    st.write("- Lesson 9")
