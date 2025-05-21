import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO


# Create tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["❄️ Lesson", "❄️ Past tense form -ed", "❄️ [t, d] Flapping/Tapping", "❄️ [t, d] Glottalization", "🍰 APPS"])




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
    




with tab4:
    st.markdown("### Glottalization: /t, d/ becomes a glottal stop sound [ʔ]")
    st.markdown("""
    
    + In English, /t, d/ sounds are pronouned as though there is no consonant at all. However, a consonant [ʔ], produced in the throuat, is indeed made. This sound is akin to the noise one might make when speaking suddenly with surprise, like 'uh'.

    + Where do we find this sound? For example, /t/ or /d/ sound before vowel in unstressed syllables when followed by /n/, as in 'button'.

    + Examples: written, eaten, mountain, captain, curtain, Manhattan, wooden, forbidden, hidden, etc.
    
    """)

    st.caption("Note that it is not necessary for learners to produce this sound actively, but you will often hear it. Thus, recognizing it aid word recognition. For listening skills, understanding this rule in English is important.")

with tab5:
    st.write("Applications")
    st.markdown("#### 📚 Tapping Practice with Level B vocabulary")
    st.markdown("👉 [APP1: Tapping practice](https://tapping-level-b.streamlit.app/)")
    st.markdown("👉 [APP2: -ed pronunciation practice](https://ed-pronunciation.streamlit.app/)")
