import streamlit as st
from gtts import gTTS
from io import BytesIO
import io

# --- Page Header ---
st.set_page_config(page_title="Lesson 15: [s] and [z]", layout="wide")
st.markdown("### 📙 Lesson 15. Three consonant pairs")
st.caption("Workbook page 77")

image_url = "https://github.com/MK316/Engpro-Class/raw/main/images/L15-keywords.png"
st.image(image_url, caption="A: B, C (Place); A, B: C (Manner)", use_container_width=True)
st.markdown("---")

# --- Audio Function ---
def generate_audio(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        return audio_fp.read()
    except Exception as e:
        st.error(f"Error generating audio for '{text}'")
        st.exception(e)
        return None

def generate_audio_simple(text):
    tts = gTTS(text=text, lang='en')
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)
    return audio_data

# --- Section 1: Word Pairs ---
st.markdown("### [1] Sound group A: [s] and [z]")

word_pairs = [
    {"en": "face and phase", "ko": "페이스와 페이즈"},
    {"en": "pressure and pleasure", "ko": "프레셔와 플레져"},
    {"en": "church and judge", "ko": "처치와 저지"},
]

for i, pair in enumerate(word_pairs):
    st.markdown(f"**🔹 English:** {pair['en']}  \n**🔸 Korean:** {pair['ko']}")
    col1, col2 = st.columns(2)
    with col1:
        en_audio = generate_audio(pair["en"], lang="en")
        if en_audio:
            st.audio(en_audio, format="audio/mp3")
    with col2:
        ko_audio = generate_audio(pair["ko"], lang="ko")
        if ko_audio:
            st.audio(ko_audio, format="audio/mp3")
    st.markdown("---")

# --- Section 2: Word Positions ---
st.markdown("#### 🎤 Practice Words by Position")

vowel_practice = {
    "[s]": {
        "Beginning": "same, sign, city, cinema, signature, system, sorry",
        "Middle": "lesson, custom, castle, history",
        "End": "bus, face, course, makes, miss, house, plus"
    },
    "[z]": {
        "Beginning": "zoo, zero, zest, zeal, zone, zinc, zipper, zebra",
        "Middle": "crazy, busy, easy, dizzy, cousin, puzzle, dozen",
        "End": "as, was, raise, is, buzz, his, breeze, amaze"
    }
}

for sound, positions in vowel_practice.items():
    st.markdown(f"#### {sound} Words")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**Beginning:** {positions['Beginning']}")
        if st.button(f"▶️ Beginning ({sound})", key=f"{sound}_beg"):
            audio = generate_audio_simple(positions["Beginning"])
            st.audio(audio.getvalue(), format="audio/mp3")

    with col2:
        st.write(f"**Middle:** {positions['Middle']}")
        if st.button(f"▶️ Middle ({sound})", key=f"{sound}_mid"):
            audio = generate_audio_simple(positions["Middle"])
            st.audio(audio.getvalue(), format="audio/mp3")

    with col3:
        st.write(f"**End:** {positions['End']}")
        if st.button(f"▶️ End ({sound})", key=f"{sound}_end"):
            audio = generate_audio_simple(positions["End"])
            st.audio(audio.getvalue(), format="audio/mp3")

st.markdown("---")

# --- Section 3: [s] vs [z] Contrast ---

st.markdown("#### 🔊 More practice: Listen and Compare [s] vs. [z]")

contrast_pairs = [
    ("Sue", "zoo"),
    ("face", "phase"),
    ("race", "raise"),
    ("bus", "buzz"),
    ("ice", "eyes"),
    ("place", "plays"),
    ("pease", "peas"),
    ("price", "prize"),
    ("racer", "razor")
]

for idx, (s_word, z_word) in enumerate(contrast_pairs):
    st.markdown(f"**[s]** `{s_word}` vs. **[z]** `{z_word}`")
    col1, col2 = st.columns(2)

    with col1:
        st.write(f"🔹 {s_word}")
        audio_s = generate_audio_simple(s_word)
        st.audio(audio_s.getvalue(), format="audio/mp3")

    with col2:
        st.write(f"🔸 {z_word}")
        audio_z = generate_audio_simple(z_word)
        st.audio(audio_z.getvalue(), format="audio/mp3")

    st.markdown("---")

# --- Section 2: Word Pair 2 ---
st.markdown("### [2] Sound group B: [ʃ] and [ʒ]")

st.info("Lips are rounded when you make these sounds. The only difference between the two sounds is the voicing. Everything else in the mouth should be the same.")

