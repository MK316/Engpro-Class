import streamlit as st
from gtts import gTTS
from io import BytesIO
import pandas as pd

# Load data with caching using the new method
@st.cache_data
def load_data(file_url):
    df = pd.read_csv(file_url, sep='\t', usecols=['SID', 'WORD', 'POS'], dtype=str)
    df.columns = df.columns.str.strip()
    df['SID'] = df['SID'].str.extract('(\d+)')[0].astype(int)
    df['WORD'] = df['WORD'].str.split().str[0]
    return df

def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_file = BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    return audio_file.getvalue()

def main():
    st.title("🎧 CEFR Listen & Spell Practice")
    st.caption("Level B has 733 words and Level C has 3,000 words.")
    tab1, tab2 = st.tabs(["Level B", "Level C"])

    with tab1:
        run_practice_app("User_LevelB", "https://raw.githubusercontent.com/MK316/CEFR/refs/heads/main/data/CEFRB1B2.txt")
    with tab2:
        run_practice_app("User_LevelC", "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/CEFRC1.txt")

def run_practice_app(user_name, file_url):
    data = load_data(file_url)
    start_sid = st.number_input("Start SID", min_value=1, max_value=len(data), value=1, key=f"{user_name}_start_sid")
    end_sid = st.number_input("End SID", min_value=1, max_value=len(data), value=min(20, len(data)), key=f"{user_name}_end_sid")
    filtered_data = data[(data['SID'] >= start_sid) & (data['SID'] <= end_sid)]

    audio_key_prefix = f"audio_{user_name}"
    input_key_prefix = f"input_{user_name}"

    generate_button_key = f"generate_audio_{user_name}"
    if st.button("Generate Audio", key=generate_button_key):
        for row in filtered_data.itertuples():
            audio_key = f"{audio_key_prefix}_{row.SID}"
            sid_key = f"{input_key_prefix}_{row.SID}"
            st.session_state[audio_key] = generate_audio(row.WORD)
            st.text_input("Type the word shown:", key=sid_key, placeholder="Type here...")

if __name__ == "__main__":
    main()
