import streamlit as st
from gtts import gTTS
import io


# Create four tabs
tabs = st.tabs(["📙 Lesson 13", "❄️ More practice"])

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

    st.markdown("#### [6] Punctuation Rules - commas, colons, semi-colons, parentheses, etc.")
    st.markdown("""
    1. Mr. Brown, _my new neighbor_, called me yesterday.
    2. Sam, _a convicted felon_, was sentenced to life in prison.
    3. He is very nice, _in my opinion_, and maybe he is the nicest person in the classroom.
    """)
                
    audio_url = "https://github.com/MK316/Engpro-Class/raw/main/audio/thoughgroup_M2.mp3"
    st.audio(audio_url, format='audio/mp3')


    st.markdown("---")


    # PRACTICE PHRASE
    st.markdown("##### ✰ PRACTICE")
    
    practice_text = """When the sunlight strikes raindrops in the air, they act as a prism and form a rainbow. 
    The rainbow is a division of white light into many beautiful colors. These take the shape of a long round arch, 
    with its path high above, and its two ends apparently beyond the horizon. 
    There is, according to legend, a boiling pot of gold at one end. People look, but no one ever finds it. 
    When a man looks for something beyond his reach, his friends say he is looking for the pot of gold at the end of the rainbow."""
    
    # Display the practice text
    st.write(practice_text)
    
    # Function to generate audio for the practice phrase
    def generate_practice_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Button to generate and play the practice phrase audio
    if st.button("🔊 Play Practice Phrase"):
        practice_audio = generate_practice_audio(practice_text)
        st.audio(practice_audio.getvalue(), format='audio/mp3')
    


    
with tabs[1]:

    # Define the practice passages
    practice_passages = {
        "1. Digital Literacy": """Digital literacy refers to the ability to use digital tools effectively for communication, research, and problem-solving. 
        In today’s world, digital competence is essential for students and educators alike. 
        Being digitally literate means not only knowing how to use technology but also understanding how to evaluate online information critically. 
        With the rapid development of artificial intelligence and automation, digital literacy has become a fundamental skill for academic success and professional growth.""",
    
        "2. Language Education": """Language education plays a crucial role in developing communication skills and cultural understanding. 
        Learning a language is not just about memorizing vocabulary and grammar rules, but also about practicing speaking, listening, reading, and writing in meaningful contexts. 
        Modern language teaching methods incorporate interactive activities, digital resources, and real-world applications to help learners become proficient users of the language. 
        Teachers need to provide opportunities for students to engage in authentic communication and critical thinking.""",
    
        "3. Teacher Qualification": """The qualifications of a teacher significantly influence the quality of education students receive. 
        A well-qualified teacher must possess subject knowledge, teaching skills, and the ability to foster an engaging learning environment. 
        In many educational systems, obtaining certification and undergoing continuous professional development are required for teachers to maintain high teaching standards. 
        Effective teachers not only impart knowledge but also inspire students to become lifelong learners and independent thinkers."""
    }
    
    # Pre-recorded audio file URLs for Male and Female voices
    audio_files_male = {
        "1. Digital Literacy": "https://github.com/MK316/Engpro-Class/raw/main/audio/DL-M.mp3",
        "2. Language Education": "https://github.com/MK316/Engpro-Class/raw/main/audio/Edu-M.mp3",
        "3. Teacher Qualification": "https://github.com/MK316/Engpro-Class/raw/main/audio/Teacher-M.mp3"
    }
    
    audio_files_female = {
        "1. Digital Literacy": "https://github.com/MK316/Engpro-Class/raw/main/audio/DL-F.mp3",
        "2. Language Education": "https://github.com/MK316/Engpro-Class/raw/main/audio/Edu-F.mp3",
        "3. Teacher Qualification": "https://github.com/MK316/Engpro-Class/raw/main/audio/Teacher-F.mp3"
    }
    
    # Display Practice Passage Selection
    st.markdown("### ✰ PRACTICE: Select a Passage to Listen/practice")
    selected_passage = st.selectbox("Choose a passage: 3 topics", list(practice_passages.keys()))
    
    # Display the selected passage
    st.write(practice_passages[selected_passage])
    
    # Arrange two buttons in a row
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔊 Male Voice"):
            st.audio(audio_files_male[selected_passage], format='audio/mp3')
    
    with col2:
        if st.button("🔊 Female Voice"):
            st.audio(audio_files_female[selected_passage], format='audio/mp3')
