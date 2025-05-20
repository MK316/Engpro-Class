import streamlit as st
from gtts import gTTS
from io import BytesIO

# Page setup must come first
st.set_page_config(page_title="Plural -s Pronunciation Practice", layout="wide")

# --- Shared audio generation function ---
def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Create tab layout
tabs = st.tabs(["🌱 e(s) Pronunciation", "🌀 Plural Nouns Generator","🌱 Possessive form", "🍁 3rd person singular"])

# --- Tab 1: e(s) Pronunciation Rules ---
with tabs[0]:
    st.title("📚 Pronunciation of Noun Plural -s/-es")
    
    st.markdown("""
    English plurals ending in **-s/-es** are pronounced in three different ways depending on the final sound of the singular noun:
    
    - `/s/` after voiceless sounds (e.g., **cats**, **books**)
    - `/z/` after voiced sounds (e.g., **dogs**, **days**)
    - `/ɪz/` after sibilant sounds (e.g., **buses**, **wishes**)
    """)
    st.markdown("---")
    
    # Words categorized by plural ending
    plural_examples = {
        "/s/ sound (voiceless ending)": ["capps", "kits", "backs", "laughs", "paths"],
        "/z/ sound (voiced ending)": ["cabs", "kids", "bags", "caves", "pens", "bells", "teachers", "ways"],
        "/ɪz/ sound (sibilant ending)": ["cases", "roses", "fishes", "garages", "matches", "badges"]
    }
    
    # Display each category with audio
    for label, words in plural_examples.items():
        st.markdown(f"### 🔈 {label}")
        cols = st.columns(5)
        for i, word in enumerate(words):
            with cols[i % 5]:
                st.markdown(f"**{word}**")
                audio = generate_audio(word)
                st.audio(audio, format="audio/mp3")
        st.markdown("---")

# --- Tab 2: Plural Generator ---
with tabs[1]:
    st.title("🔤 Plural Noun Generator")

    # Pluralization logic
    def pluralize(noun):
        irregulars = {
            "man": "men",
            "woman": "women",
            "child": "children",
            "tooth": "teeth",
            "foot": "feet",
            "mouse": "mice",
            "goose": "geese",
            "ox": "oxen",
        }
        if noun in irregulars:
            return irregulars[noun]
        if noun.endswith("y") and noun[-2] not in "aeiou":
            return noun[:-1] + "ies"
        elif noun.endswith(("s", "x", "z", "ch", "sh")):
            return noun + "es"
        elif noun.endswith("f"):
            return noun[:-1] + "ves"
        elif noun.endswith("fe"):
            return noun[:-2] + "ves"
        else:
            return noun + "s"
    
    user_input = st.text_input("Enter a singular noun:", "")
    
    if user_input:
        singular = user_input.strip().lower()
        plural = pluralize(singular)
    
        st.markdown(f"### ✅ Singular: **{singular}**")
        st.audio(generate_audio(singular), format="audio/mp3")
    
        st.markdown(f"### 🔁 Plural: **{plural}**")
        st.audio(generate_audio(plural), format="audio/mp3")

#! Tab 3

with tabs[2]:
    st.markdown("#### Possessive form follows the same rule")

    # Define the phrases for each column
    col1_phrases = ["Philip's car", "Kate's book"]
    col2_phrases = ["Keith's brother", "Michael's idea"]
    col3_phrases = ["Peter's home", "Jim's mom"]

    def generate_audio(text):
        try:
            tts = gTTS(text=text, lang='en')
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            return audio_fp.read()
        except Exception as e:
            st.error(f"Error generating audio for '{text}'")
            return None

    col1, col2, col3 = st.columns(3)

    # Column 1
    with col1:
        for phrase in col1_phrases:
            st.markdown(f"**🔹 {phrase}**")
            audio = generate_audio(phrase)
            if audio:
                st.audio(audio, format="audio/mp3")

    # Column 2
    with col2:
        for phrase in col2_phrases:
            st.markdown(f"**🔹 {phrase}**")
            audio = generate_audio(phrase)
            if audio:
                st.audio(audio, format="audio/mp3")

    # Column 3
    with col3:
        for phrase in col3_phrases:
            st.markdown(f"**🔹 {phrase}**")
            audio = generate_audio(phrase)
            if audio:
                st.audio(audio, format="audio/mp3")

    st.markdown("---")
    st.markdown("#### 🎤 Try it yourself: Type a sentence and hear the audio")

    user_text = st.text_input("Enter a sentence to hear it:")

    if user_text:
        if st.button("▶️ Generate Audio"):
            try:
                tts = gTTS(user_text, lang='en')
                audio_fp = BytesIO()
                tts.write_to_fp(audio_fp)
                audio_fp.seek(0)
                st.audio(audio_fp, format="audio/mp3")
            except Exception as e:
                st.error("⚠️ Failed to generate audio. Try again later.")
                st.exception(e)

    


with tabs[3]:
    st.title("🗣️ Sentence Pronunciation Practice")
    st.markdown("Listen to how final **–s/-es** sounds are pronounced in connected speech.")

    sentences = [
        "He kicks it.",
        "She saves it.",
        "She misses it.",
        "It works easy.",
        "She means it.",
        "He washes it.",
        "He tastes it.",
        "The boy listens it.",
        "She catches it."
    ]

    for i, sentence in enumerate(sentences, start=1):
        st.markdown(f"**{i}. {sentence}**")
        audio = generate_audio(sentence)
        st.audio(audio, format="audio/mp3")
        st.markdown("---")

    st.markdown("#### 🌴 More Practice")
    sentences2 = [
        "Hello, James!",
        "What's new?",
        "That's all right.",
        "She measures about five feet 2 inches.",
        "He has blue eyes, and weighs 100 pounds.",
        "She enters law school after finals.",
        "He got good grades.",
        "She golfs, plays tennis, and swims.",
        "The store sells watches, rings, bracelets, diamonds, and rubies.",
        "My sister's dresses, blouses, and shoes are all new."
    ]

    for i, sentence in enumerate(sentences2, start=1):
        st.markdown(f"**{i}. {sentence}**")
        audio = generate_audio(sentence)
        st.audio(audio, format="audio/mp3")
        st.markdown("---")
    
