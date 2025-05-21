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
df = df[df['ED'].isin(['[t]', '[d]', '[ɪd]'])]  # Only rows with valid ED values

# Initialize session state
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "score" not in st.session_state:
    st.session_state.score = 0
if "trials" not in st.session_state:
    st.session_state.trials = 0
if "current_word" not in st.session_state:
    st.session_state.current_word = None
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""

# App title
st.title("🎯 -ed Pronunciation Quiz")

# Get user name
# Get user name (proper flow)
if not st.session_state.get("user_name"):
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

# Show word and options
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

        st.session_state.current_word = df.sample(1).iloc[0]

    # Score display
    st.markdown(f"### 🧾 Score: {st.session_state.score} / {st.session_state.trials}")

# Restart button
if st.button("🔁 Restart Quiz"):
    st.session_state.quiz_started = False
    st.session_state.score = 0
    st.session_state.trials = 0
    st.session_state.current_word = None
    st.session_state.user_answer = None
    st.rerun()
