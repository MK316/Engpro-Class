import streamlit as st
from gtts import gTTS
import io
# Create four tabs
tabs = st.tabs(["📙 Lesson 12-1", "📙 Lesson 12-2", "❄️ Intonation contour", "❄️ APP"])

# Content for each tab
with tabs[0]:
    st.markdown("#### 📒 Lesson 12: Rhythm and Intonation in English")

    # Section 1: Introduction to Rhythm
    st.markdown("#### ➤ Part 1: Rhythm in English")
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


    
    st.markdown("---")
    st.markdown("##### 📌 Practice contraction and full form")


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
    
    # Function to generate and play combined audio
    def generate_combined_audio(contraction, full_form):
        combined_text = f"{contraction}... {full_form}"  # Adding pause with ellipsis
        tts = gTTS(text=combined_text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the selected sentence
    if selected_sentence:
        contraction, full_form = sentence_pairs[selected_sentence]
    
        st.write(f"**Contraction Form:** {contraction}")
        st.write(f"**Full Form:** {full_form}")
    
        # Generate audio for both forms in a single file
        if st.button("🔊 Play Both Forms"):
            audio_data = generate_combined_audio(contraction, full_form)
            st.audio(audio_data.getvalue(), format='audio/mp3')

with tabs[1]:
    # Section 1: Introduction to Rhythm
    st.markdown("#### ➤ Part 2: English intonation")


    st.markdown("""
    1. When learning English, we often bring our native intonation and rhythm into our English speech, frequently resulting in a foreign accent.
    2. Intonation refers to the melody, rise, and fall of the voice when speaking. Each language uses pitch fluctuation differently, creating unique melody and intonation patterns.
    3. By mastering English intonation patterns, we can sound more like native speakers and communicate more effectively.
    4. Korean intonation to compare: 

    Example)
    """)

    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/LHLH.jpg", caption="Seoul dialect")

    st.markdown("""
    5. English intonation patterns are formed by the alternation of stress and accent in a sentence. By placing stress and accent on the appropriate words according to their meanings, you can learn these patterns. 

    - Geoge Washington
    - Bill Clinton
    - George Bush

    6. There are typical intonation patterns depending on the sentence types, which can practice.
    """)

    st.markdown("---")
    st.markdown("""
    #### 📘 Intonation by sentence types
    ##### A. Declarative sentence (description or statement)
    : The final rise-fall intonation is crucial to signal that your sentence is completed, serving a **‘finality’** function.
    _Note:_Ending sentences with a rise in tone can make you appear uncertain or lacking confidence.
    """)
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/Inton-dec.jpg")

    st.markdown("##### 🎧 Audio samples")
    
    # Define the sentences
    sentences = {
        "a. We like ice cream.": "We like ice cream.",
        "b. She likes to play tennis.": "She likes to play tennis.",
        "c. I have four sisters.": "I have four sisters.",
        "d. The boss gave him a raise.": "The boss gave him a raise."
    }
    
    
    # User selects a sentence
    selected_sentence = st.selectbox("Choose a sentence:", list(sentences.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the selected sentence
    if selected_sentence:
#        st.write(f"**Sentence:** {sentences[selected_sentence]}")
    
        # Generate and play audio
        if st.button("🔊 Play Sentence", key="declarative"):
            audio_data = generate_audio(sentences[selected_sentence])
            st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("---")
    st.markdown("""
    ##### B. Yes/No question
    """)
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/inton-yesno.jpg")

    # Define the sentences for Yes/No questions
    sentences_yesno = {
        "a. Are you hungry?": "Are you hungry?",
        "b. Do you have a minute?": "Do you have a minute?",
        "c.Can I ask you a question?": "Can I ask you a question?",
    }
    
    # User selects a sentence
    selected_sentence = st.selectbox("Choose a sentence:", list(sentences_yesno.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the selected sentence
    if selected_sentence:
        st.write(f"**Sentence:** {sentences_yesno[selected_sentence]}")  # Corrected dictionary reference
    
        # Generate and play audio
        if st.button("🔊 Play Sentence", key="yesno"):
            audio_data = generate_audio(sentences_yesno[selected_sentence])  # Corrected dictionary reference
            st.audio(audio_data.getvalue(), format='audio/mp3')

   
    st.markdown("---")
    st.markdown("""
    ##### C. Wh-question
    """)
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/inton-wh.jpg")
    
    # Define the sentences for Yes/No questions
    sentences_wh = {
        "a. Who will help him?": "Who will help him?",
        "b. When are you leaving?": "When are you leaving?",
        "c. Where are you going?": "Where are you going?",
        "d. How do you know?": "How do you know?",
        "e. Which book is yours?": "Which book is yours?"
    }
    
    # User selects a sentence
    selected_sentence = st.selectbox("Choose a sentence:", list(sentences_wh.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the selected sentence
    if selected_sentence:
        st.write(f"**Sentence:** {sentences_wh[selected_sentence]}")  # Corrected dictionary reference
    
        # Generate and play audio
        if st.button("🔊 Play Sentence", key="wh"):
            audio_data = generate_audio(sentences_wh[selected_sentence])  # Corrected dictionary reference
            st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("---")

    st.markdown("""
    ##### D. Two or more choices
    """)
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/inton-choice.jpg")
    
    # Define the sentences for Yes/No questions
    sentences_choice = {
        "a. Would you like coffee or tea?": "Would you like coffee or tea?",
        "b. Are you leaving tomorrow or Sunday?": "Are you leaving tomorrow or Sunday?",
        "c. She speaks French but not Spanish.": "She speaks French but not Spanish.",
        "d. Do you want to go London, Paris, or New York?": "Do you want to go London, Paris, or New York?",
    }
    
    # User selects a sentence
    selected_sentence = st.selectbox("Choose a sentence:", list(sentences_choice.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the selected sentence
    if selected_sentence:
        st.write(f"**Sentence:** {sentences_choice[selected_sentence]}")  # Corrected dictionary reference
    
        # Generate and play audio
        if st.button("🔊 Play Sentence", key="choice"):
            audio_data = generate_audio(sentences_choice[selected_sentence])  # Corrected dictionary reference
            st.audio(audio_data.getvalue(), format='audio/mp3')

    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/L13-notes.jpg")
    


with tabs[2]:
    st.markdown("Goto App: visible intonation contour")
    st.markdown("**[APP](https://mrkim21.github.io/appfolder/tts-pitch.html)**")
with tabs[3]:
    st.markdown("### Application")
