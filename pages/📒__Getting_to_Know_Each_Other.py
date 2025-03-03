import streamlit as st
from gtts import gTTS
from io import BytesIO
import streamlit.components.v1 as components
import requests
from PIL import Image
import os

# Assuming you have already created tabs
tabs = st.tabs(["Intro_Slides", "📖 Scripts", "🔎 Introduce_yourself_audio", "🌀 TTS app", "🌀 Padlet to submit"])


# Example dictionary mapping indices to text and audio URLs
introductions = {
    1: {"text": "Enthusiastic Introduction: 'Hello everyone, I'm Mary Benson, a freshman here at GNU, studying in the Department of English Education. I'm pursuing my dream to become an English teacher because I love literature and language. I'm excited about the opportunity to inspire a love for reading in others and look forward to growing alongside my classmates!'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro01.mp3?raw=true"},
    2: {"text": "Professional Introduction: 'Good afternoon, my name is Mary Benson. I'm a freshman at GNU, focusing on English education. My goal is to become an English teacher who uses innovative methods to engage students actively. I'm dedicated to making a positive impact in the field of education, starting right here in our Department of English Education.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro02.mp3?raw=true"},
    3: {"text": "Casual Introduction: 'Hi everyone, I'm Mary Benson! I just started my freshman year at GNU and I'm working toward becoming an English teacher. I have a huge passion for storytelling and creative writing, and I'm excited to share that with my future students. Outside of my studies, I love to explore local coffee shops and write poetry.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro03.mp3?raw=true"},
    4: {"text": "Inspirational Introduction: 'Hi, I’m Mary Benson, a freshman in the Department of English Education at GNU. I chose to study here because I believe that education has the power to transform lives. I'm particularly interested in how literature can broaden our perspectives. I aim to create a classroom environment where every student feels valued and inspired to learn.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro04.mp3?raw=true"},
    5: {"text": "Detailed Introduction: 'Hello! My name’s Mary Benson, and I’m a new student here at GNU, majoring in English Education. I was drawn to this field because I admire the profound impact that great teachers can have on their students. I'm eager to develop my skills in literature analysis and pedagogy and look forward to contributing to our community here in the Department of English Education.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro05.mp3?raw=true"},
    6: {"text": "Warm and Welcoming Introduction: 'Hi everyone, I’m John Smith, a freshman at GNU in the Department of English Education. I'm originally from Jinju, a city known for its rich culture and history. I’m here to pursue my passion for teaching English and to make a difference by inspiring students. I’m thrilled to be part of this community and excited to learn with all of you!'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro06.mp3?raw=true"},
    7: {"text": "Friendly and Approachable Introduction: 'Hello, my name's John Smith, and I'm just starting my first year at GNU, focusing on becoming an English teacher. I grew up in Jinju, which is a beautiful place back home that I miss a lot. I’m passionate about bringing creativity into the classroom and making learning enjoyable for everyone. I can't wait to get to know all of you and learn together!'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro07.mp3?raw=true"},
    8: {"text": "Reflective and Inspirational Introduction: 'Good afternoon, I’m John Smith, a proud resident of Jinju, now embarking on my journey here at GNU in the Department of English Education. I chose to study English teaching because I believe in the transformative power of education. Coming from a place steeped in tradition and innovation, I aim to blend those values into my teaching approach.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro08.mp3?raw=true"},
    9: {"text": "Detailed and Professional Introduction: 'Hello everyone, I'm John Smith from Jinju. I’m currently a freshman at GNU, majoring in English Education. I’ve always been fascinated by the way languages can connect people and I’m eager to explore this further as I train to become an English teacher. I’m committed to applying my learnings to foster a dynamic and inclusive learning environment.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro09.mp3?raw=true"},
    10: {"text": "Enthusiastic and Engaging Introduction: 'Hey there! I’m John Smith, fresh into my first year at GNU in the Department of English Education. Hailing from the vibrant city of Jinju, I bring with me a passion for English and a dream to inspire future generations. I’m looking forward to collaborating with all of you, sharing ideas, and growing together in this exciting phase of our lives.'",
        "audio": "https://github.com/MK316/Engpro-Class/blob/main/practice/intro10.mp3?raw=true"}
}


# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/intro_slides/"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

# Check if there are slides in the folder
if num_slides == 0:
    st.error("No slides found in the specified folder.")
    st.stop()  # Stop the app if there are no slides


# Function to load and display the image based on the current index with resizing
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)
    
    # Set your desired width for resizing
    desired_width = 1200  # Adjust this value as needed
    aspect_ratio = image.height / image.width
    new_height = int(desired_width * aspect_ratio)
    resized_image = image.resize((desired_width, new_height))

    st.image(resized_image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")


with tabs[0]:

    # Arrange 'Start', 'Previous', 'Next', and 'Slide Selector' in a single row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
    
    with col1:
        if st.button("⛳", key="start", help="Reset to the first slide"):
            st.session_state.slide_index = 0

    with col2:
        if st.button("◀️", key="previous", help="Go back to the previous slide"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
            else:
                st.warning("This is the first slide.")

    with col3:
        if st.button("▶️", key="next", help="Go to the next slide"):
            if st.session_state.slide_index < num_slides - 1:
                st.session_state.slide_index += 1
            else:
                st.warning("Final slide")

    with col4:
        # Display slide selector dropdown
        selected_slide = st.selectbox("",
                                      options=[f"Slide {i + 1}" for i in range(num_slides)],
                                      index=st.session_state.slide_index)

        # Update slide index if dropdown selection changes
        selected_slide_index = int(selected_slide.split()[-1]) - 1
        if selected_slide_index != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide_index

    # Display the image
    display_image()




# Tab 0: Scripts
with tabs[1]:
    # URL of the raw markdown file on GitHub
    url_to_embed1 = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/practice/readme.md"
    
    try:
        response = requests.get(url_to_embed1)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")



# Tab 1: Introduce Yourself with Audio
with tabs[2]:
    st.title("Introduce Yourself in 30 seconds!")
    choice = st.selectbox("Select an introduction", range(1, len(introductions) + 1), format_func=lambda x: f"Introduction {x}")
    intro_text = introductions[choice]["text"]
    intro_audio = introductions[choice]["audio"]
    
    st.write(intro_text)
    st.audio(intro_audio)

# Tab 2: Text-to-Speech App
with tabs[3]:
    st.title("Text-to-Speech Conversion")
    text_input = st.text_area("Enter text here:")
    accent_option = st.radio("Select Accent:", ["American", "British"])
    tld = 'com' if accent_option == 'American' else 'co.uk'
    
    if st.button("Convert"):
        tts = gTTS(text=text_input, lang='en', tld=tld)
        speech_file = BytesIO()
        tts.write_to_fp(speech_file)
        speech_file.seek(0)
        st.audio(speech_file, format='audio/mp3')

# Tab 3: Open External Website
with tabs[4]:
    st.markdown("Click + sign to make a new post. [Click here to open in a new tab](https://padlet.com/mirankim316/S25Engpro)")
    # URL you want to embed
    url_to_embed2 = "https://padlet.com/mirankim316/S25Engpro"
    
    # Embed the URL using an iframe
    components.iframe(url_to_embed2, width=700, height=700, scrolling=True)
