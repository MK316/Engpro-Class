import random
from datetime import datetime
from io import BytesIO

import pandas as pd
import requests
import streamlit as st
from gtts import gTTS

# PDF (ReportLab)
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


# =========================
# Page setup
# =========================
st.set_page_config(page_title="CEFR Vowel App + Quiz", layout="wide")


# =========================
# Data loading (robust)
# =========================
CSV_URL = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/pages/cefr_20260208a.csv"

@st.cache_data(show_spinner=False)
def load_data(csv_url: str) -> pd.DataFrame:
    # Use requests first (more transparent errors on Streamlit Cloud), then read_csv from text
    r = requests.get(csv_url, timeout=20)
    r.raise_for_status()
    data = r.content.decode("utf-8", errors="replace")
    df = pd.read_csv(BytesIO(data.encode("utf-8")))
    return df

def generate_audio(text: str, lang: str = "en") -> BytesIO:
    tts = gTTS(text=text, lang=lang)
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp


# =========================
# Quiz helpers
# =========================
def build_one_question(df: pd.DataFrame) -> dict:
    """
    Odd-one-out: 4 words share vowel1, 1 word has different vowel2.
    Returns dict: {options: [..5..], correct: str, meta: {...}}
    """
    vowels = df["Stressed_Vowel"].dropna().unique().tolist()
    if len(vowels) < 2:
        raise ValueError("Not enough vowel categories in the dataset.")

    vowel1 = random.choice(vowels)

    group1 = (
        df[df["Stressed_Vowel"].astype(str).str.strip() == str(vowel1).strip()]["WORD"]
        .dropna()
        .astype(str)
        .unique()
        .tolist()
    )
    if len(group1) < 4:
        # try a few times to find a vowel with enough words
        for _ in range(20):
            vowel1 = random.choice(vowels)
            group1 = (
                df[df["Stressed_Vowel"].astype(str).str.strip() == str(vowel1).strip()]["WORD"]
                .dropna()
                .astype(str)
                .unique()
                .tolist()
            )
            if len(group1) >= 4:
                break
        if len(group1) < 4:
            raise ValueError("Not enough words to form quiz items (need 4+ for a vowel).")

    same_vowel_words = random.sample(group1, 4)

    different_vowels = [v for v in vowels if str(v).strip() != str(vowel1).strip()]
    random.shuffle(different_vowels)

    odd_word = None
    odd_vowel = None
    for v2 in different_vowels:
        group2 = (
            df[df["Stressed_Vowel"].astype(str).str.strip() == str(v2).strip()]["WORD"]
            .dropna()
            .astype(str)
            .unique()
            .tolist()
        )
        if group2:
            odd_word = random.choice(group2)
            odd_vowel = v2
            break

    if odd_word is None:
        raise ValueError("Could not find an odd-one-out word.")

    combined = [(w, vowel1) for w in same_vowel_words] + [(odd_word, odd_vowel)]
    random.shuffle(combined)
    options = [w for w, _ in combined]

    return {
        "options": options,
        "correct": odd_word,
        "vowel_same": str(vowel1),
        "vowel_odd": str(odd_vowel),
    }

