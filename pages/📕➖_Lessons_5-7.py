import streamlit as st

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

