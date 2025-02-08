import streamlit as st
from gtts import gTTS
import io
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
    st.markdown("##### 🎥 Watch: 가나다 송")
    youtube_url = "https://www.youtube.com/watch?v=DzNubK1E-kk"  # Replace with actual video link
    st.video(youtube_url)

    
    st.markdown("##### 🎥 Watch: ABC song")
    youtube_url = "https://www.youtube.com/watch?v=nfDQdBhCnPo"  # Replace with actual video link
    st.video(youtube_url)

    

    
    # Section 2: Contractions in English
    st.markdown("#### ➤ Contractions in Spoken English")
    st.write("""
    2. Contractions, formed by combining two words together into one, are commonly used in spoken English.
    """)
    
    contractions = {
        "I am → I'm": "I am going to the stor. I’m going to the store.",
        "You are → You're": "You are my best friend. You're my best friend.",
        "She is → She's": "She is coming later.She's coming later.",
        "He will → He'll": "He will call you soon. He’ll call you soon.",
        "They have → They've": "They have finished their work. They've finished their work."
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
    st.markdown("#### ➤ When to Use Full Forms")
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
    
    st.markdown("---")
    st.markdown("##### Practice contraction and full form)


    # Define sentence pairs
    sentence_pairs = {
        "1. I’ll → I will": ("I’ll be there.", "I will be there."),
        "2. You’re → You are": ("You’re right.", "You are right."),
        "3. He’s → He is": ("He’s smart.", "He is smart."),
        "4. We’ve → We have": ("We’ve been through a lot.", "We have been through a lot."),
        "5. Isn’t → Is not": ("It isn’t right.", "It is not right."),
        "6. Doesn’t → Does not": ("It doesn’t matter.", "It does not matter."),
        "7. Hasn’t → Has not": ("He hasn’t eaten yet.", "He has not eaten yet."),
        "8. That’s → That is": ("That’s right.", "That is right."),
        "9. Won’t → Will not": ("It won’t happen again.", "It will not happen again."),
        "10. I’m → I am": ("I’m here.", "I am here.")
    }
    
    # Title
    st.markdown("### 🎧 Contraction vs. Full Forms")
    st.write("Select a sentence to hear the contrast between contraction and full form.")
    
    # User selects a sentence
    selected_sentence = st.selectbox("Choose a sentence:", list(sentence_pairs.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the selected sentence
    if selected_sentence:
        contraction, full_form = sentence_pairs[selected_sentence]
    
        st.write(f"**Contraction Form:** {contraction}")
        st.write(f"**Full Form:** {full_form}")
    
        # Generate audio for both forms
        if st.button("🔊 Play Contraction Form"):
            audio_data = generate_audio(contraction)
            st.audio(audio_data.getvalue(), format='audio/mp3')
    
        if st.button("🔊 Play Full Form"):
            audio_data = generate_audio(full_form)
            st.audio(audio_data.getvalue(), format='audio/mp3')


with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
