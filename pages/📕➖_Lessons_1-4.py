import streamlit as st
from gtts import gTTS
from PIL import Image
import io

# Create four tabs
tabs = st.tabs(["💧 Lesson 1", "💧 Lesson 2", "💧 Lesson 3", "💧 Lesson 4"])

if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# Define a function to toggle the visibility state
def toggle_image():
    st.session_state.show_image = not st.session_state.show_image

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 1: Pronouncing English vowels")
    st.markdown("#### A. Monophthong vowels (=single vowels)")
    
    # Frame sentence and target words
    frame_sentence = "I say {} again."
    target_words = ["heed", "hid", "head", "had", "who'd", "hood", "hawed", "hod", "hud", "ago"]
    
    # Adding an option to pronounce all words together
    target_words_extended = target_words + ["all words together"]

    # Dropdown to select the target word
    selected_word = st.selectbox("Choose a word to insert into the sentence or select 'all words together':", target_words_extended)
    
    # Check if the user selected "all words together"
    if selected_word == "all words together":
        # Generate a sentence concatenating all words
        all_words_sentence = " ".join([frame_sentence.format(word) for word in target_words])
        full_sentence = all_words_sentence
    else:
        # Generate the full sentence by inserting the selected word into the frame
        full_sentence = frame_sentence.format(selected_word)
    
    st.write("Generated Sentence: ", full_sentence)
    
    # Button to generate and play audio
    if st.button("Generate Audio"):
        # Use gTTS to convert the generated sentence to speech
        tts = gTTS(text=full_sentence, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        
        # Display the audio player with the generated audio
        st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("#### B. Diphthong vowels (=double vowels)")
    st.caption("Diphthong vowels start with one sound and glide into a different vowel. The smooth movement between these two ‘targets’ is crucial for correct pronunciation of diphthong vowels. This is not a sequence of two vowels: e.g., “I” in English and ‘아이’ in Korean are not exactly the same.")
    
    button = st.button("Show chart: diphthong vowels", on_click=toggle_image)

    # Conditional display of the image based on the session state
    if st.session_state.show_image:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/Vowelchart.png", caption="Vowel chart")
        st.caption("Image from Ladefoged & Johnson (2015; p.46), A course in phonetics")

with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")

