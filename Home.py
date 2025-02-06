import streamlit as st
from PIL import Image
import requests
from io import BytesIO

st.caption("English Pronunciation Practice")
st.title("Coming Soon")

# Add an image from GitHub
image_url = "https://github.com/MK316/Engpro-Class/raw/main/data/engpro-cover.png"

# Load and resize the image
response = requests.get(image_url)
img = Image.open(BytesIO(response.content))
img = img.resize((300, 300))  # Set custom width and height

st.image(img, caption="Practice Makes Perfect")
