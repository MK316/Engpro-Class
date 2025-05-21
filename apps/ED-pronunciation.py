import streamlit as st
import pandas as pd
import random
from gtts import gTTS
from io import BytesIO

# Load CSV from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/ed-pronunciation.csv"
    df = pd.read_csv(url)
    return df

# Convert to regular past tense
def to_past_tense(word):
    if word.endswith("e"):
        return word + "d"
    elif word.endswith("y") and word[-2] not in "aeiou":
        return word[:-1] + "ied"
    elif (len(word) >= 3 and
          word[-1] not in "aeiouywx" and
          word[-2] in "aeiou" and
          word[-3] not in "aeiou"):
        return word + word[-1] + "ed"
    else:
        return word + "ed"

# Generate audio
def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Load data
df = load_data()
verbs = df[df['POS'].str.startswith("v", na=False)]["WORD"].dropna().unique().tolist()

st.title("🎧 Regular Verb: Present + Past Form Audio Practice")

# Selection: number of items
num_choice = st.radio("How many words to practice?", [5, 10, 20, "All"], horizontal=True)

# Initialize session state
if "selected_words" not in st.session_state:
    st.session_state.selected_words = []
    st.session_state.index = 0
    st.session_state.started = False

# Start Button
if st.button("▶️ Start") or st.session_state.started:
    if not st.session_state.started:
        total = len(verbs)
        count = total if num_choice == "All" else int(num_choice)
        st.session_state.selected_words = random.sample(verbs, count)
        st.session_state.index = 0
        st.session_state.started = True

    # Check if done
    if st.session_state.index >= len(st.session_state.selected_words):
        st.success("🎉 Completed!")
    else:
        current_word = st.session_state.selected_words[st.session_state.index].strip().lower()
        past_form = to_past_tense(current_word)
        combined_text = f"{current_word} and {past_form}"
        
        st.markdown(f"### 🔤 {combined_text}")
        audio = generate_audio(combined_text)
        st.audio(audio, format="audio/mp3")

        if st.button("➡️ Next"):
            st.session_state.index += 1
