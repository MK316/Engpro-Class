import streamlit as st
import requests
from gtts import gTTS
from io import BytesIO
import streamlit.components.v1 as components


tabs = st.tabs(["💙 Padlet", "👭 Getting to know", "💧 HW#1","💧 HW#2","💧 HW#3 Hey Jude", "💧 HW#4", "💧 HW#5"])


##############################
# Content for the Schedule tab
with tabs[0]:
    st.header("🐾 Files to share: on Padlet")
    st.write("This Padlet serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/S26Engpro", width=700, height=800)

# ---------- TAB  ----------
with tabs[1]:


    # ---------------------------
    # Data: Introductions
    # ---------------------------
    introductions = {
        1: {
            "text": "Enthusiastic Introduction: 'Hello everyone, I'm Mary Benson, a freshman here at GNU, studying in the Department of English Education. I'm pursuing my dream to become an English teacher because I love literature and language. I'm excited about the opportunity to inspire a love for reading in others and look forward to growing alongside my classmates!'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro01.mp3?raw=true",
        },
        2: {
            "text": "Professional Introduction: 'Good afternoon, my name is Mary Benson. I'm a freshman at GNU, focusing on English education. My goal is to become an English teacher who uses innovative methods to engage students actively. I'm dedicated to making a positive impact in the field of education, starting right here in our Department of English Education.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro02.mp3?raw=true",
        },
        3: {
            "text": "Casual Introduction: 'Hi everyone, I'm Mary Benson! I just started my freshman year at GNU and I'm working toward becoming an English teacher. I have a huge passion for storytelling and creative writing, and I'm excited to share that with my future students. Outside of my studies, I love to explore local coffee shops and write poetry.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro03.mp3?raw=true",
        },
        4: {
            "text": "Inspirational Introduction: 'Hi, I’m Mary Benson, a freshman in the Department of English Education at GNU. I chose to study here because I believe that education has the power to transform lives. I'm particularly interested in how literature can broaden our perspectives. I aim to create a classroom environment where every student feels valued and inspired to learn.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro04.mp3?raw=true",
        },
        5: {
            "text": "Detailed Introduction: 'Hello! My name’s Mary Benson, and I’m a new student here at GNU, majoring in English Education. I was drawn to this field because I admire the profound impact that great teachers can have on their students. I'm eager to develop my skills in literature analysis and pedagogy and look forward to contributing to our community here in the Department of English Education.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro05.mp3?raw=true",
        },
        6: {
            "text": "Warm and Welcoming Introduction: 'Hi everyone, I’m John Smith, a freshman at GNU in the Department of English Education. I'm originally from Jinju, a city known for its rich culture and history. I’m here to pursue my passion for teaching English and to make a difference by inspiring students. I’m thrilled to be part of this community and excited to learn with all of you!'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro06.mp3?raw=true",
        },
        7: {
            "text": "Friendly and Approachable Introduction: 'Hello, my name's John Smith, and I'm just starting my first year at GNU, focusing on becoming an English teacher. I grew up in Jinju, which is a beautiful place back home that I miss a lot. I’m passionate about bringing creativity into the classroom and making learning enjoyable for everyone. I can't wait to get to know all of you and learn together!'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro07.mp3?raw=true",
        },
        8: {
            "text": "Reflective and Inspirational Introduction: 'Good afternoon, I’m John Smith, a proud resident of Jinju, now embarking on my journey here at GNU in the Department of English Education. I chose to study English teaching because I believe in the transformative power of education. Coming from a place steeped in tradition and innovation, I aim to blend those values into my teaching approach.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro08.mp3?raw=true",
        },
        9: {
            "text": "Detailed and Professional Introduction: 'Hello everyone, I'm John Smith from Jinju. I’m currently a freshman at GNU, majoring in English Education. I’ve always been fascinated by the way languages can connect people and I’m eager to explore this further as I train to become an English teacher. I’m committed to applying my learnings to foster a dynamic and inclusive learning environment.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro09.mp3?raw=true",
        },
        10: {
            "text": "Enthusiastic and Engaging Introduction: 'Hey there! I’m John Smith, fresh into my first year at GNU in the Department of English Education. Hailing from the vibrant city of Jinju, I bring with me a passion for English and a dream to inspire future generations. I’m looking forward to collaborating with all of you, sharing ideas, and growing together in this exciting phase of our lives.'",
            "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro10.mp3?raw=true",
        },
    }

    # ---------------------------
    # Helpers
    # ---------------------------
    @st.cache_data(ttl=3600, show_spinner=False)
    def fetch_markdown(url: str) -> tuple[str | None, str | None]:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code != 200:
                return None, f"HTTP {r.status_code}: {r.text[:200]}"
            return r.text, None
        except Exception as e:
            return None, str(e)

    def tts_to_audio_bytes(text: str, tld: str) -> BytesIO:
        tts = gTTS(text=text, lang="en", tld=tld)
        buf = BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        return buf

    # ---------------------------
    # UI: internal tabs (4 sections)
    # ---------------------------
    st.header("🧩 ENGPRO Practice Hub")

    inner_tabs = st.tabs(["📖 Scripts", "🔎 Introduce (Audio)", "🌀 TTS"])

    # ---- Inner Tab 1: Scripts (GitHub Markdown) ----
    with inner_tabs[0]:
        RAW_MD_URL = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/practice/readme.md"
        st.caption("Source (GitHub raw)")
        st.code(RAW_MD_URL, language="text")

        md_text, err = fetch_markdown(RAW_MD_URL)
        if err:
            st.error(f"Could not load the markdown file.\n\n{err}")
        else:
            st.markdown(md_text, unsafe_allow_html=False)

    # ---- Inner Tab 2: Introduce Yourself with Audio ----
    with inner_tabs[1]:
        st.subheader("Introduce Yourself in 30 seconds!")

        choice = st.selectbox(
            "Select an introduction",
            options=sorted(introductions.keys()),
            format_func=lambda x: f"Introduction {x}",
            key="intro_choice",
        )

        st.write(introductions[choice]["text"])
        st.audio(introductions[choice]["audio"])

    # ---- Inner Tab 3: Text-to-Speech App ----
    with inner_tabs[2]:
        st.subheader("Text-to-Speech Conversion")

        text_input = st.text_area("Enter text here:", key="tts_input")
        accent_option = st.radio("Select Accent:", ["American", "British"], horizontal=True, key="tts_accent")

        tld = "com" if accent_option == "American" else "co.uk"

        c1, c2 = st.columns([1, 2])
        with c1:
            convert = st.button("Convert", type="primary", use_container_width=True)
        with c2:
            st.caption("Tip: If the text is long, try shorter chunks for faster conversion.")

        if convert:
            if not text_input.strip():
                st.warning("Please enter text first.")
            else:
                try:
                    audio_buf = tts_to_audio_bytes(text_input.strip(), tld=tld)
                    st.audio(audio_buf, format="audio/mp3")
                except Exception as e:
                    st.error(f"TTS failed: {e}")

