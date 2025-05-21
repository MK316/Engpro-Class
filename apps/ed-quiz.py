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
df = df[df['ED'].isin(['t', 'd', 'ɪd'])]

if df.empty:
    st.error("⚠️ No valid words with t, d, or ɪd in the dataset.")
    st.stop()

# Display maps for friendly labels
display_map = {'t': '[t]', 'd': '[d]', 'ɪd': '[ɪd]'}
reverse_map = {v: k for k, v in display_map.items()}

# Initialize session state
st.session_state.setdefault("user_name", "")
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("score", 0)
st.session_state.setdefault("trials", 0)
st.session_state.setdefault("answered", False)
st.session_state.setdefault("current_index", 0)
st.session_state.setdefault("word_list", [])

# Title
st.title("🎯 -ed Pronunciation Quiz")
st.caption(f"A total number of questions in dataset: {len(df)}")

# 1. Name input
if not st.session_state.user_name:
    with st.form("name_form"):
        name_input = st.text_input("Enter your name to begin:")
        submitted = st.form_submit_button("Submit")
        if submitted and name_input.strip():
            st.session_state.user_name = name_input.strip()
            st.rerun()
    st.stop()

# 2. Mode selection (5 or all)
if not st.session_state.quiz_started:
    quiz_size = st.radio("How many words would you like to practice?", ["5", "All"], horizontal=True)

    if st.button("▶️ Start Quiz"):
        if quiz_size == "5":
            st.session_state.word_list = df.sample(5).to_dict(orient="records")
        else:
            st.session_state.word_list = df.to_dict(orient="records")

        st.session_state.quiz_started = True
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.trials = 0
        st.session_state.answered = False
        st.rerun()
    st.stop()

# 3. Quiz logic
total_questions = len(st.session_state.word_list)
if st.session_state.current_index >= total_questions:
    st.success("🎉 You've completed the quiz!")
    st.markdown(f"### Final Score: **{st.session_state.score} / {st.session_state.trials}**")
    if st.button("🔁 Restart Quiz"):
        for key in ["quiz_started", "score", "trials", "current_index", "user_name", "word_list", "answered"]:
            st.session_state[key] = "" if key == "user_name" else 0 if key in ["score", "trials", "current_index"] else [] if key == "word_list" else False
        st.rerun()
    st.stop()

# Get current word
current_word_data = st.session_state.word_list[st.session_state.current_index]
word = current_word_data["WORD"]
correct_raw = current_word_data["ED"]
correct_display = display_map[correct_raw]

st.markdown(f"### Word {st.session_state.current_index + 1} of {total_questions}: **{word}**")

# User selection
user_choice = st.radio(
    "Select the correct -ed pronunciation:",
    options=["[t]", "[d]", "[ɪd]"],
    horizontal=True,
    key=f"choice_{st.session_state.trials}"
)

# Button row
col1, col2 = st.columns([1, 1])

if col1.button("✅ Check the Answer", key=f"check_{st.session_state.trials}"):
    st.session_state.trials += 1
    st.session_state.answered = True

    user_raw = reverse_map[user_choice]
    seoul_time = datetime.now(pytz.timezone("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S")

    if user_raw == correct_raw:
        st.session_state.score += 1
        st.success(f"✅ Correct! ({seoul_time})")
    else:
        st.error(f"❌ Incorrect. The correct answer was **{correct_display}**. ({seoul_time})")

# Show "Next" only after answer is checked
if st.session_state.answered:
    if col2.button("➡️ Next", key=f"next_{st.session_state.trials}"):
        st.session_state.current_index += 1
        st.session_state.answered = False
        st.rerun()

# Show score during quiz
st.markdown(f"### 🧾 Score: {st.session_state.score} / {st.session_state.trials}")
