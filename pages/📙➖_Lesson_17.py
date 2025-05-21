import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO


# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["❄️ Lesson", "❄️ Past tense form -ed", "❄️ [t, d] Flapping/Tapping", "❄️ [t, d] Glottalization"])


# --- Load data from GitHub ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/tapping_dataB.csv"
    df = pd.read_csv(url, encoding="utf-8-sig")
    return df
    
df = load_data()


# --- Tab 1: Consonant Lesson ---
with tab1:
    st.markdown("### 📙 Lesson 17. [p/b, t/d, k/g]")

    st.markdown("""
#### [1] Individual Sounds

Pronouncing [p/b, t/d, k/g] sounds is usually not a problem for Korean speakers.  
However, English has specific consonant rules that affect how voiceless sounds behave:

- After the /s/ sound (e.g., **spy**, **skate**, **steam**), voiceless sounds may lose their aspiration.  
- In unstressed syllables, consonants can sound weaker or different than expected.

Compare the following word pairs:
""")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Strong Onset")
        st.write("• pie")
        st.write("• Kate")
        st.write("• team")

    with col2:
        st.subheader("After /s/")
        st.write("• spy")
        st.write("• skate")
        st.write("• steam")

# --- Tab 2: -ed Pronunciation ---
with tab2:
    st.markdown("### 📘 Past Tense Form: -ed Pronunciation")
    st.markdown("""
The past tense ending **-ed** can be pronounced in three different ways in English:

- [t] as in **washed**
- [d] as in **played**
- [ɪd] as in **wanted**
""")

# --- Tab 3: Placeholder ---
with tab3:
    st.markdown("### 🔤 What is the Tapping Rule in English?")
    st.markdown("🐳 [APPs4U](https://apps4u.streamlit.app/): TCE Samples")
    
    st.markdown("""
    The **tapping rule** (also known as **flapping**) is a common pronunciation feature in **American English**.  
    It occurs when the sounds **/t/** and **/d/** between two vowels are pronounced as a quick, soft **tap**, similar to a fast **[d]** sound.
    """)
    
    st.markdown("#### ✅ Examples:")
    
    st.markdown("""
    | Spelling     | Regular Pronunciation | Tap Pronunciation | Sounds Like |
    |--------------|------------------------|-------------------|-------------|
    | **butter**   | [ˈbʌtər]               | [ˈbʌɾər]          | *budder*    |
    | **ladder**   | [ˈlædər]               | [ˈlæɾər]          | *ladder*    |
    | **writer**   | [ˈraɪtər]              | [ˈraɪɾər]         | *rider*     |
    | **pretty**   | [ˈprɪti]               | [ˈprɪɾi]          | *priddy*    |
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📌 When Does Tapping Happen?")
    st.markdown("""
    Tapping usually happens when:
    1. A **/t/** or **/d/** comes **between two vowels**
    2. The **second syllable is unstressed**
    3. The **/t/** or **/d/** is **not at the start or end** of a word
    """)

    st.write("water, better, cutter, grader, greater, spider, autumn, monitor, humanity, comedy, competing, etc.")
    
    st.markdown("#### 🛑 When It Doesn’t Happen:")
    st.markdown("""
    - If the **second syllable is stressed** (e.g., *attack*)  
    - Or the **/t/** is at the **beginning or end** of the word
    """)
    
    st.markdown("#### 📚 Summary")
    st.markdown("""
    The tapping rule helps make your pronunciation sound more **natural** and **fluent** in American English.  
    It doesn’t change meaning, but it makes speech smoother and more native-like.
    """)
######################
    st.markdown("---")
    st.markdown("Tapping practice app: with Level B vocabulary")


    
    # --- Initialize session state ---
    if "selected_target" not in st.session_state:
        st.session_state.selected_target = None
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "user_response" not in st.session_state:
        st.session_state.user_response = None
    if "show_word" not in st.session_state:
        st.session_state.show_word = False
    if "show_feedback" not in st.session_state:
        st.session_state.show_feedback = False
    
    # --- Title for Tab 3 ---
    st.title("🔁 Tapping Practice")
    
    # --- Target selection buttons ---
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔵 T"):
            st.session_state.selected_target = "T"
            st.session_state.current_index = 0
            st.session_state.show_word = False
            st.session_state.show_feedback = False
    with col2:
        if st.button("🔴 D"):
            st.session_state.selected_target = "D"
            st.session_state.current_index = 0
            st.session_state.show_word = False
            st.session_state.show_feedback = False
    
    # --- Filter and interact if a target is selected ---
    if st.session_state.selected_target:
        target_df = df[df["Target"] == st.session_state.selected_target].reset_index(drop=True)
        total_words = len(target_df)
        st.markdown(f"### 📌 There are **{total_words}** words to practice.")
    
        if st.button("🎯 Show a word"):
            st.session_state.show_word = True
            st.session_state.show_feedback = False
            st.session_state.user_response = None
    
        if st.session_state.show_word and st.session_state.current_index < total_words:
            current_word = target_df.loc[st.session_state.current_index, "WORD"]
            tapping_truth = target_df.loc[st.session_state.current_index, "Tapping"]
    
            # Display the word
            st.markdown(f"<h1 style='font-size: 64px; text-align: center;'>{current_word}</h1>", unsafe_allow_html=True)
    
            # Generate and play audio
            tts = gTTS(current_word)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format="audio/mp3")
    
            # Ask tapping question
            st.markdown("**Is tapping possible?**")
            st.session_state.user_response = st.radio(
                "Choose one:", ["YES", "NO", "YES/NO", "NO/YES"], index=0, key=f"radio_{st.session_state.current_index}"
            )
    
            if st.button("✅ Show Feedback"):
                st.session_state.show_feedback = True
    
            if st.session_state.show_feedback:
                # Convert "YES"/"NO" in dataset to match option
                expected = "YES" if tapping_truth.strip().upper() == "YES" else "NO"
                if expected in st.session_state.user_response:
                    st.success("🎉 Correct!")
                else:
                    st.error("❗ Try again.")
    
            # Next word button
            if st.button("➡️ Next Word"):
                if st.session_state.current_index + 1 < total_words:
                    st.session_state.current_index += 1
                    st.session_state.show_word = True
                    st.session_state.show_feedback = False
                    st.session_state.user_response = None
                else:
                    st.info("✅ You've completed all words.")
                    st.session_state.current_index = 0
                    st.session_state.show_word = False
                    st.session_state.show_feedback = False
                    st.session_state.user_response = None



#####################
with tab4:
    st.markdown("### Glottalization: /t, d/ becomes a glottal stop sound [ʔ]")
    st.markdown("""
    
    + In English, /t, d/ sounds are pronouned as though there is no consonant at all. However, a consonant [ʔ], produced in the throuat, is indeed made. This sound is akin to the noise one might make when speaking suddenly with surprise, like 'uh'.

    + Where do we find this sound? For example, /t/ or /d/ sound before vowel in unstressed syllables when followed by /n/, as in 'button'.

    + Examples: written, eaten, mountain, captain, curtain, Manhattan, wooden, forbidden, hidden, etc.
    
    """)

    st.caption("Note that it is not necessary for learners to produce this sound actively, but you will often hear it. Thus, recognizing it aid word recognition. For listening skills, understanding this rule in English is important.")
