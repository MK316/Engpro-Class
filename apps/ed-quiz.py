import streamlit as st
import pandas as pd
import random
from datetime import datetime
import pytz

# Load data from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/ed-pronunciation-quiz.csv"
    df = pd.read_csv(url)
    return df

# Load and filter valid entries
df = load_data()
df = df[df['ED'].isin(['t', 'd', 'ɪd'])]  # Match your data exactly

if df.empty:
    st.error("⚠️ No valid words with t, d, or ɪd in the dataset.")
    st.stop()

# Display map for better UI (what user sees vs. what we compare)
display_map = {'t': '[t]', 'd': '[d]', 'ɪd': '[ɪd]'}
reverse_map = {v: k for k, v in display_map.items()}  # for checking answers

# Initialize session state
st.session_state.setdefault("user_name", "")
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("score", 0)
st.session_state.setdefault("trials", 0)
st.session_state.setdefault("current_word", None)
st.session_state.setdefault("user_answer", None)
st.session_state.setdefault("feedback", "")
st.session_state.setdefault("answered", False)

# Title
st.title("🎯 -ed Pronunciation Quiz")
st.caption("A total number of questions: 103")

# Name input
if not st.session_state.user_name:
    with st.form("name_form"):
        name_input = st.text_input("Enter your name to begin:")
        submitted = st.form_submit_button("Submit")
        if submitted and name_input.strip():
            st.session_state.user_name = name_input.strip()
            st.rerun()
    st.stop()

# Start button
if not st.session_state.quiz_started:
    if st.button("▶️ Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.current_word = df.sample(1).iloc[0]
    st.stop()

# Show quiz word and options
if st.session_state.current_word is not None:
    word = st.session_state.current_word["WORD"]
    correct_raw = st.session_state.current_word["ED"]
    correct_display = display_map[correct_raw]

    st.markdown(f"### Word: **{word}**")

    st.session_state.user_answer = st.radio(
        "Select the correct -ed pronunciation:",
        options=["[t]", "[d]", "[ɪd]"],
        horizontal=True,
        key=f"choice_{st.session_state.trials}"
    )

    # Show Check and Next buttons in same row
    col1, col2 = st.columns([1, 1])
    if col1.button("✅ Check the Answer", key=f"check_{st.session_state.trials}"):
        user_raw_answer = reverse_map[st.session_state.user_answer]
        st.session_state.trials += 1
        st.session_state.answered = True

        # Get current Seoul time
        seoul_time = datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S")

        # Feedback
        if user_raw_answer == correct_raw:
            st.session_state.score += 1
            st.success(f"✅ Correct! ({seoul_time})")
        else:
            st.error(f"❌ Incorrect. The correct answer was **{correct_display}**. ({seoul_time})")

    # Show Next only after checking
    if st.session_state.answered:
        if col2.button("➡️ Next", key=f"next_{st.session_state.trials}"):
            st.session_state.current_word = df.sample(1).iloc[0]
            st.session_state.answered = False
            st.rerun()

    # Score display
    st.markdown(f"### 🧾 Score: {st.session_state.score} / {st.session_state.trials}")

# Restart
if st.button("🔁 Restart Quiz"):
    for key in ["quiz_started", "score", "trials", "current_word", "user_answer", "user_name", "answered"]:
        st.session_state[key] = "" if key == "user_name" else 0 if key in ["score", "trials"] else None if key == "current_word" else False
    st.rerun()
