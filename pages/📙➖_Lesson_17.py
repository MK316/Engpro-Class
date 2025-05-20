import streamlit as st

# Create tabs
tab1, tab2, tab3 = st.tabs(["Lesson", "Past tense form -ed", "[t, d] Flapping/Tapping"])

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

- /t/ as in **washed**
- /d/ as in **played**
- /ɪd/ as in **wanted**
""")

# --- Tab 3: Placeholder ---
with tab3:
    st.markdown("### 🔤 What is the Tapping Rule in English?")
    
    st.markdown("""
    The **tapping rule** (also known as **flapping**) is a common pronunciation feature in **American English**.  
    It occurs when the sounds **/t/** and **/d/** between two vowels are pronounced as a quick, soft **tap**, similar to a fast **/d/** sound.
    """)
    
    st.markdown("#### 🧠 In simple terms:")
    st.markdown("When **/t/** or **/d/** is between two vowel sounds, it sounds like a soft, quick **/d/** — this is called a **tap**.")
    
    st.markdown("#### ✅ Examples:")
    
    st.markdown("""
    | Spelling     | Regular Pronunciation | Tap Pronunciation | Sounds Like |
    |--------------|------------------------|-------------------|-------------|
    | **butter**   | /ˈbʌtər/               | /ˈbʌɾər/          | *budder*    |
    | **ladder**   | /ˈlædər/               | /ˈlæɾər/          | *ladder*    |
    | **writer**   | /ˈraɪtər/              | /ˈraɪɾər/         | *rider*     |
    | **pretty**   | /ˈprɪti/               | /ˈprɪɾi/          | *priddy*    |
    """, unsafe_allow_html=True)
    
    st.markdown("#### 📌 When Does Tapping Happen?")
    st.markdown("""
    Tapping usually happens when:
    1. A **/t/** or **/d/** comes **between two vowels**
    2. The **second syllable is unstressed**
    3. The **/t/** or **/d/** is **not at the start or end** of a word
    """)
    
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
