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
    * **Note**: The following guidelines indicate where you can pause, but this does not mean that you must stop at every indicated point. Instead, it should be understood as a suggestion that you *may* pause there before proceeding to the next thought group.
    """)

    st.markdown("##### 🎥 Video")
    youtube_url = "https://www.youtube.com/watch?v=Yd24_1n-8PM"
    st.video(youtube_url)
    
    # Define Thought Grouping Rules
    thought_grouping_examples = {
        "[1] When subjects are long (more than 2 key words), insert a short pause after the subject.": [
            "I went shopping.", 
            "The lady was my mom’s friend.", 
            "My younger brother / will visit me tomorrow."
        ],
        "[2] Article + Adjective + Noun = one thought group": [
            "A big dog / is chasing / a little cat.",
            "He is / a brilliant student."
        ],
        "[3] Auxiliary verb + main verb = one thought group": [
            "He was bringing a cake. (He’s bringing a cake.)",
            "He has been doing great. (He’s been doing great.)",
            "I should have seen a doctor.",
            "Would you be interested in my story?"
        ],
        "[4] Put a pause before prepositional phrases or conjunctions.": [
            "The boy / ran / into the room.",
            "He devoted his life / for the peace / of all mankind.",
            "I can see my house / from here.",
            "He thought / that he is smart.",
            "We didn’t go / because it started to rain."
        ]
    }

    # Display Thought Grouping Rules and Example Sentences
    for rule, examples in thought_grouping_examples.items():
        st.markdown(f"#### {rule}")
        for example in examples:
            st.write(f"- {example}")

    # Function to Generate Audio for Sentences
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    # Let User Select a Sentence for Audio Playback
    st.markdown("#### 🎧 Practice Thought Grouping with Audio")
    all_sentences = [sent for ex in thought_grouping_examples.values() for sent in ex]
    
    selected_sentence = st.selectbox("Choose a sentence to hear the pronunciation:", all_sentences)

    if st.button("🔊 Play Selected Sentence"):
        audio_data = generate_audio(selected_sentence)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.write(f"**Sentence:** {selected_sentence}")




    st.markdown("---")


    st.markdown("---")


    st.markdown("---")
    
with tabs[1]:
    st.markdown("### 📒 Lesson 15: ")
with tabs[2]:
    st.markdown("### 📒 Lesson 16: ")
with tabs[3]:
    st.markdown("### 📒 Lesson 17: ")
