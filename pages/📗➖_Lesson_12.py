import streamlit as st

# Create four tabs
tabs = st.tabs(["📙 Lesson 12", "❄️ App", "❄️ Lesson 16", "❄️ Lesson 17"])

# Content for each tab
with tabs[0]:
    st.markdown("#### 📒 Lesson 12: Rhythm and Intonation in English")

    # Section 1: Introduction to Rhythm
    st.markdown("#### ➤ Rhythm in English")
    st.write("""
    1. In English, certain words within a sentence must be emphasized, while others should be spoken more rapidly and weakly. 
       This creates the rhythm of English, which differs from Korean.
    """)
    st.write("**Comparison:** Stress-timed (English) vs. Syllable-timed (Korean)")
    st.write("**Example:**")
    st.write(" - Korean: 가나다라 마바사아 자차카타 파하 (Syllable-timed)")
    st.write(" - English: A B C song (Stress-timed)")


    # 🎥 Embedded YouTube Video for Rhythm
    st.markdown("#### 🎥 Watch: Understanding Rhythm in English")
    youtube_url = "https://www.youtube.com/watch?v=CHmwmGJ3HbE"  # Replace with actual video link
    st.video(youtube_url)
    
    # Section 2: Contractions in English
    st.markdown("#### 🔹 Contractions in Spoken English")
    st.write("""
    2. Contractions, formed by combining two words together into one, are commonly used in spoken English.
    """)
    
    contractions = {
        "I am → I'm": "I’m going to the store.",
        "You are → You're": "You're my best friend.",
        "She is → She's": "She's coming later.",
        "He will → He'll": "He’ll call you soon.",
        "They have → They've": "They've finished their work."
    }
    
    st.markdown("#### 🎧 Listen to Contractions in Natural Speech")
    selected_contraction = st.selectbox("Choose a contraction to hear:", list(contractions.keys()))

    # Function to generate audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    # Play contraction audio
    if st.button("Play Selected Sentence"):
        audio_data = generate_audio(contractions[selected_contraction])
        st.audio(audio_data.getvalue(), format="audio/mp3")
        st.write(f"**Sentence:** {contractions[selected_contraction]}")

    # Section 3: Using Full Forms
    st.markdown("#### 🔹 When to Use Full Forms")
    st.write("""
    3. Using the full form of a contraction in conversation can make your speech sound unnatural, as full forms are generally 
       reserved for formal speeches or when emphasizing specific words.
    """)

    # Example sentences: Full form vs. Contraction
    examples = {
        "Formal Speech:": "I will not attend the meeting today.",
        "Natural Speech:": "I won’t attend the meeting today.",
        "Formal Speech:": "He is not coming to the party.",
        "Natural Speech:": "He’s not coming to the party."
    }
    
    st.markdown("#### 🎧 Listen to the Difference: Full vs. Contracted Speech")
    selected_example = st.selectbox("Choose an example to hear:", list(examples.keys()), key="full_vs_contracted")

    # Play full vs. contracted audio
    if st.button("Play Example Sentence", key="example_audio"):
        audio_data = generate_audio(examples[selected_example])
        st.audio(audio_data.getvalue(), format="audio/mp3")
        st.write(f"**Sentence:** {examples[selected_example]}")

with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
