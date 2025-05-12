import streamlit as st
from gtts import gTTS
import io

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
    {"en": "face and phase", "ko": "페이스와 페이즈"},
    {"en": "pressure and pleasure", "ko": "프레셔와 플레져"},
    {"en": "church and judge", "ko": "처치와 저지"},
]

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
    st.markdown(f"**🔹 English:** {pair['en']}  \n**🔸 Korean:** {pair['en']}")

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

st.markdown("### [2] Practice")
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    # Practice Section
    st.markdown("### 🎤 Practice Words by Position")
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
    
    for vowel, positions in vowel_practice.items():
        st.markdown(f"#### {vowel} Words")
        col_beginning, col_middle, col_end = st.columns(3)
        
        with col_beginning:
            if positions["Beginning"] != "None":
                st.write(f"**Beginning:** {positions['Beginning']}")
                if st.button(f"Play Beginning Words ({vowel})", key=f"audio_{vowel}_beginning"):
                    audio_data = generate_audio(positions['Beginning'])
                    st.audio(audio_data.getvalue(), format='audio/mp3')
        
        with col_middle:
            if positions["Middle"] != "None":
                st.write(f"**Middle:** {positions['Middle']}")
                if st.button(f"Play Middle Words ({vowel})", key=f"audio_{vowel}_middle"):
                    audio_data = generate_audio(positions['Middle'])
                    st.audio(audio_data.getvalue(), format='audio/mp3')
        
        with col_end:
            if positions["End"] != "None":
                st.write(f"**End:** {positions['End']}")
                if st.button(f"Play End Words ({vowel})", key=f"audio_{vowel}_end"):
                    audio_data = generate_audio(positions['End'])
                    st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("---")
