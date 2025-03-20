import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import time
import os

def load_names(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")
    data = pd.read_csv(path)
    return data['Names'].tolist()

def text_to_speech(text):
    tts = gTTS(text, lang='en')
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

def main():
    st.title("Class Name Caller")
    st.markdown("### Teacher's Talk")
    st.markdown("🔊 Calling will begin shortly. Please listen to your name and respond with 'Present'.")

    path = st.text_input("Enter the path to the CSV file:", value="https://github.com/MK316/Engpro-Class/raw/main/data/Engpro-roster25.csv")

    if path:
        try:
            names = load_names(path)
        except FileNotFoundError as e:
            st.error(e)
            return

        if st.button("Start Calling Names"):
            for name in names:
                audio_response = text_to_speech(name)
                st.audio(audio_response, format='audio/mp3')
                st.write(f"Now calling: {name}")
                time.sleep(1)

                if name != names[-1]:
                    interjection = "Next up,"
                    audio_response = text_to_speech(interjection)
                    st.audio(audio_response, format='audio/mp3')
                    time.sleep(0.5)

if __name__ == "__main__":
    main()
