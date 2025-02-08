import streamlit as st
from gtts import gTTS
from PIL import Image
import random
import time
import io

# Create five tabs
tabs = st.tabs(["💧 Lesson 1", "💧 Lesson 2", "💧 Lesson 3", "💧 Lesson 4", "Listening practice"])

if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# Define a function to toggle the visibility state
def toggle_image():
    st.session_state.show_image = not st.session_state.show_image

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 1: Pronouncing English vowels")
    st.markdown("#### A. Monophthong vowels (=single vowels)")
    
    frame_sentence = "I say {} again."
    target_words = ["heed", "hid", "head", "had", "who'd", "hood", "hawed", "hod", "hud", "ago"]
    target_words_extended = target_words + ["all words together"]
    
    selected_word = st.selectbox("Choose a word to insert into the sentence or select 'all words together':", target_words_extended)
    
    if selected_word == "all words together":
        full_sentence = " ".join([frame_sentence.format(word) for word in target_words])
    else:
        full_sentence = frame_sentence.format(selected_word)
    
    st.write("Generated Sentence: ", full_sentence)
    
    if st.button("Generate Audio", key="audio_1"):
        tts = gTTS(text=full_sentence, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        st.audio(audio_data.getvalue(), format='audio/mp3')
    
    st.markdown("#### B. Diphthong vowels (=double vowels)")
    st.caption("Diphthong vowels start with one sound and glide into a different vowel.")
    
    if st.button("Show chart: diphthong vowels", on_click=toggle_image, key="chart_1"):
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/Vowelchart.png", caption="Vowel chart")
    
with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/sheep.png", width=300, caption="Sheep")
    with col2:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/ship.png", width=300, caption="Ship")
    
    sentences = ["The children are cleaning the ship", "The children are cleaning the sheep"]
    
    if st.button("Audio", key="audio_2"):
        chosen_sentence = random.choice(sentences)
        tts = gTTS(text=chosen_sentence, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(chosen_sentence)
    
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - suit vs. soot")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/suit.jpg", width=300, caption="Suit")
    with col2:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/soot.jpg", width=300, caption="Soot")
    
    sentences_u = ["He is cleaning the suit damaged by the fire.", "He is cleaning the soot damaged by the fire."]
    
    if st.button("Audio", key="audio_3"):
        chosen_sentence_u = random.choice(sentences_u)
        tts = gTTS(text=chosen_sentence_u, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(chosen_sentence_u)
    
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
    
with tabs[4]:
    st.title("Listening practice")
    st.markdown("""
    - [Lesson 1](https://engpro-listening.streamlit.app/Lesson_01)
    - [Lesson 2](https://engpro-listening.streamlit.app/Lesson_02)
    """)
