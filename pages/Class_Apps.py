import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components  # For embedding YouTube videos
from gtts import gTTS
import io

# Function to create word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Streamlit tabs
tabs = st.tabs(["📈 QR", "⏳ Timer", "👥 Grouping", "⛅ Word Cloud", "🔊 Text-to-Speech"])

# QR Code tab
with tabs[0]:
    st.subheader("QR Code Generator")
    qr_link = st.text_input("Enter a link to generate a QR code:")
    caption = st.text_input("Enter a caption for your QR code:")  # Allows user to type a caption

    # Adding a 'Generate QR Code' button
    generate_qr_button = st.button("Generate QR Code")
    
    if generate_qr_button and qr_link:
        # Generate the QR code only when the button is clicked
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_link)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')

        # Convert the QR code image to RGB format and resize
        qr_img = qr_img.convert('RGB')  # Convert to RGB to be compatible with st.image
        qr_img = qr_img.resize((600, 600))  # Resize the image

        # Display the resized image with the user-provided caption
        st.image(qr_img, caption=caption, use_container_width=False, width=400)

# Text-to-Speech tab
with tabs[4]:
    st.subheader("Text-to-Speech Converter")
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language:", ["Korean", "English (American)", "English (British)", "Russian", "Spanish", "French", "Japanese"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        # Map human-readable language selection to language codes
        lang_codes = {
            "Korean": "ko",
            "English (American)": "en-us",
            "English (British)": "en-uk",
            "Russian": "ru",
            "Spanish": "es",
            "French": "fr",
            "Japanese": "ja"
        }
        language_code = lang_codes[language]

        # Use gTTS to convert text to speech
        tts = gTTS(text=text_input, lang=language_code, slow=False)
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)

        # Display the audio file
        st.audio(speech.getvalue(), format='audio/mp3')

# Continue with your existing code for other tabs...
