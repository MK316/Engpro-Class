import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# Function to convert word to regular past tense
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
def generate_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Load CSV from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/ed-pronunciation.csv"  # Update if needed
    df = pd.read_csv(url)
    return df

# Load and filter the dataset
df = load_data()

st.title("📝 Regular Verb Past Tense Converter + Audio")

# Filter just the verb entries
verbs = df[df['POS'].str.startswith("v", na=False)]["WORD"].dropna().unique()

# Display table
st.markdown("### Base and Regular Past Forms")

for word in verbs[:20]:  # Limit to first 20 to avoid overload
    base = word.strip().lower()
    past = to_past_tense(base)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"🔹 **{base}** → **{past}**")
    with col2:
        audio_base = generate_audio(base)
        audio_past = generate_audio(past)
        st.audio(audio_base, format="audio/mp3", start_time=0)
        st.audio(audio_past, format="audio/mp3", start_time=0)

