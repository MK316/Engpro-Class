import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/pages/cefr_250502.csv")

# Function to generate and return audio
def generate_audio(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Load data
df = load_data()

# Create tabs
tab1, tab2, tab3 = st.tabs(["🔤 Search by Word", "📘 By Vowels", "📗 By SID"])

# --- Tab 1: Flashcard App ---
with tab1:
    st.header("🔤 Search by word")
    st.caption("A total of 2,106 words from CEFR level B and level C")

    # User input
    user_input = st.text_input("Enter a word to look up:", "").strip().lower()

    if user_input:
        matched = df[df['WORD'].str.lower() == user_input]

        if not matched.empty:
            for _, row in matched.iterrows():
                with st.container():
                    st.markdown("---")
                    st.markdown(f"### 🌱 **{row['WORD']}**")
                    st.markdown(f"**🔵 Part of Speech:** {row['POS']}")
                    st.markdown(f"**🔵 Vowel Type:** {row['Vowel_Type']}")
                    st.markdown(f"**🔴 Stressed Vowel:** `{row['Stressed_Vowel']}`")

                    # Generate and play audio
                    audio = generate_audio(row['WORD'])
                    st.audio(audio, format='audio/mp3')
        else:
            st.warning("No matching word found.")

# --- Tab 2 Placeholder ---
with tab2:
    st.header("📘 App 2")
    st.write("You can implement a different app here.")

# --- Tab 3 Placeholder ---
with tab3:
    st.header("📗 App 3")
    st.write("You can implement another app here.")
