import streamlit as st


# Base URL to GitHub raw content
github_base_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/soundlinking/"
slide_filenames = [f"Sound linking.{i:03}.png" for i in range(1, 16)]
total_slides = len(slide_filenames)

# Initialize session state
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0

# --- Combined navigation bar (Previous | Dropdown | Next) ---
col1, col2, col3 = st.columns([1.2, 3, 1])

with col1:
    if st.button("⬅️ Previous") and st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1
        st.rerun()
with col2:
    if st.button("Next ➡️") and st.session_state.slide_index < total_slides - 1:
        st.session_state.slide_index += 1
        st.rerun()
with col3:
    selected = st.selectbox(
        "🔢 Jump to Slide", 
        range(1, total_slides + 1), 
        index=st.session_state.slide_index, 
        label_visibility="collapsed"
    )
    st.session_state.slide_index = selected - 1
st.markdown("---")


# --- Display the selected slide ---
image_url = github_base_url + slide_filenames[st.session_state.slide_index]
st.image(image_url, caption=f"📄 Slide {st.session_state.slide_index + 1} of {total_slides}", use_container_width=True)

st.markdown("---")

# --- YouTube video section ---
st.markdown("### 🎥 Watch an example video")
st.caption("'My heart is drenched in wine.'")

# Example: starting at 60 seconds (1 minute)
youtube_url = "https://youtu.be/cAhDjrc5s64?si=BP0DR8S-xlSSTOuv&t=58"  # replace with actual video ID and time

st.video(youtube_url)
