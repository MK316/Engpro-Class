import streamlit as st
from gtts import gTTS
from io import BytesIO

st.set_page_config(page_title="Plural -s Pronunciation Practice", layout="wide")
st.title("📚 Pronunciation of Noun Plural -s/-es")

st.markdown("""
English plurals ending in **-s/-es** are pronounced in three different ways depending on the final sound of the singular noun:
- `/s/` after voiceless sounds (e.g., **cats**, **books**)
- `/z/` after voiced sounds (e.g., **dogs**, **days**)
- `/ɪz/` after sibilant sounds (e.g., **buses**, **wishes**)
""")
st.markdown("---")

# Audio function
def generate_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_fp = BytesIO()
    tts.write_to_fp(audio_fp)
    audio_fp.seek(0)
    return audio_fp

# Words categorized by plural ending
plural_examples = {
    "/s/ sound (voiceless ending)": ["maps", "cats", "packs", "laughs", "paths"],
    "/z/ sound (voiced ending)": ["cabs", "kids", "bags", "caves", "pens", "bells","teachers", "ways"],
    "/ɪz/ sound (sibilant ending)": ["cases","roses","fishes","garages","matches","badges"]
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