################################

with tabs[3]:
    st.caption("To be updated")
    
with tabs[4]:
    st.markdown("### 🎼  Hey Jude (HW #4)")

    # Define the URLs for the YouTube videos
    st.markdown("#### 1. Hey Jude (Beatles)")
    video_url1 = "https://www.youtube.com/embed/mQER0A0ej0M?si=eSi7vtIJzot9cqAf"
    st.video(video_url1, format="video/mp4", start_time=0)

    st.markdown("---")
    st.markdown("""
    #### 🎼 Lyrics

    1.  
    Hey Jude, don't make it bad.  
    Take a sad song and make it better.  
    Remember to let her into your heart,  
    Then you can start to make it better.  
    
    2.  
    Hey Jude, don't be afraid.  
    You were made to go out and get her.  
    The minute you let her under your skin,  
    Then you begin to make it better.  

    3.  
    And anytime you feel the pain, hey Jude, refrain,  
    Don't carry the world upon your shoulders.  
    For well you know that it's a fool who plays it cool  
    By making his world a little colder.  

    4.  
    Hey Jude, don't let me down.  
    You have found her, now go and get her.  
    Remember to let her into your heart,  
    Then you can start to make it better.  
    
    5.  
    So let it out and let it in, hey Jude, begin,  
    You're waiting for someone to perform with.  
    And don't you know that it's just you, hey Jude, you'll do,  
    The movement you need is on your shoulder.  
    
    6.  
    Hey Jude, don't make it bad.  
    Take a sad song and make it better.  
    Remember to let her under your skin,  
    Then you'll begin to make it  
    Better better better better better better, oh.  
    
    Na na na nananana, nannana, hey Jude...  
    (repeat X number of times, fade)

    """)

    st.markdown("[samples on Padlet](https://padlet.com/mirankim316/S26Engpro)")

with tabs[5]:
    st.markdown("To be announced")

with tabs[6]:
    st.write("To be updated")
