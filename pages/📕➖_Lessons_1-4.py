import streamlit as st
from gtts import gTTS
from PIL import Image
import random
import time
import io

# Create four tabs
tabs = st.tabs(["💧 Lesson 1", "💧 Lesson 2", "💧 Lesson 3", "💧 Lesson 4", "Listening practice"])

if 'show_image' not in st.session_state:
    st.session_state.show_image = False

# Define a function to toggle the visibility state
def toggle_image():
    st.session_state.show_image = not st.session_state.show_image

# Content for each tab
with tabs[0]:
    st.markdown("### 📒 Lesson 1: Pronouncing English vowels")
    st.markdown("#### A. Monophthong vowels (=single vowels)")
    
    # Frame sentence and target words
    frame_sentence = "I say {} again."
    target_words = ["heed", "hid", "head", "had", "who'd", "hood", "hawed", "hod", "hud", "ago"]
    
    # Adding an option to pronounce all words together
    target_words_extended = target_words + ["all words together"]

    # Dropdown to select the target word
    selected_word = st.selectbox("Choose a word to insert into the sentence or select 'all words together':", target_words_extended)
    
    # Check if the user selected "all words together"
    if selected_word == "all words together":
        # Generate a sentence concatenating all words
        all_words_sentence = " ".join([frame_sentence.format(word) for word in target_words])
        full_sentence = all_words_sentence
    else:
        # Generate the full sentence by inserting the selected word into the frame
        full_sentence = frame_sentence.format(selected_word)
    
    st.write("Generated Sentence: ", full_sentence)
    
    # Button to generate and play audio
    if st.button("Generate Audio"):
        # Use gTTS to convert the generated sentence to speech
        tts = gTTS(text=full_sentence, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        
        # Display the audio player with the generated audio
        st.audio(audio_data.getvalue(), format='audio/mp3')

    st.markdown("#### B. Diphthong vowels (=double vowels)")
    st.caption("Diphthong vowels start with one sound and glide into a different vowel. The smooth movement between these two ‘targets’ is crucial for correct pronunciation of diphthong vowels. This is not a sequence of two vowels: e.g., “I” in English and ‘아이’ in Korean are not exactly the same.")
    
    button = st.button("Show chart: diphthong vowels", on_click=toggle_image)

    # Conditional display of the image based on the session state
    if st.session_state.show_image:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/Vowelchart.png", caption="Vowel chart")
        st.caption("Image from Ladefoged & Johnson (2015; p.46), A course in phonetics")

with tabs[1]:
    st.markdown("### 📒 Lesson 2: Tense and lax ‘i’ - sheep vs. ship")
    # Using columns to place images side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/sheep.png",
                 width=300, caption="Image on the Left")
    with col2:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/ship.png",
                 width=300, caption="Image on the Right")

    # List of sentences to choose from
    sentences = [
        "The children are cleaning the ship",
        "The children are cleaning the sheep"
    ]

    # Button to generate and play audio
    if st.button("Random Audio"):
        # Randomly choose a sentence to be generated
        chosen_sentence = random.choice(sentences)
        tts = gTTS(text=chosen_sentence, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)

        # Display the audio player
        st.audio(audio_data.getvalue(), format='audio/mp3')
        
        # Display the sentence as caption below the audio
        st.caption(chosen_sentence)

    st.markdown("#### A. Warming-up: Tense [ i ]")
    # Word lists
    word_lists = {
        "Beginning": "eat, equal, easy, each",
        "Middle": "please, deep, peach, need",
        "End": "key, agree, pea, knee, tea"
    }

    # Generate and play audio with 2 seconds gap between words
    def generate_audio(word_list):
        # Creating a single string with pauses between words
        words_with_pause = ' '.join([word + '...' for word in word_list.split(', ')])
        tts = gTTS(text=words_with_pause, lang='en', tld='com')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    # Creating a single row for all buttons
    col_beginning, col_middle, col_end = st.columns(3)
    with col_beginning:
        if st.button("Play words at the Beginning"):
            audio_data = generate_audio(word_lists["Beginning"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists["Beginning"])

    with col_middle:
        if st.button("Play words in the Middle"):
            audio_data = generate_audio(word_lists["Middle"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists["Middle"])

    with col_end:
        if st.button("Play words at the End"):
            audio_data = generate_audio(word_lists["End"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists["End"])

    st.markdown("### B. Warming-up: Lax [ ɪ ]")
    # Word lists for lax [ɪ]
    lax_word_lists = {
        "Beginning": "is, itch, it, pin, sin, bit, pitch, mitt, give, win, gym, gift, with, lips, guilt, build, quick, this, symbol, syrup, little",
        "Middle": "vivid, limit, visit, habit, polish, mimic, permit, business, spirit, profit, mystic, logic, gossip",
        "End": "No words end with lax vowel in English"
    }

    # Creating a single row for all buttons for lax [ɪ]
    col_beginning_lax, col_middle_lax, col_end_lax = st.columns(3)
    with col_beginning_lax:
        if st.button("Play words at the Beginning", key="begin_lax"):
            audio_data = generate_audio(lax_word_lists["Beginning"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(lax_word_lists["Beginning"])

    with col_middle_lax:
        if st.button("Play words in the Middle", key="middle_lax"):
            audio_data = generate_audio(lax_word_lists["Middle"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(lax_word_lists["Middle"])
    with col_end_lax:
        if st.button("No words at the End", key="end_lax"):
            audio_data = generate_audio(lax_word_lists["End"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(lax_word_lists["End"])

    # C. Contrast
    st.markdown("### C. Contrast between tense and lax 'i'")

    # List of word pairs with descriptions
    word_pairs = [
        ("each", "itch"),
        ("peach", "pitch"),
        ("eat", "it"),
        ("scene", "sin"),
        ("heel", "hill"),
        ("cheap", "chip"),
        ("heat", "hit"),
        ("meat", "mitt"),
        ("seat", "sit"),
        ("lean", "Lynn"),
        ("wheel", "will"),
        ("Seeley (pron.)", "silly")
    ]
  
    # Create a dropdown to select the word pair
    options = [f"Number {i+1}. {pair[0]} versus {pair[1]}" for i, pair in enumerate(word_pairs)]
    selected_option = st.selectbox("Choose a word pair to hear the contrast:", options)
    
    # Function to generate audio
    def generate_contrast_audio(pair_description):
        tts = gTTS(text=pair_description, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    if st.button("Generate and Play Audio"):
        # Get the index from the selected option to find the correct word pair
        index = options.index(selected_option)
        pair_description = f"Number {index+1}. {word_pairs[index][0]} versus {word_pairs[index][1]}"
        audio_data = generate_contrast_audio(pair_description)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(pair_description)
# You can configure other tabs as needed
with tabs[2]:
    st.markdown("### 📒 Lesson 3: Tense and lax ‘u’ - suit vs. soot")
    
    # Using columns to place images side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/suit.jpg",
                 width=300, caption="Suit")
    with col2:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/soot.jpg",
                 width=300, caption="Soot")

    # List of sentences to choose from
    sentences_u = [
        "He is cleaning the suit damaged by the fire.",
        "He is cleaning the soot damaged by the fire."
    ]

    # Button to generate and play audio
    if st.button("Random Audio", key="audio_lesson3"):
        chosen_sentence_u = random.choice(sentences_u)
        tts = gTTS(text=chosen_sentence_u, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(chosen_sentence_u)

    st.markdown("#### A. Warming-up: Tense [ u ]")
    word_lists_u = {
        "Beginning": "None is available.",
        "Middle": "food, lose, knew, pool, loose, June, group, room, mood, truth, Tuesday, duty, school, suit",
        "End": "shoe, canoe, through, boo, you"
    }

    def generate_audio(word_list_u):
        words_with_pause = ' '.join([word + '...' for word in word_list_u.split(', ')])
        tts = gTTS(text=words_with_pause, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data

    col_beginning, col_middle, col_end = st.columns(3)
    with col_beginning:
        if st.button("Play words at the Beginning", key="begin_u"):
            audio_data = generate_audio(word_lists_u["Beginning"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_u["Beginning"])
    with col_middle:
        if st.button("Play words in the Middle", key="middle_u"):
            audio_data = generate_audio(word_lists_u["Middle"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_u["Middle"])
    with col_end:
        if st.button("Play words at the End", key="end_u"):
            audio_data = generate_audio(word_lists_u["End"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_u["End"])

    st.markdown("### B. Warming-up: Lax [ ʊ ]")
    lax_word_lists = {
        "Beginning": "No words begin with this vowel in English",
        "Middle": "cook, book, good, took, look, brook, stood, hood, woman, would, should, could, cookie, cushion, pudding, push, pull, bullet, wood",
        "End": "No words end with lax vowel in English"
    }

    col_beginning_lax, col_middle_lax, col_end_lax = st.columns(3)
    with col_beginning_lax:
        if st.button("Play words at the Beginning", key="begin_lax_u"):
            audio_data = generate_audio(lax_word_lists["Beginning"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(lax_word_lists["Beginning"])
    with col_middle_lax:
        if st.button("Play words in the Middle", key="middle_lax_u"):
            audio_data = generate_audio(lax_word_lists["Middle"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(lax_word_lists["Middle"])
    with col_end_lax:
        if st.button("No words at the End", key="end_lax_u"):
            audio_data = generate_audio(lax_word_lists["End"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(lax_word_lists["End"])

    st.markdown("### C. Contrast between tense and lax 'u'")
    word_pairs_u = [
        ("fool", "full"),
        ("suit", "soot"),
        ("Luke", "look"),
        ("pool", "pull"),
        ("wooed", "wood"),
        ("shoed", "should"),
        ("cooed", "could")
    ]
    
    options_u = [f"Number {i+1}. {pair[0]} versus {pair[1]}" for i, pair in enumerate(word_pairs_u)]
    selected_option_u = st.selectbox("Choose a word pair to hear the contrast:", options_u, key="contrast_u")
    
    def generate_contrast_audio(pair_description):
        tts = gTTS(text=pair_description, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    if st.button("Generate and Play Audio", key="contrast_audio_u"):
        index = options_u.index(selected_option_u)
        pair_description = f"Number {index+1}. {word_pairs_u[index][0]} versus {word_pairs_u[index][1]}"
        audio_data = generate_contrast_audio(pair_description)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(pair_description)


with tabs[3]:
    st.markdown("### 📒 Lesson 4: Vowel pair in ‘bed’ and ‘bad’")
     # Using columns to place images side-by-side
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/left.jpg",
                 width=300, caption="Image on the Left")
    with col2:
        st.image("https://github.com/MK316/Engpro-Class/raw/main/images/laughed.jpg",
                 width=300, caption="Image on the Right") 

    # List of sentences to choose from
    sentences_e = [
        "She finally left after hearing the unexpected news.",
        "She finally laughed after hearing the unexpected news."
    ]
    
    # Button to generate and play audio
    if st.button("Random Audio", key="audio_sentence_e"):
        # Randomly choose a sentence to be generated
        chosen_sentence_e = random.choice(sentences_e)
        
        # Generate speech using gTTS
        tts = gTTS(text=chosen_sentence_e, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
    
        # Display the audio player
        st.audio(audio_data.getvalue(), format='audio/mp3')
        
        # Display the sentence as caption below the audio
        st.caption(chosen_sentence_e)


    
    st.markdown("#### Articulation Tips")
    st.write("The [æ] vowel is articulated with a lower jaw position than the [ɛ] vowel.")
    
    st.markdown("#### A. Warming-up: [ɛ]")
    word_lists_e = {
        "Beginning": "end, egg, else, effort, elephant, extra, every, error",
        "Middle": "bed, next, west, bent, many, bread, yes, meant, measure",
        "End": "NA"
    }
    
    def generate_audio(word_list):
        words_with_pause = ' '.join([word + '...' for word in word_list.split(', ')])
        tts = gTTS(text=words_with_pause, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    col_beginning, col_middle, col_end = st.columns(3)
    with col_beginning:
        if st.button("Play words at the Beginning", key="begin_e"):
            audio_data = generate_audio(word_lists_e["Beginning"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_e["Beginning"])
    with col_middle:
        if st.button("Play words in the Middle", key="middle_e"):
            audio_data = generate_audio(word_lists_e["Middle"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_e["Middle"])
    with col_end:
        st.write("No words end with [ɛ] in English.")
    
    st.markdown("#### B. Warming-up: [æ]")
    word_lists_ae = {
        "Beginning": "and, apple, ask, action, absent, after, angry, animal",
        "Middle": "cat, back, black, have, map, cap, laugh, happy, last, class",
        "End": "NA"
    }
    
    col_beginning_ae, col_middle_ae, col_end_ae = st.columns(3)
    with col_beginning_ae:
        if st.button("Play words at the Beginning", key="begin_ae"):
            audio_data = generate_audio(word_lists_ae["Beginning"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_ae["Beginning"])
    with col_middle_ae:
        if st.button("Play words in the Middle", key="middle_ae"):
            audio_data = generate_audio(word_lists_ae["Middle"])
            st.audio(audio_data.getvalue(), format='audio/mp3')
            st.caption(word_lists_ae["Middle"])
    with col_end_ae:
        st.write("No words end with [æ] in English.")
    
    st.markdown("### C. Contrast between [ɛ] and [æ]")
    word_pairs_e_ae = [
        ("head", "had"),
        ("met", "mat"),
        ("pet", "pat"),
        ("lend", "land"),
        ("pest", "past (passed)"),
        ("ten", "tan"),
        ("said", "sad"),
        ("end", "and"),
        ("bed", "bad"),
        ("Ed", "add (ad)")
    ]
    
    options_e_ae = [f"Number {i+1}. {pair[0]} versus {pair[1]}" for i, pair in enumerate(word_pairs_e_ae)]
    selected_option_e_ae = st.selectbox("Choose a word pair to hear the contrast:", options_e_ae, key="contrast_e_ae")
    
    def generate_contrast_audio(pair_description):
        tts = gTTS(text=pair_description, lang='en')
        audio_data = io.BytesIO()
        tts.write_to_fp(audio_data)
        audio_data.seek(0)
        return audio_data
    
    if st.button("Generate and Play Audio", key="contrast_audio_e_ae"):
        index = options_e_ae.index(selected_option_e_ae)
        pair_description = f"Number {index+1}. {word_pairs_e_ae[index][0]} versus {word_pairs_e_ae[index][1]}"
        audio_data = generate_contrast_audio(pair_description)
        st.audio(audio_data.getvalue(), format='audio/mp3')
        st.caption(pair_description)
with tabs[4]:
    st.title("Listening practice")
    st.markdown("""
    - [Lesson 1](https://engpro-listening.streamlit.app/Lesson_01)
    - [Lesson 2](https://engpro-listening.streamlit.app/Lesson_02)
    """)
