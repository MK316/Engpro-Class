import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# Function to generate audio from text
def text_to_speech(text):
    tts = gTTS(text, lang='en')  # Using 'ko' for Korean pronunciation
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

# Main function defining the Streamlit app
def main():
    st.title("Class Name Caller")
    st.markdown("### Teacher's Talk")
    st.markdown("🔊 Calling will begin shortly. Please listen to your name and respond with 'Present'.")

    # User selects the CSV file column for names
    url = "https://github.com/MK316/Engpro-Class/raw/main/data/s25engpro-roster1.csv"
    data = pd.read_csv(url)

    # Let the user choose which column of names to use
    name_column = st.radio("Choose which names to call:", ('Names', 'ENames'))

    # Extract names from the selected column
    names = data[name_column].tolist()

    # Initialize or reset the name ID (nid) using Streamlit's session state
    if 'nid' not in st.session_state or st.button("Reset Counter"):
        st.session_state.nid = 1  # Resets or initializes the counter

    if st.button("Start Calling Names"):
        # Process each name and increment nid after each call
        for name in names:
            st.write(f"Now calling: {st.session_state.nid}")
            audio_response = text_to_speech(name)
            st.audio(audio_response, format='audio/mp3')
            st.session_state.nid += 1  # Increment nid in the session state

if __name__ == "__main__":
    main()
