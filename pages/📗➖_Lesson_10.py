import streamlit as st
import io
from gtts import gTTS

# Create four tabs
tabs = st.tabs(["❄️ Lesson 10", "❄️ App 1", "❄️ App2", "❄️ App3", ])

# Content for each tab
with tabs[0]:
    st.markdown("#### 📚 Word Stress in English")

    # Define text sections with improved clarity and structure
    text_sections = {
        "[1] Word Stress in English": """In English, word stress is typically fixed for a given word with a specific meaning. 
        Changing the stress can alter the word’s meaning. However, the position of stress may shift when additional 
        morphemes are added. For example, the word *economy* changes to *economic*. 

        Another case is when the grammatical category of a word changes, such as when the verb *record* becomes the noun *record*. 
        Additionally, stress may shift in compound words, such as *greenhouse*, which is formed from the words *green* and *house*.""",
    
        "[2] How to Identify Stress": """To determine the primary stress in individual words, consult a dictionary. 
        Stress is often indicated by a symbol, such as a single quotation mark before the stressed syllable, 
        boldface type, or both.""",
    
        "[3] Importance of Stress Placement": """Stress placement is crucial for clear English pronunciation. 
        Placing stress on the wrong syllable can confuse listeners and reduce speech intelligibility. 
        Therefore, practicing stress placement in words and phrases is essential. 

        In the next class, we will further explore stress patterns in phrases and sentences.""",

        "[4] Characteristics of Stressed Syllables": """Stressed syllables are typically:
        first, longer in duration,  
        second, louder in intensity, and  
        third, higher in pitch than unstressed syllables in a word.  

        However, the pitch may not always be higher, as it can vary depending on the intended meaning of the word within a specific sentence."""
    }

    
    # Function to generate audio for a given text
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display sections with audio
    st.markdown("#### A. Introduction: Understanding Word Stress in English")
    
    for section, text in text_sections.items():
        st.markdown(f"### {section}")
        st.write(text)
    
        # Generate audio for each section
        audio_data = generate_audio(text)
    
        # Display the audio player
        st.audio(audio_data.getvalue(), format="audio/mp3")
        
    st.markdown("#### B. How to manifest stressed syllables?") 

with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