st.markdown("#### 🎤 Practice Words by Position")

vowel_practice2 = {
    "[ʃ]": {
        "Beginning": "shine, shame, sugar",
        "Middle": "fashion, cushion",
        "End": "fish, cash, smash"
    },
    "[ʒ]": {
        "Beginning": "genre",
        "Middle": "pleasure, measure, leisure, vision, decision, television, lesion, occasion, usual, Asia, conclusion",
        "End": "beige, garage, camouflage, entourage, rouge, regime, massage"
    }
}

for sound, positions in vowel_practice2.items():
    st.markdown(f"#### {sound} Words")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**Beginning:** {positions['Beginning']}")
        if st.button(f"▶️ Beginning ({sound})", key=f"{sound}_beg"):
            audio = generate_audio_simple(positions["Beginning"])
            st.audio(audio.getvalue(), format="audio/mp3")

    with col2:
        st.write(f"**Middle:** {positions['Middle']}")
        if st.button(f"▶️ Middle ({sound})", key=f"{sound}_mid"):
            audio = generate_audio_simple(positions["Middle"])
            st.audio(audio.getvalue(), format="audio/mp3")

    with col3:
        st.write(f"**End:** {positions['End']}")
        if st.button(f"▶️ End ({sound})", key=f"{sound}_end"):
            audio = generate_audio_simple(positions["End"])
            st.audio(audio.getvalue(), format="audio/mp3")

st.markdown("---")


# --- Section 3: Word Pair3 ---
st.markdown("### [3] Sound group B: [tʃ] and [dʒ]")

st.info("Lips are rounded when you make these sounds. The only difference between the two sounds is the voicing. Everything else in the mouth should be the same.")

st.markdown("#### 🎤 Practice Words by Position")

vowel_practice3 = {
    "[tʃ]": {
        "Beginning": "chain, church, cherry, champion",
        "Middle": "preacher, teacher, butcher, catcher",
        "End": "match, catch, church, peach"
    },
    "[dʒ]": {
        "Beginning": "giant, gym, gelly, giraffe",
        "Middle": "magic, pledger, pager, larger",
        "End": "cage, large, forge, badge"
    }
}

for sound, positions in vowel_practice3.items():
    st.markdown(f"#### {sound} Words")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.write(f"**Beginning:** {positions['Beginning']}")
        if st.button(f"▶️ Beginning ({sound})", key=f"{sound}_beg"):
            audio = generate_audio_simple(positions["Beginning"])
            st.audio(audio.getvalue(), format="audio/mp3")

    with col2:
        st.write(f"**Middle:** {positions['Middle']}")
        if st.button(f"▶️ Middle ({sound})", key=f"{sound}_mid"):
            audio = generate_audio_simple(positions["Middle"])
            st.audio(audio.getvalue(), format="audio/mp3")

    with col3:
        st.write(f"**End:** {positions['End']}")
        if st.button(f"▶️ End ({sound})", key=f"{sound}_end"):
            audio = generate_audio_simple(positions["End"])
            st.audio(audio.getvalue(), format="audio/mp3")

st.markdown("---")

import random

# --- Section 4: Listening Quiz ---
# --- Section 4: Listening Quiz ---
st.markdown("### [4] Listening Quiz")
st.markdown("🎧 Listen to each audio and type the word you hear.")

# Word list (in pairs)
quiz_words = [
    "chess", "Jess", "Jack", "Zack", "chew", "jew", "zoo", "jew",
    "heads", "hedge", "zone", "Joan", "bays", "beige", "ruse", "rouge",
    "Caesar", "seizure", "version", "virgin", "lesion", "legion", "pleasure", "pledger"
]

# Show in pairs
for i in range(0, len(quiz_words), 2):
    word1 = quiz_words[i]
    word2 = quiz_words[i+1]

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("🔊 **Audio 1**")
        audio1 = generate_audio_simple(word1)
        st.audio(audio1.getvalue(), format="audio/mp3")
        ans1 = st.text_input(f"Type what you heard (1):", key=f"input_{i}")
        if ans1:
            if ans1.strip().lower() == word1.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect. Try again.")

    with col2:
        st.markdown("🔊 **Audio 2**")
        audio2 = generate_audio_simple(word2)
        st.audio(audio2.getvalue(), format="audio/mp3")
        ans2 = st.text_input(f"Type what you heard (2):", key=f"input_{i+1}")
        if ans2:
            if ans2.strip().lower() == word2.lower():
                st.success("✅ Correct")
            else:
                st.error(f"❌ Incorrect. Try again.")

    st.markdown("---")
