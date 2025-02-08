import streamlit as st
import io
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from gtts import gTTS
import soundfile as sf


# Create four tabs
tabs = st.tabs(["📗 Lesson 11", "❄️ App1", "❄️ App2", "❄️ App3"])

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
    "5) To tell the truth, I was quite nervous before giving the presentation.": 
    "To tell the truth, I was quite nervous before giving the presentation."
}

# Title
st.markdown("##### 🎧 Listen to the Sentences")

# User selects a sentence
selected_example_sentence = st.selectbox("Choose a sentence to hear the pronunciation:", list(example_sentences.keys()))

# Function to generate and return audio file
def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    return audio_data

# Generate and Play Audio
if st.button("Play Selected Sentence"):
    audio_data = generate_audio(example_sentences[selected_example_sentence])
    st.audio(audio_data.getvalue(), format='audio/mp3')
    st.write(f"**Sentence:** {example_sentences[selected_example_sentence]}")

    # Save generated audio for pitch analysis
    temp_audio_path = "temp_audio.wav"
    with open(temp_audio_path, "wb") as f:
        f.write(audio_data.getvalue())

    # Load and Downsample Audio for Faster Processing
    y, sr = librosa.load(temp_audio_path, sr=8000)  # Downsampling to 8kHz for speed

    # Extract Pitch (Fundamental Frequency)
    f0, voiced_flag, voiced_probs = librosa.pyin(y, fmin=50, fmax=300)
    
    # Convert time array to match pitch points
    times = np.linspace(0, len(y) / sr, len(f0))

    # Plot the Pitch Contour
    st.markdown("##### 📈 Pitch Contour of the Sentence")
    fig, ax = plt.subplots(figsize=(6, 2))
    
    ax.plot(times, f0, marker="o", markersize=3, color="blue", label="Pitch Contour")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Frequency (Hz)")
    ax.set_title("Pitch Contour")
    ax.legend()
    
    st.pyplot(fig)

with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
