import streamlit as st

st.markdown("### 📙 Lesson 15. Three consonant pairs")
st.caption("Workbook page 77")
image_url = "https://github.com/MK316/Engpro-Class/raw/main/images/L15-keywords.png"
st.image(image_url, caption="A: B, C (Place); A, B: C (Manner)", use_container_width=True)

st.markdown("---")

st.markdown("### [1] Sound group A: [s] and [z]")

from gtts import gTTS
from io import BytesIO

# Define word pairs in English and Korean
word_pairs = [
    {"en": "face and phase", "ko": "페이스 그리고 페이즈"},
    {"en": "pressure and pleasure", "ko": "프레셔 그리고 플레져"},
    {"en": "church and judge", "ko": "처치 그리고  젇지"},
]

st.markdown("### [2] Listen to minimal pairs in English and Korean")

# Function to generate and return audio data
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

# Loop through each pair
for pair in word_pairs:
    st.markdown(f"**🔹 English:** {pair['en']}  \n**🔸 Korean:** {pair['en']")

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
