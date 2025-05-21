# 🔧 Required libraries
import streamlit as st
import pandas as pd
import random
from datetime import datetime
import pytz
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# 🏆 Certificate Generator
def generate_certificate(user_name, score, total, start_time, end_time):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    # Image paths (must be local)
    trophy_path = "https://github.com/MK316/Engpro-Class/raw/main/images/trophy.png"
    signature_path = "https://github.com/MK316/Engpro-Class/raw/main/images/signature2.png"

    try:
        c.drawImage(trophy_path, x=260, y=height - 150, width=80, height=100)
    except:
        c.setFont("Helvetica", 10)
        c.drawString(50, height - 150, "[Trophy image not found]")

    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height - 230, "Certificate of Completion")

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 280, "This certifies that")

    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width / 2, height - 310, user_name)

    c.setFont("Helvetica", 14)
    c.drawCentredString(width / 2, height - 340, "has completed the -ed Pronunciation Quiz")
    c.drawCentredString(width / 2, height - 370, f"with a score of {score} out of {total}.")

    c.setFont("Helvetica-Oblique", 12)
    c.drawCentredString(width / 2, height - 400, f"- Start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    c.drawCentredString(width / 2, height - 420, f"- End time: {end_time.strftime('%Y-%m-%d %H:%M:%S')}")

    c.setFont("Helvetica", 12)
    c.drawCentredString(width / 2, height - 460, "🎉 Congratulations on your achievement!")

    try:
        c.drawImage(signature_path, x=220, y=height - 700, width=200, height=180)
    except:
        c.drawString(50, height - 570, "[Signature image not found]")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

# 🧠 Load data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/ed-pronunciation-quiz.csv"
    df = pd.read_csv(url)
    return df

df = load_data()
df = df[df['ED'].isin(['t', 'd', 'ɪd'])]

if df.empty:
    st.error("⚠️ No valid words found.")
    st.stop()

# 🌐 Setup
display_map = {'t': '[t]', 'd': '[d]', 'ɪd': '[ɪd]'}
reverse_map = {v: k for k, v in display_map.items()}
seoul = pytz.timezone("Asia/Seoul")

# 🔄 Session state
st.session_state.setdefault("user_name", "")
st.session_state.setdefault("quiz_started", False)
st.session_state.setdefault("score", 0)
st.session_state.setdefault("trials", 0)
st.session_state.setdefault("answered", False)
st.session_state.setdefault("current_index", 0)
st.session_state.setdefault("word_list", [])
st.session_state.setdefault("start_time", None)
st.session_state.setdefault("end_time", None)

# 🧾 Title
st.title("🎯 -ed Pronunciation Quiz")
st.caption(f"📚 Total words available: {len(df)}")

# Step 1: Name input
if not st.session_state.user_name:
    with st.form("name_form"):
        name_input = st.text_input(
            label="Enter your name to begin in English:",
            placeholder="e.g., Gil-dong Kim"
        )
        submitted = st.form_submit_button("Submit")
        if submitted and name_input.strip():
            st.session_state.user_name = name_input.strip()
            st.rerun()
    st.stop()

# Step 2: Quiz setup
if not st.session_state.quiz_started:
    quiz_size = st.radio("How many words would you like to practice?", ["5", "All"], horizontal=True)
    if st.button("▶️ Start Quiz"):
        if quiz_size == "5":
            st.session_state.word_list = df.sample(5).to_dict(orient="records")
        else:
            st.session_state.word_list = df.to_dict(orient="records")

        st.session_state.quiz_started = True
        st.session_state.start_time = datetime.now(seoul)
        st.session_state.score = 0
        st.session_state.trials = 0
        st.session_state.current_index = 0
        st.session_state.answered = False
        st.rerun()
    st.stop()

# Step 3: Completion
total_questions = len(st.session_state.word_list)
if st.session_state.current_index >= total_questions:
    st.session_state.end_time = datetime.now(seoul)
    st.success("🎉 You've completed the quiz!")
    st.markdown(f"### ✅ Final Score: **{st.session_state.score} / {st.session_state.trials}**")

    cert = generate_certificate(
        user_name=st.session_state.user_name,
        score=st.session_state.score,
        total=st.session_state.trials,
        start_time=st.session_state.start_time,
        end_time=st.session_state.end_time
    )

    st.download_button(
        label="📄 Download Your Certificate",
        data=cert,
        file_name=f"{st.session_state.user_name}_certificate.pdf",
        mime="application/pdf"
    )

    if st.button("🔁 Restart Quiz"):
        for key in ["quiz_started", "score", "trials", "current_index", "user_name", "word_list", "answered", "start_time", "end_time"]:
            st.session_state[key] = "" if key == "user_name" else 0 if key in ["score", "trials", "current_index"] else [] if key == "word_list" else None if key in ["start_time", "end_time"] else False
        st.rerun()
    st.stop()

# Step 4: Quiz in progress
current = st.session_state.word_list[st.session_state.current_index]
word = current["WORD"]
correct_raw = current["ED"]
correct_display = display_map[correct_raw]

st.markdown(f"### Word {st.session_state.current_index + 1} of {total_questions}: **{word}**")

user_choice = st.radio(
    "Select the correct -ed pronunciation:",
    options=["[t]", "[d]", "[ɪd]"],
    horizontal=True,
    key=f"choice_{st.session_state.trials}"
)

col1, col2, spacer = st.columns([2, 2, 3])

if col1.button("✅ Check the Answer", key=f"check_{st.session_state.trials}"):
    user_raw = reverse_map[user_choice]
    st.session_state.trials += 1
    st.session_state.answered = True
    now = datetime.now(seoul).strftime("%Y-%m-%d %H:%M:%S")
    if user_raw == correct_raw:
        st.session_state.score += 1
        st.success(f"✅ Correct! ({now})")
    else:
        st.error(f"❌ Incorrect. The correct answer was **{correct_display}**. ({now})")

if st.session_state.answered:
    if col2.button("➡️ Next", key=f"next_{st.session_state.trials}"):
        st.session_state.current_index += 1
        st.session_state.answered = False
        st.rerun()

st.markdown(f"### 🧾 Score: {st.session_state.score} / {st.session_state.trials}")
