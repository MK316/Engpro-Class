import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.markdown("### 🐣 English Pronunication (Spring 2025)")
st.markdown('"_Confidence is a habit that can be developed by acting as if you already had the confidence you desire to have."_  Brian Tracy (writer and motivational public speaker)')

# Add an image from GitHub
image_url = "https://github.com/MK316/Engpro-Class/raw/main/data/engpro-cover.png"

# Load and resize the image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img = img.resize((500, 500))  # Set custom width and height

st.image(img, caption="©️ MK316 English Pronunciation Practice: Practice Makes Perfect")

st.markdown("⛺Goto [MK316 home](https://mk316.github.io)")
