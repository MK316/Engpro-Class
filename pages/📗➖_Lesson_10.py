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
        Therefore, practicing stress placement in words and phrases is essential."""
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
    st.write("Characteristics of Stressed Syllables: Stressed syllables are typically: longer in duration, louder in intensity, and higher in pitch than unstressed syllables in a word. However, the pitch may not always be higher, as it can vary depending on the intended meaning of the word within a specific sentence.")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/banana.jpg", caption="Example 'banana'")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/banana-spec.jpg", caption="Spectrogram of 'banana'")


    st.markdown("#### C. Words can have more than one stress")
    st.write("When a word consists of more than two syllables, it can have more than one stress. In such cases, there are primary (main) stresses and secondary stresses, which are weaker than the primary stress.")
    st.write("Primary stress is indicated with an accent mark ( ́ ) or an upper bar ( ˈ ) in dictionaries. Secondary stress is marked with an grave mark ( ̀ ) or a lower bar ( ˌ ) in dictionaries.")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/L10-words.jpg", caption="Practice words")

# Word lists categorized by stress pattern
stress_words = {
    "First syllable": ["accident", "strawberry", "seventy", "personal", "elephant", "February", "salary"],
    "Second syllable": ["acceptance", "vanilla", "examine", "translation", "gorilla", "December", "employer"],
    "Third syllable": ["accidental", "absolute", "seventeen", "personnel", "kangaroo", "gasoline", "employee"]
}

    # Function to generate and play audio
    def generate_audio(words):
        text = ", ".join(words)
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Implement under tabs[0]
    
        # Display word lists and audio buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 🔹 First Syllable Stress")
            st.write(", ".join(stress_words["First syllable"]))
            if st.button("Play First Syllable Words", key="first_syllable"):
                audio = generate_audio(stress_words["First syllable"])
                st.audio(audio.getvalue(), format='audio/mp3')
    
        with col2:
            st.markdown("#### 🔹 Second Syllable Stress")
            st.write(", ".join(stress_words["Second syllable"]))
            if st.button("Play Second Syllable Words", key="second_syllable"):
                audio = generate_audio(stress_words["Second syllable"])
                st.audio(audio.getvalue(), format='audio/mp3')
    
        with col3:
            st.markdown("#### 🔹 Third Syllable Stress")
            st.write(", ".join(stress_words["Third syllable"]))
            if st.button("Play Third Syllable Words", key="third_syllable"):
                audio = generate_audio(stress_words["Third syllable"])
                st.audio(audio.getvalue(), format='audio/mp3')

with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