def init_quiz_state():
    defaults = {
        "quiz_active": False,
        "quiz_user": "",
        "quiz_n": 5,
        "quiz_start_time": None,
        "quiz_end_time": None,
        "quiz_items": [],          # list of question dicts
        "quiz_index": 0,           # current question index
        "quiz_selected": None,     # current selection
        "quiz_score": 0,
        "quiz_total_trials": 0,
        "quiz_item_trials": {},    # {idx: trials}
        "quiz_wrong_items": [],    # list of dicts: {idx, correct, chosen, options, trials}
        "quiz_submitted": False,   # whether current item has been submitted
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def start_quiz(df: pd.DataFrame):
    name = st.session_state.get("quiz_user_input", "").strip()
    n = int(st.session_state.get("quiz_n_input", 5))

    if not name:
        st.session_state["quiz_active"] = False
        st.session_state["quiz_error"] = "Please type your name in English."
        return
    if n < 1:
        st.session_state["quiz_active"] = False
        st.session_state["quiz_error"] = "Number of items must be at least 1."
        return

    items = []
    # Build n questions (robust retries)
    tries = 0
    while len(items) < n and tries < n * 10:
        tries += 1
        try:
            items.append(build_one_question(df))
        except Exception:
            continue

    if len(items) < n:
        st.session_state["quiz_active"] = False
        st.session_state["quiz_error"] = "Could not generate enough quiz items from the dataset."
        return

    # Reset session quiz state
    st.session_state["quiz_active"] = True
    st.session_state["quiz_error"] = ""
    st.session_state["quiz_user"] = name
    st.session_state["quiz_n"] = n
    st.session_state["quiz_start_time"] = datetime.now()
    st.session_state["quiz_end_time"] = None
    st.session_state["quiz_items"] = items
    st.session_state["quiz_index"] = 0
    st.session_state["quiz_selected"] = None
    st.session_state["quiz_score"] = 0
    st.session_state["quiz_total_trials"] = 0
    st.session_state["quiz_item_trials"] = {}
    st.session_state["quiz_wrong_items"] = []
    st.session_state["quiz_submitted"] = False

def submit_answer():
    idx = st.session_state["quiz_index"]
    items = st.session_state["quiz_items"]
    if not items:
        return

    chosen = st.session_state.get("quiz_choice_radio", None)
    if chosen is None:
        st.session_state["quiz_feedback"] = ("warning", "Please choose an answer first.")
        return

    # One-click protection
    if st.session_state.get("quiz_submitted", False):
        return

    st.session_state["quiz_submitted"] = True

    st.session_state["quiz_total_trials"] += 1
    st.session_state["quiz_item_trials"][idx] = st.session_state["quiz_item_trials"].get(idx, 0) + 1

    correct = items[idx]["correct"]
    if chosen == correct:
        st.session_state["quiz_score"] += 1
        st.session_state["quiz_feedback"] = ("success", f"Correct! ✅  The odd word is: {correct}")
    else:
        st.session_state["quiz_feedback"] = ("error", f"Incorrect. ❌  The correct answer is: {correct}")
        st.session_state["quiz_wrong_items"].append(
            {
                "idx": idx + 1,
                "correct": correct,
                "chosen": chosen,
                "options": items[idx]["options"],
                "trials_for_item": st.session_state["quiz_item_trials"][idx],
            }
        )

def next_item():
    items = st.session_state["quiz_items"]
    idx = st.session_state["quiz_index"]

    # Must submit before moving on
    if not st.session_state.get("quiz_submitted", False):
        st.session_state["quiz_feedback"] = ("warning", "Please submit your answer before going to the next item.")
        return

    if idx + 1 < len(items):
        st.session_state["quiz_index"] += 1
        st.session_state["quiz_choice_radio"] = None
        st.session_state["quiz_submitted"] = False
        st.session_state["quiz_feedback"] = None
    else:
        # finish
        st.session_state["quiz_end_time"] = datetime.now()
        st.session_state["quiz_feedback"] = ("info", "Quiz completed. You can generate your PDF report below.")

def reset_quiz():
    # Keep input widgets, reset only quiz run
    st.session_state["quiz_active"] = False
    st.session_state["quiz_items"] = []
    st.session_state["quiz_index"] = 0
    st.session_state["quiz_selected"] = None
    st.session_state["quiz_score"] = 0
    st.session_state["quiz_total_trials"] = 0
    st.session_state["quiz_item_trials"] = {}
    st.session_state["quiz_wrong_items"] = []
    st.session_state["quiz_start_time"] = None
    st.session_state["quiz_end_time"] = None
    st.session_state["quiz_submitted"] = False
    st.session_state["quiz_feedback"] = None
    st.session_state["quiz_error"] = ""

def build_pdf_report() -> BytesIO:
    """
    PDF includes: username, start/end time, final score, total trials,
    and list of incorrectly answered items.
    """
    user = st.session_state.get("quiz_user", "")
    start_t = st.session_state.get("quiz_start_time")
    end_t = st.session_state.get("quiz_end_time") or datetime.now()
    score = st.session_state.get("quiz_score", 0)
    n = st.session_state.get("quiz_n", 0)
    total_trials = st.session_state.get("quiz_total_trials", 0)
    wrong_items = st.session_state.get("quiz_wrong_items", [])

    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4

    y = height - 20 * mm
    c.setFont("Helvetica-Bold", 16)
    c.drawString(20 * mm, y, "Quiz Report")
    y -= 10 * mm

    c.setFont("Helvetica", 11)
    c.drawString(20 * mm, y, f"Name: {user}")
    y -= 7 * mm
    c.drawString(20 * mm, y, f"Start time: {start_t.strftime('%Y-%m-%d %H:%M:%S') if start_t else '-'}")
    y -= 7 * mm
    c.drawString(20 * mm, y, f"End time: {end_t.strftime('%Y-%m-%d %H:%M:%S')}")
    y -= 10 * mm

    c.setFont("Helvetica-Bold", 12)
    c.drawString(20 * mm, y, f"Final score: {score} / {n}")
    y -= 7 * mm
    c.setFont("Helvetica", 11)
    c.drawString(20 * mm, y, f"Total trials (Submit clicks): {total_trials}")
    y -= 12 * mm

    c.setFont("Helvetica-Bold", 12)
    c.drawString(20 * mm, y, "Incorrect items")
    y -= 8 * mm

    c.setFont("Helvetica", 10)
    if not wrong_items:
        c.drawString(20 * mm, y, "None (Perfect score).")
        y -= 6 * mm
    else:
        for w in wrong_items:
            line1 = f"Item {w['idx']}: chosen '{w['chosen']}'  | correct '{w['correct']}'  | trials {w['trials_for_item']}"
            c.drawString(20 * mm, y, line1[:110])
            y -= 6 * mm
            opts = ", ".join(w["options"])
            c.drawString(25 * mm, y, ("Options: " + opts)[:115])
            y -= 8 * mm

            if y < 25 * mm:
                c.showPage()
                y = height - 20 * mm
                c.setFont("Helvetica", 10)

    c.showPage()
    c.save()
    buf.seek(0)
    return buf


# =========================
# App start
# =========================
init_quiz_state()

try:
    df = load_data(CSV_URL)
except Exception as e:
    st.error(f"Failed to load the dataset. ({type(e).__name__}) {e}")
    st.stop()


tab1, tab2, tab3, tab4 = st.tabs(["🔤 Search by Word", "📘 Monophthongs", "📗 Diphthongs", "🌈 Quiz"])


# -------------------------
# Tab 1
# -------------------------
with tab1:
    st.header("🔤 Search by word")
    st.caption("A total of 2,106 words from CEFR level B and level C")
    user_input = st.text_input("Enter a word to look up:", "").strip().lower()

    if user_input:
        matched = df[df["WORD"].astype(str).str.lower() == user_input]
        if not matched.empty:
            for _, row in matched.iterrows():
                st.markdown("---")
                st.markdown(f"### 🌱 {row['WORD']}")
                st.write(f"Part of Speech: {row['POS']}")
                st.write(f"Vowel Type: {row['Vowel_Type']}")
                st.write(f"Stressed Vowel: {row['Stressed_Vowel']}")

                audio = generate_audio(str(row["WORD"]))
                st.audio(audio, format="audio/mp3")
        else:
            st.warning("No matching word found.")


# -------------------------
# Tab 2
# -------------------------
with tab2:
    st.markdown("### 📘 Browse Words by Vowels (Monophthongs)")
    st.caption("The following contains monophthong vowels.")

    monophthongs = ["Choose a vowel", "/ i /", "/ ɪ /", "/ u /", "/ ʊ /", "/ ɛ /", "/ æ /", "/ ʌ /", "/ ɔ /", "/ ɑ /", "/ ɝ /"]
    if "page_start_mono" not in st.session_state:
        st.session_state.page_start_mono = 0
    if "prev_vowel_mono" not in st.session_state:
        st.session_state.prev_vowel_mono = ""
    if "prev_count_mono" not in st.session_state:
        st.session_state.prev_count_mono = 5

    selected_vowel = st.selectbox("Choose a monophthong vowel:", monophthongs, key="mono_vowel")
    num_display = st.radio("How many words to display?", [5, 10, 20], horizontal=True, key="mono_n")

    if selected_vowel != st.session_state.prev_vowel_mono or num_display != st.session_state.prev_count_mono:
        st.session_state.page_start_mono = 0
        st.session_state.prev_vowel_mono = selected_vowel
        st.session_state.prev_count_mono = num_display

    filtered_df = df[
        (df["Stressed_Vowel"].astype(str).str.strip() == str(selected_vowel).strip())
        & (df["Vowel_Type"].astype(str) == "Monophthong")
    ]
    total_matches = len(filtered_df)
    st.info(f"Found {total_matches} words with stressed vowel {selected_vowel}.")

    start = st.session_state.page_start_mono
    end = start + num_display
    to_display = filtered_df.iloc[start:end]

    if not to_display.empty:
        for _, row in to_display.iterrows():
            st.markdown("---")
            st.markdown(f"### 🌼 {row['WORD']}")
            st.write(f"Part of Speech: {row['POS']}")
            st.write(f"Stressed Vowel: {row['Stressed_Vowel']}")
            st.audio(generate_audio(str(row["WORD"])), format="audio/mp3")

        if end < total_matches:
            if st.button("Next", key="mono_next"):
                st.session_state.page_start_mono += num_display
    else:
        st.warning("No matching words found (or end of list).")


# -------------------------
# Tab 3
# -------------------------
with tab3:
    st.markdown("### 📗 Browse Words by Vowels (Diphthongs)")
    st.caption("The following contains diphthong vowels.")

    diphthongs = ["Choose a vowel", "/ aɪ /", "/ oʊ /", "/ eɪ /", "/ aʊ /", "/ ɔɪ /"]
    if "page_start_diph" not in st.session_state:
        st.session_state.page_start_diph = 0
    if "prev_vowel_diph" not in st.session_state:
        st.session_state.prev_vowel_diph = ""
    if "prev_count_diph" not in st.session_state:
        st.session_state.prev_count_diph = 5

    selected_vowel = st.selectbox("Choose a diphthong vowel:", diphthongs, key="diph_vowel")
    num_display = st.radio("How many words to display?", [5, 10, 20], horizontal=True, key="diph_n")

    if selected_vowel != st.session_state.prev_vowel_diph or num_display != st.session_state.prev_count_diph:
        st.session_state.page_start_diph = 0
        st.session_state.prev_vowel_diph = selected_vowel
        st.session_state.prev_count_diph = num_display

    filtered_df = df[
        (df["Stressed_Vowel"].astype(str).str.strip() == str(selected_vowel).strip())
        & (df["Vowel_Type"].astype(str) == "Diphthong")
    ]
    total_matches = len(filtered_df)
    st.info(f"Found {total_matches} words with stressed vowel {selected_vowel}.")

    start = st.session_state.page_start_diph
    end = start + num_display
    to_display = filtered_df.iloc[start:end]

    if not to_display.empty:
        for _, row in to_display.iterrows():
            st.markdown("---")
            st.markdown(f"### 🌼 {row['WORD']}")
            st.write(f"Part of Speech: {row['POS']}")
            st.write(f"Stressed Vowel: {row['Stressed_Vowel']}")
            st.audio(generate_audio(str(row["WORD"])), format="audio/mp3")

        if end < total_matches:
            if st.button("Next", key="diph_next"):
                st.session_state.page_start_diph += num_display
    else:
        st.warning("No matching words found (or end of list).")


# -------------------------
# Tab 4 (NEW QUIZ FLOW)
# -------------------------
with tab4:
    st.header("🌈 Quiz (Odd-one-out)")
    st.caption("Before you start, type your name, choose the number of items, and click Start. "
               "At the end, you can download a PDF report.")

    # Setup area
    left, right = st.columns([1, 1])
    with left:
        st.text_input("Your name (English):", key="quiz_user_input", placeholder="e.g., Mina Kim")
    with right:
        st.number_input("How many items do you want in this quiz?", min_value=1, max_value=50, value=10, step=1, key="quiz_n_input")

    c1, c2 = st.columns([1, 1])
    with c1:
        st.button("✅ Start", on_click=start_quiz, args=(df,), use_container_width=True)
    with c2:
        st.button("↩️ Reset", on_click=reset_quiz, use_container_width=True)

    if st.session_state.get("quiz_error"):
        st.error(st.session_state["quiz_error"])

    st.markdown("---")

    # Active quiz
    if st.session_state["quiz_active"] and st.session_state["quiz_items"]:
        items = st.session_state["quiz_items"]
        idx = st.session_state["quiz_index"]
        n = len(items)

        # Progress (bottom later too, but show here for clarity)
        progress = (idx) / n
        st.progress(progress)

        st.subheader(f"Item {idx+1} of {n}")
        st.write("Choose the word that has a different stressed vowel than the others.")

        q = items[idx]
        choice = st.radio(
            "Select one:",
            q["options"],
            index=None,
            key="quiz_choice_radio"
        )

        # Feedback
        fb = st.session_state.get("quiz_feedback", None)
        if fb:
            kind, msg = fb
            if kind == "success":
                st.success(msg)
            elif kind == "error":
                st.error(msg)
            elif kind == "warning":
                st.warning(msg)
            else:
                st.info(msg)

        # Controls (one-click via callbacks)
        b1, b2 = st.columns([1, 1])
        with b1:
            st.button("Submit", on_click=submit_answer, use_container_width=True)
        with b2:
            label = "Next" if (idx + 1 < n) else "Finish"
            st.button(label, on_click=next_item, use_container_width=True)

        # Score summary
        st.markdown("---")
        st.write(f"**Score:** {st.session_state['quiz_score']} / {n}")
        st.write(f"**Total trials (Submit clicks):** {st.session_state['quiz_total_trials']}")

        # Bottom progress bar (as requested)
        st.progress((idx + (1 if st.session_state.get("quiz_submitted") else 0)) / n)

        # PDF button appears only after last item is finished
        if st.session_state.get("quiz_end_time") is not None:
            st.markdown("---")
            st.subheader("📄 Final report")
            st.caption("Click the button below to download your PDF report (name, timestamps, incorrect items, score, and trials).")

            pdf_bytes = build_pdf_report()
            st.download_button(
                "Generate PDF report",
                data=pdf_bytes,
                file_name=f"quiz_report_{st.session_state['quiz_user'].replace(' ', '_')}.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
    else:
        st.info("Set your name and number of items, then click **Start** to begin.")
