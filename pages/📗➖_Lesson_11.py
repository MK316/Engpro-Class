import streamlit as st
import io
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from gtts import gTTS
import soundfile as sf


# Create four tabs
tabs = st.tabs(["📗 Lesson 11", "❄️ Pitch-contour-app"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 11: Accents in English")
    st.write("In addition to word stress, which is assigned to individual syllables, English words can also receive accents within a sentence. This combination of stress and accent leads to greater emphasis. For instance, stressed syllables are naturally more emphasized than unstressed ones. Moreover, stressed syllables in accented words are even stronger and longer than those in unaccented words.")
    st.write("Example) My **younger** brother ate **ten** chocolate **cookies.**")

    st.markdown("##### 1. New information is usually accented with a high pitch")
    st.write("My name is Jane Smith. (H* vs. L* carry different meanings)")
    
    st.markdown("##### 2. The final key word within a sentence receives the most emphasis in English.")
    st.markdown("""
    A. Steve is my **cousin**.
    B. He is at the **store**.
    C. Today is **Saturday**.
    """)

    st.markdown("##### 3. Function words are not accented unless they are intentionally emphasized.")
    st.markdown("""
    - Function words: articles (a, the), prepositions (for, of, in, to, etc.),
    - pronouns (I, her, he, she, you, they, etc.)
    - conjunctions (but, and, as, etc.)
    - helping verbs (is, was, are, were, has, can, etc.)
    """)

# Example Sentences
example_sentences = {
    "1) Today is Thursday.": "Today is Thursday.",
    "2) The lecture will start in a moment.": "The lecture will start in a moment.",
    "3) You’ll see him sooner or later.": "You’ll see him sooner or later.",
    "4) I wanna be a singer.": "I wanna be a singer.",
    "5) To tell the truth, I was quite nervous before giving the presentation.": "To tell the truth, I was quite nervous before giving the presentation.",
    "6) To tell the truth, I was quite nervous before giving the presentation 2": "https://github.com/MK316/Engpro-Class/raw/main/audio/totellthetruth.mp3"  # Update with your actual URL
}

# Title
st.markdown("##### 🎧 Listen to the Sentences")

# User selects a sentence
selected_example_sentence = st.selectbox("Choose a sentence to hear the pronunciation:", list(example_sentences.keys()))

# Function to generate and return audio file
def generate_audio(text):
    if "http" not in text:
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    else:
        return text  # Return the URL for the sixth sentence

# Generate and Play Audio
if st.button("Play Selected Sentence"):
    audio_data = generate_audio(example_sentences[selected_example_sentence])
    if isinstance(audio_data, io.BytesIO):
        st.audio(audio_data.getvalue(), format='audio/mp3')
    else:
        st.audio(audio_data, format='audio/mp3')  # Play the audio from the URL directly
    st.write(f"**Sentence:** {selected_example_sentence}")


with tabs[1]:
    st.markdown("### 📒 Show Pitch Contour")

    # Directly open the link when clicking the button
    st.markdown(
        '<a href="https://mrkim21.github.io/appfolder/tts-pitch.html" target="_blank">'
        '<button style="padding:10px 20px; font-size:16px;">Open Pitch Contour App</button>'
        '</a>', 
        unsafe_allow_html=True
    )


