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
    word_list_text = "O-spelling words: cop, cod, lock, comedy, contrary, company, copy, oxen, option, on, odd, honest, shop, rocket, block, cot, top, fox, spot, opera, follow, constitution. "
    word_list_text += "A-spelling words: father, arm, want, wallet, dark, wasp, watch, March."
    
    if st.button("Generate and Play Audio", key="audio_word_list"):
        audio_data = generate_audio(word_list_text)
        st.audio(audio_data.getvalue(), format='audio/mp3')

    # Read-aloud
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/constitution.jpg")

    text1 = """The Constitution of the United States is the supreme law of the United States of America. 
    The Constitution, originally comprising seven articles, delineates the national frame of government. 
    Its first three articles entrench the doctrine of the separation of powers, 
    whereby the federal government is divided into three branches: 
    the legislative, consisting of the bicameral Congress; the executive,
    consisting of the President; and the judicial, 
    consisting of the Supreme Court and other federal courts. 
    Articles Four, Five and Six entrench concepts of federalism, 
    describing the rights and in relationship to the federal responsibilities of state governments and of the states government.
    Article Seven establishes the procedure subsequently used by the thirteen States to ratify it."""
    

    if st.button("Generate and Play Audio", key="text1"):
        audio_data = generate_audio(text1)
        st.audio(audio_data.getvalue(), format='audio/mp3')    

    # More practice: names of animal
    # Define animal lists and corresponding image URLs
    animal_lists = {
        "List 1": ("Leopard, Giraffe, Dolphin, Sea Otter, Octopus", "https://github.com/MK316/Animal-Images/raw/main/animal01.jpg"),
        "List 2": ("Squirrel, Chameleon, Penguin, Ocelot, Hippopotamus", "https://github.com/MK316/Animal-Images/raw/main/animal02.jpg"),
        "List 3": ("Jaguar, Tortoise, Rhinoceros, Kangaroo, Wolf", "https://github.com/MK316/Animal-Images/raw/main/animal03.jpg"),
        "List 4": ("Coyote, Camel, Zebra, Buffalo, Alligator", "https://github.com/MK316/Animal-Images/raw/main/animal04.jpg")
    }
    
    st.markdown("### Choose an Animal List to Hear the Pronunciation")
    
    # Dropdown to select the list
    selected_list = st.selectbox("Select an animal list:", list(animal_lists.keys()))
    
    # Function to generate and play audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    # Display the corresponding image for the selected list
    st.image(animal_lists[selected_list][1], caption=f"{selected_list} - Animals")
    
    if st.button("Generate and Play Audio", key="audio_animal_list"):
        audio_data = generate_audio(animal_lists[selected_list][0])
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(f"{selected_list}: {animal_lists[selected_list][0]}")
        



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

