import streamlit as st
from gtts import gTTS
import io


# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 TTS", "💧 App2", "💧 App3"])

# Content for each tab
with tabs[0]:
    st.markdown("### 🐾 Table of contents ")
    st.markdown("""
    - **Lesson 1**: Pronouncing English vowels  
    - **Lesson 2**: Stress and rhythm in English  
    - **Lesson 3**: Consonant articulation  
    - **Lesson 4**: Connected speech patterns  
    - **Lesson 5**: Vowel [ɑ] and spelling confusion
    - **Lesson 6**: Vowels in ‘but’, ‘bought’, ‘boat’
    - **Lesson 7**: Diphthong vowels in English
    - **Lesson 8**: Unstressed vowel (schwa vowel) as in ‘ago’, ‘upon’, ‘company’
    - **Lesson 9**: R-colored vowels as in ‘perfect’ and ‘percent’

    """)
# Text-to-Speech tab
with tabs[1]:
    st.subheader("Text-to-Speech Converter (using Google TTS")
    st.markdown("""
    Sample sentences:
    
    1. The quick brown fox jumps over lazy dogs near the bright city.
    2. Tom bought a colorful, vivid kite for flying on windy days.
    3. Many students receive good grades when they study history and biology.
    4. He thought the small children should play outside in sunny weather.
    5. A joyful crowd cheered as the wise, old man spoke profoundly.
    6. Jessica left her black sketchbook at the espresso stand.
    7. 오늘은 날씨가 참 좋네요.
    8. 재원이는 제주도에 놀러갔어요.
    """)
    
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language: 🇰🇷 🇺🇸 🇬🇧 🇷🇺 🇫🇷 🇪🇸 🇯🇵 ", ["English (American)", "Korean", "English (British)", "Russian", "Spanish", "French", "Japanese"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        # Map human-readable language selection to language codes and optionally to TLDs for English
        lang_codes = {
            "English (American)": ("en", 'com'),
            "Korean": ("ko", None),
            "English (British)": ("en", 'co.uk'),
            "Russian": ("ru", None),
            "Spanish": ("es", None),
            "French": ("fr", None),
            "Japanese": ("ja", None)
        }
        language_code, tld = lang_codes[language]

        # Assuming you have a version of gTTS that supports tld or you have modified it:
        # This check ensures that the tld parameter is only used when not None.
        if tld:
            tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
        else:
            tts = gTTS(text=text_input, lang=language_code, slow=False)
        
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)

        # Display the audio file
        st.audio(speech.getvalue(), format='audio/mp3')
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - pool vs. pull")
with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
