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
            ("about", "a-BOUT"),
            ("around", "a-ROUND"),
            ("again", "a-GAIN"),
            ("asleep", "a-SLEEP"),
            ("today", "to-DAY")
        ],
        "Trochaic (Strong-Weak)": [
            ("happy", "HAP-py"),
            ("doctor", "DOC-tor"),
            ("mother", "MOTH-er"),
            ("table", "TA-ble"),
            ("yellow", "YEL-low")
        ]
    }

    selected_words = word_patterns[foot_type]

    st.markdown(f"### 🎧 Listen to {foot_type} Words")

    def generate_audio(word, pronunciation):
        text = f"{word}. {pronunciation}."
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    for word, pronunciation in selected_words:
        st.write(f"**{word}** - {pronunciation}")
        if st.button(f"Play {word}", key=f"audio_{word}"):
            audio_data = generate_audio(word, pronunciation)
            st.audio(audio_data.getvalue(), format='audio/mp3')

    # Rhythmic Beat Practice
    st.markdown(f"### 🥁 Practice {foot_type} Foot with Beats")
    st.write("Tap along with the beats to feel the rhythm pattern!")

    if st.button("Start Beat Practice"):
        if foot_type == "Iambic (Weak-Strong)":
            st.write("🎵 Weak - Strong | Weak - Strong | Weak - Strong")
            time.sleep(0.5)
            for _ in range(3):
                st.write("• (weak)   ➝   ● (strong)")
                time.sleep(1)
        else:
            st.write("🎵 Strong - Weak | Strong - Weak | Strong - Weak")
            time.sleep(0.5)
            for _ in range(3):
                st.write("● (strong)   ➝   • (weak)")
                time.sleep(1)

# Placeholder for Lesson 9
with tabs[1]:
    st.markdown("### 📒 Lesson 9: R-colored vowels as in ‘perfect’ and ‘percent’")

# Placeholder for Listening
with tabs[2]:
    st.markdown("### 🎧 Listening Practice")
    st.write("- Lesson 8")
    st.write("- Lesson 9")
