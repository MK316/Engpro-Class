import streamlit as st
from gtts import gTTS
import io

# Create four tabs
tabs = st.tabs(["💧 Lesson 5", "💧 Lesson 6", "💧 Lesson 7", "Listening"])

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 5: Vowel [ɑ] and spelling confusion")
     # Using columns to place images side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/a.jpg",
                 width=300, caption="[a]")
    with col2:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/bigA.jpg",
                 width=300, caption="[ɑ]")
    
    st.markdown("""
    ### 'o' spelling
    cop, cod, lock, comedy, contrary, company, copy, oxen, option, on, odd, honest, shop, rocket, block, cot, top, fox, spot, oera, follow, constitution

    ### 'a' spelling
    father, arm, want, wallet, dark, wasp, watch, March
    """)

        # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Prepare the text for audio pronunciation
    word_list_text = "o spelling: cop, cod, lock, comedy, contrary, company, copy, oxen, option, on, odd, honest, shop, rocket, block, cot, top, fox, spot, opera, follow, constitution. "
    word_list_text += "a spelling: father, arm, want, wallet, dark, wasp, watch, March."
    
    if st.button("Generate and Play Audio", key="audio_word_list"):
        audio_data = generate_audio(word_list_text)
        st.audio(audio_data.getvalue(), format='audio/mp3')
    

with tabs[1]:
    st.markdown("### 📒 Lesson 6: Vowels in ‘but’, ‘bought’, ‘boat’")

with tabs[2]:
    st.markdown("### 📒 Lesson 7: Diphthong vowels in English")
with tabs[3]:
    st.markdown("""
    - Lesson 5
    - Lesson 6
    - Lesson 7
    """)

