import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import time

path = st.text_input("Enter the path to the CSV file:", value="path/to/your/names.csv")

# Load names from a CSV file
@st.cache
def load_names(path):
    data = pd.read_csv(path)
    return data['Names'].tolist()

# Generate speech from text
def text_to_speech(text):
    tts = gTTS(text, lang='en')
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

def main():
    st.title("Class Name Caller")

    # Display an introductory message
    st.markdown("### Teacher's Talk")
    st.markdown("🔊 Calling will begin shortly. Please listen to your name and respond with 'Present'.")

    # Load names
    
    if path:
        names = load_names(path)

        # Button to start the name calling
        if st.button("Start Calling Names"):
            for name in names:
                # Generate and play name
                audio_response = text_to_speech(name)
                st.audio(audio_response, format='audio/mp3')
                st.write(f"Now calling: {name}")
                time.sleep(1)  # Wait for a bit after each name

                # Optional teacher's natural response
                if name != names[-1]:  # To avoid a response after the last name
                    interjection = "Next up,"
                    audio_response = text_to_speech(interjection)
                    st.audio(audio_response, format='audio/mp3')
                    time.sleep(0.5)  # Short pause between names


if __name__ == "__main__":
    main()
