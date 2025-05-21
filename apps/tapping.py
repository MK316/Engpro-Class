import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO

# --- Load data from GitHub ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/data/tapping_dataB.csv"
    df = pd.read_csv(url, encoding="utf-8-sig")
    return df

df = load_data()

# --- Initialize session state ---
if "selected_target" not in st.session_state:
    st.session_state.selected_target = None
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "user_response" not in st.session_state:
    st.session_state.user_response = None
if "show_word" not in st.session_state:
    st.session_state.show_word = False
if "show_feedback" not in st.session_state:
    st.session_state.show_feedback = False

# --- Function to move to next word ---
def go_next():
    if st.session_state.current_index + 1 < len(st.session_state.target_df):
        st.session_state.current_index += 1
    else:
        st.session_state.current_index = 0
    st.session_state.show_word = True
    st.session_state.show_feedback = False
    st.session_state.user_response = None

# --- App Title ---
st.title("🔁 Tapping Practice App")

# --- Target selection buttons ---
st.markdown("### Step 1: Choose your target sound")
col1, col2 = st.columns(2)
with col1:
    if st.button("🔵 T"):
        st.session_state.selected_target = "T"
        st.session_state.current_index = 0
        st.session_state.show_word = False
        st.session_state.show_feedback = False
with col2:
    if st.button("🔴 D"):
        st.session_state.selected_target = "D"
        st.session_state.current_index = 0
        st.session_state.show_word = False
        st.session_state.show_feedback = False

# --- Filter based on selected target ---
if st.session_state.selected_target:
    st.session_state.target_df = df[df["Target"] == st.session_state.selected_target].reset_index(drop=True)
    total_words = len(st.session_state.target_df)
    st.markdown(f"### 📌 There are **{total_words}** words to practice.")

    if st.button("🎯 Show a word"):
        st.session_state.show_word = True
        st.session_state.show_feedback = False
        st.session_state.user_response = None

    if st.session_state.show_word and st.session_state.current_index < total_words:
        current_word = st.session_state.target_df.loc[st.session_state.current_index, "WORD"]
        tapping_truth = st.session_state.target_df.loc[st.session_state.current_index, "Tapping"]
        target_letter = st.session_state.selected_target

        # --- Highlight target sound ---
        def highlight_letter(word, target):
            index = word.lower().find(target.lower())
            if index == -1:
                return word
            return (
                word[:index] +
                f"<span style='color:red; font-weight:bold;'>{word[index]}</span>" +
                word[index + 1:]
            )

        highlighted_word = highlight_letter(current_word, target_letter)
        st.markdown(f"<h1 style='font-size: 64px; text-align: center;'>{highlighted_word}</h1>", unsafe_allow_html=True)

        # --- Audio generation ---
        try:
            tts = gTTS(current_word)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format="audio/mp3")
        except Exception as e:
            st.error("⚠️ Failed to generate audio.")
            st.exception(e)

        # --- Tapping question ---
        st.markdown("**Is tapping possible?**")
        st.session_state.user_response = st.radio(
            "Choose one:", ["YES", "NO", "YES/NO", "NO/YES"], index=0,
            key=f"radio_{st.session_state.current_index}"
        )

        # --- Feedback ---
        if st.button("✅ Show Feedback"):
            st.session_state.show_feedback = True

        if st.session_state.show_feedback:
            expected = "YES" if tapping_truth.strip().upper() == "YES" else "NO"
            if expected in st.session_state.user_response:
                st.success("🎉 Correct!")
            else:
                st.error("❗ Try again.")

        # --- Next word button (immediate click response)
        st.button("➡️ Next Word", on_click=go_next)
