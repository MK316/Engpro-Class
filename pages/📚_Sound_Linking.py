import streamlit as st

# Define GitHub base URL (use raw.githubusercontent.com format for images)
github_base_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/soundlinking/"

# Slide filenames (make sure they match your GitHub files)
slide_filenames = [
    f"Sound linking.{i:03}.png" for i in range(14, 19)  # example: slide 14 to 18
]

# Total slides
total_slides = len(slide_filenames)

# Initialize session state
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# Navigation buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1

with col3:
    if st.button("Next ➡️") and st.session_state.slide_index < total_slides - 1:
        st.session_state.slide_index += 1

# Dropdown to select slide
selected = st.selectbox("🔢 Jump to slide", range(1, total_slides + 1), index=st.session_state.slide_index)
st.session_state.slide_index = selected - 1

# Show slide
image_url = github_base_url + slide_filenames[st.session_state.slide_index]
st.image(image_url, caption=f"Slide {st.session_state.slide_index + 1}", use_container_width=True)
