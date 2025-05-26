import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv("https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/pages/cefr_20260505a.csv")

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
tab1, tab2, tab3, tab4 = st.tabs(["🔤 Search by Word", "📘 Monophthongs", "📗 Diphthongs", "🌈 Quiz"])

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
    st.caption("🚩 The following contains all monophthong vowels. (A total of 1,644 words)")

    # Monophthong vowel list
    monophthongs = ["Choose a vowel", "/ i /", "/ ɪ /", "/ u /", "/ ʊ /", "/ ɛ /", "/ æ /", "/ ʌ /", "/ ɔ /", "/ ɑ /", "/ ɝ /"]


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

# --- Tab 3: Browse by Diphthong Vowel ---
with tab3:
    st.markdown("### 📗 Browse Words by Vowels (Diphthongs)")
    st.caption("🚩 The following contains all diphthong vowels. (A total of 462 words)")

    # Diphthong vowel list
    diphthongs = ["Choose a vowel", "/ aɪ /", "/ oʊ /", "/ eɪ /", "/ aʊ /", "/ ɔɪ /"]

    # Initialize session state for pagination
    if "page_start_diph" not in st.session_state:
        st.session_state.page_start_diph = 0
    if "prev_vowel_diph" not in st.session_state:
        st.session_state.prev_vowel_diph = ""
    if "prev_count_diph" not in st.session_state:
        st.session_state.prev_count_diph = 5

    # UI: Dropdown + Radio with unique keys
    selected_vowel = st.selectbox("Choose a diphthong vowel:", diphthongs, key="diphthong_dropdown")
    num_display = st.radio("How many words would you like to display?", [5, 10, 20], horizontal=True, key="diphthong_display_count")

    # Reset pagination if vowel or count changed
    if selected_vowel != st.session_state.prev_vowel_diph or num_display != st.session_state.prev_count_diph:
        st.session_state.page_start_diph = 0
        st.session_state.prev_vowel_diph = selected_vowel
        st.session_state.prev_count_diph = num_display

    # Filter dataset for diphthongs
    filtered_df = df[(df["Stressed_Vowel"].str.strip() == selected_vowel) & (df["Vowel_Type"] == "Diphthong")]
    total_matches = len(filtered_df)
    st.info(f"🔍 Found **{total_matches}** words with stressed vowel **{selected_vowel}**.")

    # Get page slice
    start = st.session_state.page_start_diph
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
            if st.button("Next", key="diphthong_next"):
                st.session_state.page_start_diph += num_display
    else:
        st.warning("No matching words found or end of list reached.")



# --- Tab 4: Minimal Vowel Quiz ---




with tab4:
    st.markdown("### 🍀 Vowel Odd-One-Out Quiz")
    st.caption("Q: Choose the word that has a different stressed vowel than the others.")

    # Initialize session states for quiz logic
    for key in ["quiz_words", "correct_answer", "quiz_choice", "score", "attempts", "answered"]:
        if key not in st.session_state:
            st.session_state[key] = None if key in ["quiz_words", "correct_answer", "quiz_choice"] else 0

    if st.button("🎯 Show me a question."):
        st.session_state.answered = False
        st.session_state.quiz_choice = None
    
        # Step 1: Pick one vowel
        vowels = df["Stressed_Vowel"].dropna().unique().tolist()
        vowel1 = random.choice(vowels)
    
        # Get 4 words with that vowel
        group1 = df[df["Stressed_Vowel"] == vowel1]["WORD"].dropna().unique().tolist()
        if len(group1) < 4:
            st.warning("Not enough words to form a quiz. Try again.")
        else:
            group1_words = random.sample(group1, 4)
    
            # Step 2: Pick a truly different vowel
            different_vowels = [v for v in vowels if v != vowel1]
            odd_word = None
            odd_vowel = None
    
            for v2 in random.sample(different_vowels, len(different_vowels)):
                group2 = df[df["Stressed_Vowel"] == v2]["WORD"].dropna().unique().tolist()
                if group2:
                    odd_word = random.choice(group2)
                    odd_vowel = v2
                    break
    
            if odd_word:
                # Combine and store as (word, vowel) pairs
                combined = [(w, vowel1) for w in group1_words] + [(odd_word, odd_vowel)]
                random.shuffle(combined)
    
                # Extract just the words for display
                st.session_state.quiz_words = [w for w, _ in combined]
                st.session_state.correct_answer = odd_word
            else:
                st.warning("Could not find an odd-one-out word. Try again.")


    # Display quiz if ready
    if st.session_state.quiz_words:
        st.session_state.quiz_choice = st.radio(
            "Which word has a different stressed vowel?",
            st.session_state.quiz_words,
            key="quiz_choice_radio"
        )

        if st.button("✅ Show the answer"):
            if not st.session_state.answered:
                st.session_state.attempts += 1
                st.session_state.answered = True

                if st.session_state.quiz_choice == st.session_state.correct_answer:
                    st.session_state.score += 1
                    st.success(f"🎉 Correct! The odd word is **{st.session_state.correct_answer}**.")
                    st.balloons()
                else:
                    st.error(f"❌ Incorrect. The correct answer is **{st.session_state.correct_answer}**.")

    # Show score summary
    if st.session_state.attempts > 0:
        st.markdown(f"### 🧾 Score: {st.session_state.score} / {st.session_state.attempts}")

