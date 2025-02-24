import streamlit as st
from gtts import gTTS
from io import BytesIO
import pandas as pd

@st.cache_data
def load_data(file_url):
    # Loads data from a given URL and processes it
    df = pd.read_csv(file_url, sep='\t', usecols=['SID', 'WORD', 'POS'], dtype=str)
    df.columns = df.columns.str.strip()
    df['SID'] = df['SID'].str.extract('(\d+)')[0].astype(int)
    df['WORD'] = df['WORD'].str.split().str[0]
    return df

def generate_audio(text):
    # Generates audio from text using gTTS
    tts = gTTS(text=text, lang='en')
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file

def run_practice_app(user_name, file_url):
    # Main application logic for practice session
    data = load_data(file_url)
    total_words = len(data)
    st.header(f"Welcome, {user_name}")
    start_sid = st.number_input("Start SID", min_value=1, max_value=total_words, value=1, key=f"{user_name}_start_sid")
    end_sid = st.number_input("End SID", min_value=1, max_value=total_words, value=min(20, total_words), key=f"{user_name}_end_sid")
    filtered_data = data[(data['SID'] >= start_sid) & (data['SID'] <= end_sid)]

    if st.button("Generate Audio", key=f"generate_{user_name}"):
        for row in filtered_data.itertuples():
            audio_data = generate_audio(row.WORD)
            audio_key = f"audio_{row.SID}"
            st.session_state[audio_key] = audio_data
            st.audio(st.session_state[audio_key], format='audio/mp3', start_time=0)

def main():
    # Main entry point for the Streamlit app
    st.title("🎧 CEFR Listen & Spell Practice")
    tab1, tab2 = st.tabs(["Level B", "Level C"])

    with tab1:
        run_practice_app("User_LevelB", "https://raw.githubusercontent.com/MK316/CEFR/refs/heads/main/data/CEFRB1B2.txt")
    with tab2:
        run_practice_app("User_LevelC", "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/CEFRC1.txt")

if __name__ == "__main__":
    main()
