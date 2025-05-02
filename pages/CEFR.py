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
tab1, tab2, tab3 = st.tabs(["🔤 Search by Word", "📘 Monophthongs", "📗 Diphthongs"])

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


# --- Tab 2: Browse by Monophthong Vowel ---
with tab2:
    st.markdown("### 📘 Browse Words by Vowels (Monophthongs)")
    st.caption("🚩 The following contains all monophthong vowels.")

    # Monophthong vowel list
    monophthongs = ["/ i /", "/ ɪ /", "/ u /", "/ ʊ /", "/ ɛ /", "/ æ /", "/ ʌ /", "/ ɔ /", "/ ɑ /", "/ ɝ /"]


    # Initialize session state for pagination
    if "page_start" not in st.session_state:
        st.session_state.page_start = 0
    if "prev_vowel" not in st.session_state:
        st.session_state.prev_vowel = ""
    if "prev_count" not in st.session_state:
        st.session_state.prev_count = 5

    # UI: Dropdown + Radio
    selected_vowel = st.selectbox("Choose a monophthong vowel:", monophthongs)
    num_display = st.radio("How many words would you like to display?", [5, 10, 20], horizontal=True)

    # Reset pagination if vowel or count changed
    if selected_vowel != st.session_state.prev_vowel or num_display != st.session_state.prev_count:
        st.session_state.page_start = 0
        st.session_state.prev_vowel = selected_vowel
        st.session_state.prev_count = num_display

    # Filter dataset
    filtered_df = df[(df["Stressed_Vowel"].str.strip() == selected_vowel) & (df["Vowel_Type"] == "Monophthong")]
    total_matches = len(filtered_df)
    st.info(f"🔍 Found **{total_matches}** words with stressed vowel **{selected_vowel}**.")

    # Get page slice
    start = st.session_state.page_start
    end = start + num_display
    to_display = filtered_df.iloc[start:end]

    if not to_display.empty:
        for _, row in to_display.iterrows():
            with st.container():
                st.markdown("---")
                st.markdown(f"### 🌼 **{row['WORD']}**")
                st.markdown(f"**Part of Speech:** {row['POS']}")
                st.markdown(f"**Stressed Vowel:** `{row['Stressed_Vowel']}`")
                audio = generate_audio(row['WORD'])
                st.audio(audio, format='audio/mp3')

        # Only show "Next" if more results remain
        if end < total_matches:
            if st.button("Next"):
                st.session_state.page_start += num_display
    else:
        st.warning("No matching words found or end of list reached.")

# --- Tab 3 Placeholder ---
with tab3:
    st.header("📗 App 3")
    st.write("You can implement another app here.")
