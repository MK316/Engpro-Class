import streamlit as st

tab1, tab2, tab3 = st.tabs(["Lesson", "Past tense form -ed", "APP"])

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

with tab2:
    st.markdown("### 📘 Past Tense Form: -ed Pronunciation")
    st.markdown("""
    The past tense ending **-ed** can be pronounced in three different ways in English:

    - /t/ as in **washed**
    - /d/ as in **played**
    - /ɪd/ as in **wanted**
    """)

with tab3:
    st.markdown("### ⚙️ Interactive App Coming Soon")
    st.write("This section will include a pronunciation practice tool for voicing contrasts.")
