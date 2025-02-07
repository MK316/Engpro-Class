import streamlit as st
import streamlit.components.v1 as components
from gtts import gTTS
import io


# Create four tabs
tabs = st.tabs(["💧 Contents", "💧 Audio-samples", "💧 TTS", "💧 App3"])

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
# Define the list of sentences
sentences = [
    "The quick brown fox jumps over lazy dogs near the bright city.",
    "Tom bought a colorful, vivid kite for flying on windy days.",
    "Many students receive good grades when they study history and biology.",
    "He thought the small children should play outside in sunny weather.",
    "A joyful crowd cheered as the wise, old man spoke profoundly.",
    "Jessica left her black sketchbook at the espresso stand.",
    "오늘은 날씨가 참 좋네요.",
    "재원이는 제주도에 놀러갔어요."
]

# Audio-samples tab
with tabs[1]:
    selected_sentence = st.selectbox("Choose a sentence to generate audio:", sentences)

    if st.button("Generate Audio"):
        # Detect language based on content
        lang = 'ko' if any(char > '\u1100' and char < '\u11ff' for char in selected_sentence) else 'en'
        
        # Generate the audio using gTTS
        tts = gTTS(text=selected_sentence, lang=lang)
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        # Correctly display the audio file
        st.audio(audio_data.getvalue(), format='audio/mp3')

# TTS tab
# TTS tab
with tabs[2]:
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language: 🇰🇷 🇺🇸 🇬🇧 🇷🇺 🇫🇷 🇪🇸 🇯🇵 ", ["English (American)", "Korean", "English (British)", "Russian", "Spanish", "French", "Japanese"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        # Map human-readable language selection to language codes
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
        if tld:
            tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
        else:
            tts = gTTS(text=text_input, lang=language_code, slow=False)
        
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)

        # Display the audio file
        st.audio(speech.getvalue(), format='audio/mp3')

with tabs[3]:
    st.write("IPA")
    
    # URL you want to embed
    url_to_embed = "https://ipa.typeit.org/"
    
    # Embed the URL using an iframe
    components.iframe(url_to_embed, width=700, height=800, scrolling=True)
