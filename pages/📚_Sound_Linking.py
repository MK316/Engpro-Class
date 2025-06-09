import streamlit as st

# --- Configuration ---
# Base URL for raw GitHub content
github_raw_base = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/soundlinking/"

# Generate filenames like "Sound linking.001.png" to "Sound linking.020.png"
slide_filenames = [f"Sound linking.{i:03}.png" for i in range(1, 21)]  # Adjust the range as needed

# Full image URLs
slide_urls = [github_raw_base + filename for filename in slide_filenames]

total_slides = len(slide_filenames)

# --- Session state to track current slide ---
if 'slide_index' not in st.session_state:
    st.session_state.slide_index = 0

# --- Sidebar or main dropdown ---
selected = st.selectbox("📑 Go to Slide:", options=range(total_slides), format_func=lambda i: f"Slide {i + 1}")
st.session_state.slide_index = selected

# --- Display current slide ---
image_url = github_base_url + slide_filenames[st.session_state.slide_index]
st.image(image_url, use_column_width=True, caption=f"Slide {st.session_state.slide_index + 1}")

# --- Navigation buttons ---
col1, col2, col3 = st.columns([1, 6, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1
        st.experimental_rerun()

with col3:
    if st.button("Next ➡️") and st.session_state.slide_index < total_slides - 1:
        st.session_state.slide_index += 1
        st.experimental_rerun()
