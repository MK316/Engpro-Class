import streamlit as st
import io
from gtts import gTTS

# Create four tabs
tabs = st.tabs(["❄️ Lesson 10", "❄️ Speechnotes"])

# Content for each tab
with tabs[0]:
    st.markdown("#### 📚 Word Stress in English")

    # Define text sections with improved clarity and structure
    text_sections = {
        "[1] Word Stress in English": """In English, word stress is typically fixed for a given word with a specific meaning. 
        Changing the stress can alter the word’s meaning. However, the position of stress may shift when additional 
        morphemes are added. For example, the word *economy* changes to *economic*. Another case is when the grammatical category of a word changes, such as when the verb *record* becomes the noun *record*. 
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

    st.markdown("---")    
    st.markdown("#### B. How to Manifest Stressed Syllables") 
    st.write("Characteristics of Stressed Syllables: Stressed syllables are typically longer in duration, louder in intensity, and higher in pitch than unstressed syllables in a word. However, the pitch may not always be higher, as it can vary depending on the intended meaning of the word within a specific sentence.")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/banana.jpg", caption="Example 'banana'")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/banana-spec.jpg", caption="Spectrogram of 'banana'")

    st.markdown("---")    
    st.markdown("#### C. Words Can Have More Than One Stress")
    st.write("When a word consists of more than two syllables, it can have more than one stress. In such cases, there are primary (main) stresses and secondary stresses, which are weaker than the primary stress.")
    st.write("Primary stress is indicated with an accent mark ( ́ ) or an upper bar ( ˈ ) in dictionaries. Secondary stress is marked with a grave mark ( ̀ ) or a lower bar ( ˌ ) in dictionaries.")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/L10-words.jpg", caption="Practice words")

    # Word lists categorized by stress pattern
    stress_words = {
        "First syllable": ["accident", "strawberry", "seventy", "personal", "elephant", "February", "salary"],
        "Second syllable": ["acceptance", "vanilla", "examine", "translation", "gorilla", "December", "employer"],
        "Third syllable": ["accidental", "absolute", "seventeen", "personnel", "kangaroo", "gasoline", "employee"]
    }

    st.markdown("---")    
    # Display word lists and audio buttons
    st.markdown("#### 🎧 Practice: Stress by position")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("##### 🔹1st Syllable")
        st.write(", ".join(stress_words["First syllable"]))
        if st.button("Play First Syllable Words", key="first_syllable"):
            audio = generate_audio(", ".join(stress_words["First syllable"]))
            st.audio(audio.getvalue(), format='audio/mp3')

    with col2:
        st.markdown("##### 🔹2nd Syllable")
        st.write(", ".join(stress_words["Second syllable"]))
        if st.button("Play Second Syllable Words", key="second_syllable"):
            audio = generate_audio(", ".join(stress_words["Second syllable"]))
            st.audio(audio.getvalue(), format='audio/mp3')

    with col3:
        st.markdown("##### 🔹3rd Syllable")
        st.write(", ".join(stress_words["Third syllable"]))
        if st.button("Play Third Syllable Words", key="third_syllable"):
            audio = generate_audio(", ".join(stress_words["Third syllable"]))
            st.audio(audio.getvalue(), format='audio/mp3')

    st.markdown("---")        
    st.markdown("#### D. English stress can have the following characteristics")
    st.markdown("""
    1. By placing stress on the correct syllables, you can ensure that your pronunciation is more easily understood by listeners.
    2. Change in grammatical category: noun, verb, or adjective
    - These are known as homographs (words that are spelled the same but have different meanings)
    - See the examples below:
    """)
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/L10-words2.jpg")

    # Sentences containing words in different grammatical functions
    sentences = {
        "1. invalid (Noun/Adjective)": "The hospital provides special care for an invalid, as they require constant medical attention, but his insurance claim was deemed invalid due to missing documents.",
        "2. desert (Noun/Verb)": "The stranded travelers feared they would be left in the desert without water, but the guide refused to desert them in such a dangerous situation.",
        "3. conflict (Noun/Verb)": "The ongoing conflict between the two nations has led to trade restrictions, yet neither side wants to conflict with international laws.",
        "4. conduct (Noun/Verb)": "The professor’s strict conduct in class ensures discipline, while students are expected to conduct themselves professionally during discussions.",
        "5. content (Noun/Verb)": "She carefully examined the content of the report before submission, making sure it would content the board members.",
        "6. contest (Noun/Verb)": "The debate tournament included a heated contest among schools, but the losing team decided to contest the final results.",
        "7. permit (Noun/Verb)": "The government must issue a permit before construction begins, but the residents plan to permit only eco-friendly projects.",
        "8. object (Noun/Verb)": "The museum displayed a rare object from ancient history, but some critics continued to object to its removal from its country of origin.",
        "9. increase (Noun/Verb)": "The company saw an increase in sales last quarter, but the CEO plans to increase investment in research to sustain growth.",
        "10. exploit (Noun/Verb)": "His book is an inspiring exploit of adventure and survival, but critics argue that he tried to exploit the story for financial gain."
    }

    sentences2 = {
        "1. invalid (Noun/Adjective)": "The hospital provides special care for **an invalid**, as they require constant medical attention, but his insurance claim was deemed **invalid** due to missing documents.",
        "2. desert (Noun/Verb)": "The stranded travelers feared they would be left in **the desert** without water, but the guide refused **to desert** them in such a dangerous situation.",
        "3. conflict (Noun/Verb)": "**The ongoing conflict** between the two nations has led to trade restrictions, yet neither side wants **to conflict** with international laws.",
        "4. conduct (Noun/Verb)": "The professor’s strict **conduct** in class ensures discipline, while students are expected **to conduct** themselves professionally during discussions.",
        "5. content (Noun/Verb)": "She carefully examined **the content** of the report before submission, making sure it would **content** the board members.",
        "6. contest (Noun/Verb)": "The debate tournament included **a heated contest** among schools, but the losing team decided **to contest** the final results.",
        "7. permit (Noun/Verb)": "The government must issue **a permit** before construction begins, but the residents plan **to permit** only eco-friendly projects.",
        "8. object (Noun/Verb)": "The museum displayed **a rare object** from ancient history, but some critics continued **to object** to its removal from its country of origin.",
        "9. increase (Noun/Verb)": "The company saw **an increase** in sales last quarter, but the CEO plans **to increase** investment in research to sustain growth.",
        "10. exploit (Noun/Verb)": "His book is **an inspiring exploit** of adventure and survival, but critics argue that he tried **to exploit** the story for financial gain."
    }
    # User selection for the sentence to play
    st.markdown("### 🎧 Practice: Words with differenct stress")
    selected_sentence = st.selectbox("Choose a sentence to hear the pronunciation:", list(sentences.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Button to generate and play the selected sentence
    if st.button("Play Selected Sentence"):
        audio_data = generate_audio(sentences[selected_sentence])
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.write(f"**Sentence:** {sentences2[selected_sentence]}")

    st.markdown("##### 3. Compound nouns (when two words are combined to create a new meaning): The stress is typically on the first word.")
    st.markdown("""
    ||A + N| Compound noun|
    |--|--|--|
    |1| bed room|bedroom|
    |2| green house | greenhouse|
    |3| dark room | darkroom|
    |4| blue bird | bluebird|
    |5| white house | White house|
    |6| black board| blackboard|
    |7|| mailman, fisherman, fireman, policeman, repairman|
    |8|| lifeguard, babysitter, movie star, bartender, saleswoman, disc Jockey|
    """)

    # ✾ PRACTICE sentences
    practice_sentences = {
        "1. The convict escaped from jail.": "The convict escaped from jail.",
        "2. Keep a record of your expenses.": "Keep a record of your expenses.",
        "3. The police don’t suspect anyone.": "The police don’t suspect anyone.",
        "4. The student will present a speech.": "The student will present a speech.",
        "5. The present was not wrapped.": "The present was not wrapped.",
        "6. The invalid was in the hospital.": "The invalid was in the hospital.",
        "7. Please print your address clearly.": "Please print your address clearly.",
        "8. Be sure to record your speech.": "Be sure to record your speech.",
        "9. The letter is in the envelop.": "The letter is in the envelop.",
        "10. I want to envelop the baby in my arms.": "I want to envelop the baby in my arms."
    }
    
    # Title
    st.markdown("### 🎧 Practice Sentences")
    
    # User selects a sentence
    selected_practice_sentence = st.selectbox("Choose a sentence to hear the pronunciation:", list(practice_sentences.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Button to generate and play the selected sentence
    if st.button("Play Selected Sentence", key="practice_sentences"):
        audio_data = generate_audio(practice_sentences[selected_practice_sentence])
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.write(f"**Sentence:** {practice_sentences[selected_practice_sentence]}")
with tabs[1]:
    st.markdown("### 📒 Speechnotes ")
    st.markdown("Visit [Speechnotes](https://speechnotes.co) to hone your reading skills. Read the sentences aloud one by one and observe how the AI transcribes them in real-time. This interactive exercise will not only improve your pronunciation but also give you immediate feedback on how accurately your spoken words are being captured by the AI. Perfect for enhancing your reading fluency!")

