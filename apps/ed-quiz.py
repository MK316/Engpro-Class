import streamlit as st
import pandas as pd
import random

# Load data from GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/ed-pronunciation-quiz.csv"
    df = pd.read_csv(url)
    return df

# Load dataset
df = load_data()
df = df[df['ED'].isin(['[t]', '[d]', '[ɪd]'])]  # Filter only valid rows

# ✅ Check for empty data
if df.empty:
    st.error("⚠️ No valid entries with [t], [d], or [ɪd] found in the dataset.")
    st.stop()

# Initialize session state
st.session_state.setdefault("user_name", "")
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("score", 0)
st.session_state.setdefault("trials", 0)
st.session_state.setdefault("current_word", None)
st.session_state.setdefault("user_answer", None)
st.session_state.setdefault("feedback", "")

# App title
st.title("🎯 -ed Pronunciation Quiz")

# ✅ Name input form
if not st.session_state.get("user_name"):
    with st.form("name_form"):
        name_input = st.text_input("Enter your name to begin:")
        submitted = st.form_submit_button("Submit")
        if submitted and name_input.strip():
            st.session_state.user_name = name_input.strip()
            st.rerun()
    st.stop()

# ✅ Start button logic
if not st.session_state.quiz_started:
    if st.button("▶️ Start Quiz"):
        st.session_state.quiz_started = True
        st.session_state.current_word = df.sample(1).iloc[0]
    st.stop()

# ✅ Show the current quiz word
if st.session_state.current_word is not None:
    word = st.session_state.current_word["WORD"]
    correct_answer = st.session_state.current_word["ED"]

    st.markdown(f"### Word: **{word}**")
    st.session_state.user_answer = st.radio(
        "Select the correct -ed ending pronunciation:",
        options=["[t]", "[d]", "[ɪd]"],
        horizontal=True,
        key=f"choice_{st.session_state.trials}"
    )

    if st.button("✅ Check the Answer"):
        st.session_state.trials += 1
        if st.session_state.user_answer == correct_answer:
            st.session_state.score += 1
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect. The correct answer was **{correct_answer}**.")

        # ✅ Get the next word safely
        if not df.empty:
            st.session_state.current_word = df.sample(1).iloc[0]
        else:
            st.session_state.current_word = None
            st.warning("No more words available.")

    # Score display
    st.markdown(f"### 🧾 Score: {st.session_state.score} / {st.session_state.trials}")

# ✅ Restart quiz
if st.button("🔁 Restart Quiz"):
    st.session_state.quiz_started = False
    st.session_state.score = 0
    st.session_state.trials = 0
    st.session_state.current_word = None
    st.session_state.user_answer = None
    st.session_state.user_name = ""
    st.rerun()
