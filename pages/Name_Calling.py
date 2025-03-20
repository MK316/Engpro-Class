import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# Function to generate audio from text
def text_to_speech(text):
    tts = gTTS(text, lang='en')  # Using 'ko' for Korean
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Main function defining the Streamlit app
def main():
    st.title("Class Name Caller")
    st.markdown("### Teacher's Talk")
    st.markdown("🔊 Calling will begin shortly. Please listen to your name and respond with 'Present'.")

    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/data/Engpro-roster25.csv"
    data = pd.read_csv(url)
    names = data['Names'].tolist()

    if st.button("Start Calling Names"):
        for name in names:
            st.write(f"Now calling:")
            # Generate audio for the name
            audio_response = text_to_speech(name)
            # Display audio player for the generated audio
            st.audio(audio_response, format='audio/mp3')

if __name__ == "__main__":
    main()
