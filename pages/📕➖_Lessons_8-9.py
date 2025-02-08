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
    st.caption("Workbook page 50")

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
    st.markdown("### A. Warming up: [ə]")

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

    st.markdown("---")
    st.markdown("### B. Schwa vowel [ə] in spelling: 'a, e, i, o, u, y'")
    st.markdown("**arrive, oven, liquid, occur, upon**")
    st.markdown("**ashamed, belief, typical, lesson, column**")

    st.markdown("---")
    st.markdown("### C. Stressed vs. unstressed vowel duration")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/stress1.jpg", caption="Stress also changes the vowel quality")
    
# Placeholder for Lesson 9
# Lesson 9 Content
with tabs[1]:
    st.markdown("#### 📒 Lesson 9: R-colored vowels in American English")
    st.caption("Workbook page 54")
    
    # Explanation of R-colored vowels
    st.markdown("""
    **[1]** In American English, when an ‘r’ sound follows a vowel within a syllable, they behave as one unit.  
    **[2]** Most British English speakers do not pronounce ‘r’ **after a vowel**, while American English speakers do pronounce ‘r’ together with the vowel.  
    **[3]** When ‘r’ is pronounced in conjunction with a vowel, we use the symbols **[ɝ] (stressed)** and **[ɚ] (unstressed)** depending on the presence or absence of stress.  
    """)

    # Visual representation of [ɝ] vs. [ɚ]
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### **[ɝ] (stressed)**")
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/perfect.jpg", caption="/ˈpɝfɛkt/")

    with col2:
        st.markdown("### **[ɚ] (unstressed)**")
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/perfume.jpg", caption="/pɚˈfjum/")

    # Warming-up practice
    st.markdown("## **A. Warming up: [ɝ] (stressed)**")
    
    stressed_words = {
        "At the beginning of words": "earth, earn, irk, herb, early, urgent, urban",
        "In the middle of words": "turn, burn, learn, heard, verb, word, curve, third, Thursday, circus, bird, firm, hurt, term",
        "At the end of words": "sir, her, fur, prefer, defer, occur"
    }

    unstressed_words = {
        "At the beginning of words": "NA",
        "In the middle of words": "perhaps, surprise, flowerpot, understood",
        "At the end of words": "baker, mirror, butter, weather, sooner, failure, nature, grammar, dollar"
    }

    # Audio generation function
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    # Display buttons to play audio with words by position
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Play Beginning Words [ɝ]", key="begin_ɝ"):
            audio_data = generate_audio(stressed_words["At the beginning of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(stressed_words["At the beginning of words"])

    with col2:
        if st.button("Play Middle Words [ɝ]", key="middle_ɝ"):
            audio_data = generate_audio(stressed_words["In the middle of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(stressed_words["In the middle of words"])

    with col3:
        if st.button("Play End Words [ɝ]", key="end_ɝ"):
            audio_data = generate_audio(stressed_words["At the end of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(stressed_words["At the end of words"])

    st.markdown("## **B. Warming up: [ɚ] (unstressed)**")

    col4, col5, col6 = st.columns(3)
    with col4:
        if st.button("Play Beginning Words [ɚ]", key="begin_ɚ"):
            st.write("No words start with this vowel.")
    
    with col5:
        if st.button("Play Middle Words [ɚ]", key="middle_ɚ"):
            audio_data = generate_audio(unstressed_words["In the middle of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(unstressed_words["In the middle of words"])

    with col6:
        if st.button("Play End Words [ɚ]", key="end_ɚ"):
            audio_data = generate_audio(unstressed_words["At the end of words"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(unstressed_words["At the end of words"])


# Placeholder for Listening
with tabs[2]:
    st.markdown("### 🎧 Listening Practice")
    st.markdown("""
    - [Lesson 8](https://engpro-listening.streamlit.app/Lesson_08)
    - [Lesson 9](https://engpro-listening.streamlit.app/Lesson_09)
    """)
