import streamlit as st
from gtts import gTTS
from io import BytesIO

# Example dictionary mapping indices to text and audio URLs
introductions = {
    1: {"text": "Enthusiastic Introduction: 'Hello everyone, I'm Mary Benson, a freshman here at GNU, studying in the Department of English Education. I'm pursuing my dream to become an English teacher because I love literature and language. I'm excited about the opportunity to inspire a love for reading in others and look forward to growing alongside my classmates!'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio1.mp3?raw=true"},
    2: {"text": "Professional Introduction: 'Good afternoon, my name is Mary Benson. I'm a freshman at GNU, focusing on English education. My goal is to become an English teacher who uses innovative methods to engage students actively. I'm dedicated to making a positive impact in the field of education, starting right here in our Department of English Education.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio2.mp3?raw=true"},
    3: {"text": "Casual Introduction: 'Hi everyone, I'm Mary Benson! I just started my freshman year at GNU and I'm working toward becoming an English teacher. I have a huge passion for storytelling and creative writing, and I'm excited to share that with my future students. Outside of my studies, I love to explore local coffee shops and write poetry.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio3.mp3?raw=true"},
    4: {"text": "Inspirational Introduction: 'Hi, I’m Mary Benson, a freshman in the Department of English Education at GNU. I chose to study here because I believe that education has the power to transform lives. I'm particularly interested in how literature can broaden our perspectives. I aim to create a classroom environment where every student feels valued and inspired to learn.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio4.mp3?raw=true"},
    5: {"text": "Detailed Introduction: 'Hello! My name’s Mary Benson, and I’m a new student here at GNU, majoring in English Education. I was drawn to this field because I admire the profound impact that great teachers can have on their students. I'm eager to develop my skills in literature analysis and pedagogy and look forward to contributing to our community here in the Department of English Education.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio5.mp3?raw=true"},
    6: {"text": "Warm and Welcoming Introduction: 'Hi everyone, I’m John Smith, a freshman at GNU in the Department of English Education. I'm originally from Jinju, a city known for its rich culture and history. I’m here to pursue my passion for teaching English and to make a difference by inspiring students. I’m thrilled to be part of this community and excited to learn with all of you!'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio6.mp3?raw=true"},
    7: {"text": "Friendly and Approachable Introduction: 'Hello, my name's John Smith, and I'm just starting my first year at GNU, focusing on becoming an English teacher. I grew up in Jinju, which is a beautiful place back home that I miss a lot. I’m passionate about bringing creativity into the classroom and making learning enjoyable for everyone. I can't wait to get to know all of you and learn together!'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio7.mp3?raw=true"},
    8: {"text": "Reflective and Inspirational Introduction: 'Good afternoon, I’m John Smith, a proud resident of Jinju, now embarking on my journey here at GNU in the Department of English Education. I chose to study English teaching because I believe in the transformative power of education. Coming from a place steeped in tradition and innovation, I aim to blend those values into my teaching approach.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio8.mp3?raw=true"},
    9: {"text": "Detailed and Professional Introduction: 'Hello everyone, I'm John Smith from Jinju. I’m currently a freshman at GNU, majoring in English Education. I’ve always been fascinated by the way languages can connect people and I’m eager to explore this further as I train to become an English teacher. I’m committed to applying my learnings to foster a dynamic and inclusive learning environment.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio9.mp3?raw=true"},
    10: {"text": "Enthusiastic and Engaging Introduction: 'Hey there! I’m John Smith, fresh into my first year at GNU in the Department of English Education. Hailing from the vibrant city of Jinju, I bring with me a passion for English and a dream to inspire future generations. I’m looking forward to collaborating with all of you, sharing ideas, and growing together in this exciting phase of our lives.'",
        "audio": "https://github.com/yourusername/repo/blob/main/audio10.mp3?raw=true"}
}


# Assuming you have already created tabs
tabs = st.tabs(["Scripts", "🔎 Introduce_yourself_audio", "🌀 TTS app", "🌀 Padlet to submit"])

with tabs[0]:
    st.title("Scripts (example)")
    url = "https://github.com/MK316/Engpro-Class/blob/main/practice/readme.md"  # Replace with the actual URL you want to display
    if st.button('Visit Website'):
        js = f"window.open('{url}')"
        st.components.v1.html(f'<script>{js}</script>', height=0)  
with tabs[1]:
    st.title("Practice 01: Introduce Yourself")
    st.write("Introduce yourself in public")

    # Let the user select a number from 1 to 10
    choice = st.selectbox("Choose an introduction number:", list(introductions.keys()))

    # Display the introduction text
    st.write(introductions[choice]["text"])

    # Play the audio
    st.audio(introductions[choice]["audio"])

with tabs[2]:
    st.title("Text-to-Speech Converter")
    text_input = st.text_area("Enter text to convert to speech:")
    accent_option = st.selectbox("Choose Accent:", ["American", 'British'])
    if st.button("Convert to Speech"):
        tts = gTTS(text=text_input, lang='en', tld='com' if accent_option == 'American' else 'co.uk')
        speech_file = BytesIO()
        tts.write_to_fp(speech_file)
        speech_file.seek(0)
        st.audio(speech_file, format='audio/mp3')

with tabs[3]:
    st.title("Padlet: to post your video")
    url = "https://padlet.com/mirankim316/S25Engpro"  # Replace with the actual URL you want to display
    if st.button('Visit Website'):
        js = f"window.open('{url}')"
        st.components.v1.html(f'<script>{js}</script>', height=0)  
