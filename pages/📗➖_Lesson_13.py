import streamlit as st
from gtts import gTTS
import io


# Create four tabs
tabs = st.tabs(["📙 Lesson 13", "❄️ App", "❄️ App", "❄️ App"])

# Content for each tab
with tabs[0]:
    st.markdown("#### 📒 Lesson 13: Thought grouping")

    st.write("""
    * When words are combined to form a sentence, certain words are further grouped into smaller units and pronounced together to convey the intended meaning more effectively. These smaller units are known as **thought groups**.
    * There are no fixed rules for forming thought groups, as the grouping depends on the speaker's intended meaning. However, there are some tips for creating basic thought groups.  

    _**Note**_: The following guidelines indicate where you can pause, but this does not mean that you must stop at every indicated point. Instead, it should be understood as a suggestion that you *may* pause there before proceeding to the next thought group.
    """)

    st.markdown("##### 🎥 Video")
    youtube_url = "https://www.youtube.com/watch?v=Yd24_1n-8PM"
    st.video(youtube_url)



    # Custom CSS for blue-colored highlights
    st.markdown("""
        <style>
        .highlight { color: blue; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)
    
    # Define Thought Grouping Rules with Styled Display and Separate Audio Text
    thought_grouping_examples = {
        "[1] When subjects are long (more than 2 key words), insert a short pause after the subject.": {
            "display": [
                "I went shopping.", 
                "The lady was my mom’s friend.", 
                " <span class='highlight'>My younger brother</span> / will visit me tomorrow."
            ],
            "audio": [
                "I went shopping.", 
                "The lady was my mom’s friend.", 
                "My younger brother will visit me tomorrow."
            ]
        },
        "[2] Article + Adjective + Noun = one thought group": {
            "display": [
                "A big dog / is chasing / a little cat.",
                "He is / <span class='highlight'>a brilliant student.</span>"
            ],
            "audio": [
                "A big dog is chasing a little cat.",
                "He is a brilliant student."
            ]
        },
        "[3] Auxiliary verb + main verb = one thought group": {
            "display": [
                "He <span class='highlight'>was bringing</span> a cake. (He’s bringing a cake.)",
                "He <span class='highlight'>has been doing</span> great. (He’s been doing great.)",
                "I <span class='highlight'>should have seen</span> a doctor.",
                "<span class='highlight'>Would you be interested</span> in my story?"
            ],
            "audio": [
                "He was bringing a cake.",
                "He has been doing great.",
                "I should have seen a doctor.",
                "Would you be interested in my story?"
            ]
        },
        "[4] Put a pause before prepositional phrases or conjunctions.": {
            "display": [
                "The boy / ran / <span class='highlight'>into the room.</span>",
                "He devoted his life / for the peace / <span class='highlight'>of all mankind.</span>",
                "I can see my house / <span class='highlight'>from here.</span>",
                "He thought / <span class='highlight'>that he is smart.</span>",
                "We didn’t go / <span class='highlight'>because it started to rain.</span>"
            ],
            "audio": [
                "The boy ran into the room.",
                "He devoted his life for the peace of all mankind.",
                "I can see my house from here.",
                "He thought that he is smart.",
                "We didn’t go because it started to rain."
            ]
        },
        "[5] Verb + Object (simple object)": {
            "display": [
                "He <span class='highlight'>teaches English.</span>",
                "We <span class='highlight'>drank beer.</span>",
                "I <span class='highlight'>like football.</span>",
                "<span class='highlight'>He’s been calling her </span>/ all day."
            ],
            "audio": [
                "He teaches English.",
                "We drank beer.",
                "I like football.",
                "He’s been calling her all day."
            ]
        },
        "[6] Punctuation Rules - commas, colons, semi-colons, parentheses, etc.": {
            "display": [
                "Mr. Brown<span class='highlight'>, my new neighbor,</span> called me yesterday.",
                "Sam<span class='highlight'>, a convicted felon,</span> was sentenced to life in prison.",
                "He is very nice<span class='highlight'>; in my opinion,</span> he is the nicest person in the classroom."
            ],
            "audio": [
                "Mr. Brown, my new neighbor, called me yesterday.",
                "Sam, a convicted felon, was sentenced to life in prison.",
                "He is very nice; in my opinion, he is the nicest person in the classroom."
            ]
        }
    }
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display Thought Grouping Rules and Example Sentences
    st.markdown("### 📖 Thought Grouping Rules")
    
    for rule, content in thought_grouping_examples.items():
        st.markdown(f"#### {rule}")
        
        # Display formatted examples with blue highlights
        for example in content["display"]:
            st.markdown(f"- {example}", unsafe_allow_html=True)
    
        # Button to play corresponding audio
        if st.button(f"🔊 Play Examples for {rule}"):
            audio_text = " ".join(content["audio"])  # Combine all audio sentences
            audio_data = generate_audio(audio_text)
            st.audio(audio_data.getvalue(), format='audio/mp3')



    # Function to Generate Audio for Sentences
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    st.markdown("---")
    
    # Let User Select a Sentence for Audio Playback
    st.markdown("#### 🎧 Practice Thought Grouping with Audio")
    all_sentences = [sent for ex in thought_grouping_examples.values() for sent in ex]
    
    selected_sentence = st.selectbox("Choose a sentence to hear the pronunciation:", all_sentences)

    if st.button("🔊 Play Selected Sentence"):
        audio_data = generate_audio(selected_sentence)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.write(f"**Sentence:** {selected_sentence}")




    
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
    


    st.markdown("---")


    st.markdown("---")

with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
