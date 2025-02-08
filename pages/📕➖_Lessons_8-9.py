import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np
from gtts import gTTS
import io
import time

# Create tabs
tabs = st.tabs(["Lesson8", "Lesson9", "Listening"])

# Lesson 8 Content
with tabs[0]:
    st.markdown("#### 📒 Lesson 8: Unstressed vowel (schwa vowel)")

    # Introduction
    st.markdown("#### 1. Understanding Iambic and Trochaic beat (Foot)")
    st.write("English words follow different rhythmic patterns. The **iambic foot** consists of a weak (short) syllable followed by a strong (long) syllable, while the **trochaic foot** follows a strong-weak pattern.")

    # User selection for foot type
    foot_type = st.radio("Choose a rhythm pattern:", ["Iambic (Weak-Strong)", "Trochaic (Strong-Weak)"])

    # Visualization of rhythmic pattern
    st.markdown("**Visualization of Iambic and Trochaic Patterns**")
    fig, ax = plt.subplots(figsize=(6, 2))
    
    # Define positions for circles
    positions = np.linspace(0, 10, 6)
    
    # Define correct sizes and colors
    if foot_type == "Iambic (Weak-Strong)":
        sizes = [(0.5, 0.3), (2, 0.3)] * 3  # Small (circle) -> Large (wide ellipse)
        colors = ['gray', 'orange'] * 3  # Small = Gray, Large = Orange
    else:
        sizes = [(2, 0.3), (0.5, 0.3)] * 3  # Large (wide ellipse) -> Small (circle)
        colors = ['orange', 'gray'] * 3  # Large = Orange, Small = Gray
    
    # Plot ellipses with correct sizes and colors
    for pos, (width, height), color in zip(positions, sizes, colors):
        ellipse = Ellipse((pos, 1), width=width, height=height, color=color, alpha=0.8)
        ax.add_patch(ellipse)
    
    ax.set_xlim(-1, 11)
    ax.set_ylim(0, 2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)
    
    st.pyplot(fig)

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
    st.markdown(f"#### 3. 🎧 Listen to {foot_type} Words")

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
    st.markdown("### Warming up: [ə]")

    # Word lists by position
    word_lists = {
        "At the beginning of words": "ago, away, along, amaze, contain, suppose, asleep, upon, arrive, obtain, typical, cousin, capital, support",
        "In the middle of words": "agony, relative, holiday, buffalo, telephone, company, belief, jacket, cement, open, believe, signal, famous, nation, certain",
        "At the end of words": "soda, sofa, zebra, papa, believe, signal, famous, nation, certain"
    }
    
    # Function to generate audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Layout with columns for buttons
    st.markdown("### 🎧 Practice Words by Position")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Beginning Position"):
            st.write(f"**Words:** {word_lists['At the beginning of words']}")
            audio_data = generate_audio(word_lists["At the beginning of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
    
    with col2:
        if st.button("Middle Position"):
            st.write(f"**Words:** {word_lists['In the middle of words']}")
            audio_data = generate_audio(word_lists["In the middle of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
    
    with col3:
        if st.button("End Position"):
            st.write(f"**Words:** {word_lists['At the end of words']}")
            audio_data = generate_audio(word_lists["At the end of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')

# Placeholder for Lesson 9
with tabs[1]:
    st.markdown("### 📒 Lesson 9: R-colored vowels as in ‘perfect’ and ‘percent’")

# Placeholder for Listening
with tabs[2]:
    st.markdown("### 🎧 Listening Practice")
    st.write("- Lesson 8")
    st.write("- Lesson 9")
