import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# Function to generate audio from text
def text_to_speech(text):
    tts = gTTS(text, lang='en')  # Correct language code if needed
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer

def main():
    st.title("😍 Name Caller")
    st.markdown("### Teacher's Talk")
    intro = text_to_speech("Calling will begin shortly. Please listen to your name and respond with 'Present'.")
    st.audio(intro, format='audio/mp3')

    st.write("1. Roll call (Male teacher)")
    roster_audio1 = "https://github.com/MK316/Engpro-Class/raw/main/audio/roll-call-S25.mp3"
    st.audio(roster_audio1, format='audio/mp3')

    st.write("2. Roll call (Female teacher)")
    roster_audio2 = "https://github.com/MK316/Engpro-Class/raw/main/audio/roll-call-S25-F.mp3"
    st.audio(roster_audio2, format='audio/mp3')
    
    # User selects the CSV file column for names
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/data/s25engpro-roster2.csv"
    data = pd.read_csv(url)
    # st.write("Data columns:", data.columns)  # This will display the actual column names for debugging

    # Let the user choose which column of names to use, ensuring the exact case from the data
    name_column = st.radio("Choose which names to call:", ('Names', 'ENames'))

    # Check if the selected column exists in the DataFrame to avoid KeyErrors
    if name_column in data.columns:
        names = data[name_column].tolist()

        # Initialize or reset the name ID (nid) using Streamlit's session state
        if 'nid' not in st.session_state or st.button("Reset Counter"):
            st.session_state.nid = 1  # Resets or initializes the counter

        if st.button("Start Calling Names"):
            for name in names:
                st.write(f"Now calling: {st.session_state.nid}")
                audio_response = text_to_speech(name)
                st.audio(audio_response, format='audio/mp3')
                st.session_state.nid += 1  # Increment nid in the session state
    else:
        st.error(f"Selected column '{name_column}' does not exist in the data.")

if __name__ == "__main__":
    main()
