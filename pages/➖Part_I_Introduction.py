import streamlit as st

# Create four tabs
tabs = st.tabs(["📗 Basics 1", "📗 Basics 2", "📗 Basics 3", "📗 Basics 4"])

# Content for each tab
with tabs[0]:
    st.markdown("### Basics 1: Understanding English Sounds")

    # GitHub raw URLs for the MP3 files with descriptions
    audio_files = {
        "1. Unique set of sounds:": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-01.mp3",
            "desc": "Every language has its own unique set of sounds. When learning a second language, the first step is figuring out which sounds are familiar—similar to the ones in our native language—and which ones are completely new. Once we know that, we can focus on practicing the new sounds by learning how to shape our mouth and move our tongue in the right way."
        },
        "2. Speech gestures...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-02.mp3",
            "desc": "Even small changes in how we shape our mouth or move our tongue can make a big difference in how sounds are produced and understood. These changes might completely change the meaning of a word, make speech sound accented, or sometimes have no effect on the actual sounds—but they can still impact things like tone and expressiveness. "
        },
        "3. How we approach...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-03.mp3",
            "desc": "In this course, we'll learn how to pronounce individual English sounds by understanding how they’re made and practicing them. We’ll also work on putting sounds together to form words and using tone and rhythm to communicate naturally with English speakers."
        },
        "4. Letters and sounds...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-04.mp3",
            "desc": "Here's a question: Do we really need to learn IPA symbols? Isn't knowing how to spell words enough? Note that English spelling can be pretty tricky—it often doesn't tell us much about how words are actually pronounced. For example, let's take the word sigh. How many letters does it have? Now, how many different sounds do you hear?"
        },
    }

    # Display each title with description and playable audio
    for title, data in audio_files.items():
        st.subheader(title)
        st.write(data["desc"])  # Add description under each title
        st.audio(data["url"], format="audio/mp3")

    # Button to show the worksheet image
    if st.button("🎯 Show: 1. Example worksheet"):
        worksheet_url = "https://github.com/MK316/Engpro-Class/raw/main/images/P1-04example.png"
        st.image(worksheet_url, caption="Example Worksheet (p.14)", use_container_width=True)

    
with tabs[1]:
    st.markdown("### Symbols (IPA) to represent English vowels")


    # Button to show the worksheet image
    if st.button("🎯 Show: 1. English vowels (IPA symbols)"):
        worksheet_url01 = "https://github.com/MK316/Engpro-Class/raw/main/images/P1-vowelchart.png"
        st.image(worksheet_url01, caption="Example Worksheet (p.15)", use_container_width=True)
    st.write("Note: Vowel sounds and stress can also vary depending on the region.")  
    st.caption("Vowel example: daughter, coffee, law, house, etc.")
    st.caption("Stress example: a.  Caˈribbean (AE)	b.  ˌCaribˈbean (BE)")

    if st.button("🎯 Show: 2. Video showing different pronunciation b/w American and British"):
        youtube_url = "https://www.youtube.com/watch?v=DKEM-juLxmM"
        st.video(youtube_url)

    
with tabs[2]:
    st.markdown("### Symbols (IPA) to represent English consonants")

    if st.button("🎯 Show: 3. English consonants (IPA symbols)"):
        worksheet_url02 = "https://github.com/MK316/Engpro-Class/raw/main/images/P1-consonantchart.png"
        st.image(worksheet_url02, caption="Example Worksheet (p.16)", use_container_width=True)
    if st.button("🎯 Show: 4. English consonants (Additional IPA symbols)"):
        worksheet_url03 = "https://github.com/MK316/Engpro-Class/raw/main/images/P1-consonantchart2.png"
        st.image(worksheet_url03, caption="Example Worksheet (p.16)", use_container_width=True)

with tabs[3]:
    st.markdown("### Dictionaries for pronunciation?")

    # GitHub raw URLs for the MP3 files with descriptions
    audio_files = {
        "Getting help from dictioinaries:": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/P1-05.mp3",
            "desc": "If you don’t have someone to help you with English pronunciation in person, you’ll need a good reference. Most dictionaries give some basic info on how to pronounce words, but their pronunciations don’t always match what you hear in everyday speech. That’s because sounds change depending on the words around them and the way people actually speak. So, think of a dictionary pronunciation guide as just that—a guide. It’s based on certain rules, but real-world pronunciation can be more flexible:"
        },
        "1) The symbols...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/p18-02.mp3",
            "desc": "1) The symbols in a dictionary represent one possible pronunciation when words are pronounced in isolation (also known as the citation form or emphasized form). For this reason, some dictionaries may present more than one pronunciation form, including variations that account for dialectal differences."
        },
        "2) When and how individual sounds change...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/p18-03.wav",
            "desc": "You'll learn when and how individual sounds are subject to change according to the sound rules in English. Let's take English tapping rule, for example. The /t/ sound may become a tap or flap in most American English speech when it occurs between two vowels, with the second vowel being unstressed. e.g., butter, heater, beater, better, and letter; cutter, Peter, meter, creator, and waiter."
        },
        "3) Examples of dictionary pronunciation symbols...": {
            "url": "https://github.com/MK316/Engpro-Class/raw/main/audio/p18-03.wav",
            "desc": "You'll learn when and how individual sounds are subject to change according to the sound rules in English. Let's take English tapping rule, for example. The /t/ sound may become a tap or flap in most American English speech when it occurs between two vowels, with the second vowel being unstressed. e.g., butter, heater, beater, better, and letter; cutter, Peter, meter, creator, and waiter."
        },
      
    }

    # Display each title with description and playable audio
    for title, data in audio_files.items():
        st.subheader(title)
        st.write(data["desc"])  # Add description under each title
        st.audio(data["url"], format="audio/mp3")

    if st.button("🎯 Show: Dictionary transcription of words"):
        worksheet_url04 = "https://github.com/MK316/Engpro-Class/raw/main/images/p19-01.png"
        st.image(worksheet_url04, caption="Example Worksheet (p.19)", use_container_width=True)
