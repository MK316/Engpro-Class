import streamlit as st

# Base URL pointing to raw GitHub images
github_base_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/soundlinking/"

# Generate filenames: Sound linking.001.png ~ Sound linking.015.png
slide_filenames = [f"Sound linking.{i:03}.png" for i in range(1, 16)]

# Total slides
total_slides = len(slide_filenames)

# Initialize session state
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# --- Navigation buttons ABOVE the image ---
col1, col2, col3 = st.columns([2, 6, 1])  # Wider left column for 'Previous'

with col1:
    if st.button("⬅️ Previous") and st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1
        st.rerun()

with col3:
    if st.button("Next ➡️") and st.session_state.slide_index < total_slides - 1:
        st.session_state.slide_index += 1
        st.rerun()

# --- Dropdown to jump to a slide ---
selected = st.selectbox("🔢 Jump to Slide", range(1, total_slides + 1), index=st.session_state.slide_index)
st.session_state.slide_index = selected - 1

# --- Display current slide ---
image_url = github_base_url + slide_filenames[st.session_state.slide_index]
st.image(image_url, caption=f"📄 Slide {st.session_state.slide_index + 1} of {total_slides}", use_container_width=True)
