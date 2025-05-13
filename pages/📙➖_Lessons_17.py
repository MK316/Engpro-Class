import streamlit as st

tab1, tab2, tab3 = st.tabs(["Lesson", "Past tense form -ed", "APP"])

with tab1:
  st.markdown("### 📙 Lesson 17. [p/b, t/d, k/g]")

  st.markdown("""
  #### [1] Individual sounds

  Pronouncing [p/b, t/d, k/g] sounds is not a problem for Koreans. However, we need to learn a consonant rule in English that changes the quality of the voiceless sounds after /s/, and when they are located in unstressed syllables.
  """)
  
    col1, col2 = st.columns(2)

    with col1:
        st.write("pie")
        st.write("Kate")
        st.write("team")

    with col2:
        st.write("spy")
        st.write("skate")
        st.write("steam") 

with tab2:
  st.markdown("### Past tense form -ed pronunciaiton")
  
with tab3:
  st.markdown("### TBA")
