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
    st.markdown("---")
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
        "List 1": ("Leopard, Giraffe, Dolphin, Sea Otter, Octopus", "https://github.com/MK316/Engpro-Class/raw/main/images/animal01.jpg"),
        "List 2": ("Squirrel, Chameleon, Penguin, Ocelot, Hippopotamus", "https://github.com/MK316/Engpro-Class/raw/main/images/animal02.jpg"),
        "List 3": ("Jaguar, Tortoise, Rhinoceros, Kangaroo, Wolf", "https://github.com/MK316/Engpro-Class/raw/main/images/animal03.jpg"),
        "List 4": ("Coyote, Camel, Zebra, Buffalo, Alligator", "https://github.com/MK316/Engpro-Class/raw/main/images/animal04.jpg")
    }
    st.markdown("---")
    
    st.markdown("### 🐳 More practice: Names")
    st.caption("Choose an Animal List to Hear the Pronunciation")
    
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
    # st.image(animal_lists[selected_list][1], caption=f"{selected_list} - Animals")
    st.image(animal_lists[selected_list][1], caption=animal_lists[selected_list][0])
    if st.button("Generate and Play Audio", key="audio_animal_list"):
        audio_data = generate_audio(animal_lists[selected_list][0])
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(f"{selected_list}: {animal_lists[selected_list][0]}")
        
#######################################################################
with tabs[1]:
    st.markdown("### 📒 Lesson 6: Vowels in ‘but’, ‘bought’, ‘boat’")
    st.write("Word list: cut, caught, coat")
    col3, col4, col5 = st.columns(3)
    # Function to generate audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    with col3:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/cut.jpg", width=300, caption="[ʌ]")
        sentence_cut = "The director shouted cut while filming."
        st.write(sentence_cut)
        if st.button("Play Audio", key="audio_cut"):
            audio_data = generate_audio(sentence_cut)
            st.audio(audio_data.getvalue(), format='audio/mp3')
    
    with col4:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/caught.jpg", width=300, caption="[ɔ]")
        sentence_caught = "A cat caught a mouse."
        st.write(sentence_caught)
        if st.button("Play Audio", key="audio_caught"):
            audio_data = generate_audio(sentence_caught)
            st.audio(audio_data.getvalue(), format='audio/mp3')
    
    with col5:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/coat.jpg", width=300, caption="[oʊ]")
        sentence_coat = "My sister got a new winter coat."
        st.write(sentence_coat)
        if st.button("Play Audio", key="audio_coat"):
            audio_data = generate_audio(sentence_coat)
            st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("---")
    
    # Practice Section
    st.markdown("### 🎤 Practice Words by Position")
    vowel_practice = {
        "[ʌ]": {
            "Beginning": "up, of, us",
            "Middle": "lucky, hug, much, rough",
            "End": "None"
        },
        "[ɔ]": {
            "Beginning": "off, all, also",
            "Middle": "boss, long, across",
            "End": "law, raw"
        }
    }
    
    for vowel, positions in vowel_practice.items():
        st.markdown(f"#### {vowel} Words")
        col_beginning, col_middle, col_end = st.columns(3)
        
        with col_beginning:
            if positions["Beginning"] != "None":
                st.write(f"**Beginning:** {positions['Beginning']}")
                if st.button(f"Play Beginning Words ({vowel})", key=f"audio_{vowel}_beginning"):
                    audio_data = generate_audio(positions['Beginning'])
                    st.audio(audio_data.getvalue(), format='audio/mp3')
        
        with col_middle:
            if positions["Middle"] != "None":
                st.write(f"**Middle:** {positions['Middle']}")
                if st.button(f"Play Middle Words ({vowel})", key=f"audio_{vowel}_middle"):
                    audio_data = generate_audio(positions['Middle'])
                    st.audio(audio_data.getvalue(), format='audio/mp3')
        
        with col_end:
            if positions["End"] != "None":
                st.write(f"**End:** {positions['End']}")
                if st.button(f"Play End Words ({vowel})", key=f"audio_{vowel}_end"):
                    audio_data = generate_audio(positions['End'])
                    st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("---")

    # Contrast Practice Section
    st.markdown("### 🔊 Contrast Practice")
    contrast_pairs = {
        "1. but / bought / boat": "but, bought, boat",
        "2. cut / caught / coat": "cut, caught, coat",
        "3. hull / hall / hole": "hull, hall, hole",
        "4. scull / call / coal": "scull, call, coal",
        "5. mull / mall / mole": "mull, mall, mole",
        "6. dug / dog": "dug, dog",
        "7. done / dawn": "done, dawn",
        "8. lung / long": "lung, long",
        "9. cuff / cough": "cuff, cough",
        "10. saw / so": "saw, so",
        "11. law / low": "law, low",
        "12. tall / toll": "tall, toll",
        "13. bald / bold": "bald, bold",
        "14. color / caller / collar": "color, caller, collar"
    }
    
    selected_pair = st.selectbox("Select a contrast pair to hear:", list(contrast_pairs.keys()))
    if st.button("Play Contrast Audio", key="contrast_audio"):
        audio_data = generate_audio(contrast_pairs[selected_pair])
        st.audio(audio_data.getvalue(), format='audio/mp3')
#######################################################################
with tabs[2]:
    st.markdown("### 📒 Lesson 7: Diphthong vowels in English")
    st.image("https://github.com/MK316/Engpro-Class/raw/main/images/diphthong.jpg", caption="I don't know how that boy won the game last night, but it was impressive!")

    diphthong_text="I don't know how that boy won the game last night, but it was impressive!"

    # Function to generate audio
    def generate_audio(text):
        tts = gTTS(text=text, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    # Play audio button
    if st.button("Play Contrast Audio", key="diphthong"):
        audio_data_1 = generate_audio(diphthong_text)
        st.audio(audio_data_1.getvalue(), format='audio/mp3')

    st.markdown("**game, night, how, don't, boy**")

    st.markdown("### 🔍 Practice: Clear articulation of diphthongs")
    # Sentences for audio generation
    sentences = {
        "A. Oh, really!": "Oh, really!",
        "B. So, let’s get started.": "So, let’s get started.",
        "C. Please don’t tell him.": "Please don’t tell him.",
        "D. It’s very cold in here.": "It’s very cold in here.",
        "E. You don’t have to.": "You don’t have to."
    }

    st.markdown("### 🎧 Practice Sentences")

    # Generate audio for each sentence
    for key, text in sentences.items():
        st.write(key)
        if st.button(f"Play {key}", key=key):
            audio_data = generate_audio(text)
            st.audio(audio_data.getvalue(), format='audio/mp3')
#######################################################################
with tabs[3]:
    st.markdown("""
    - [Lesson 5](https://engpro-listening.streamlit.app/Lesson_05)
    - [Lesson 6](https://engpro-listening.streamlit.app/Lesson_06)
    - [Lesson 7](https://engpro-listening.streamlit.app/Lesson_07)
    """)

