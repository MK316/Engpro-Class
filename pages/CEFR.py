import streamlit as st
import pandas as pd

# Load your dataset
@st.cache_data
def load_data():
    return pd.read_csv("/pages/cefr_levelB.csv")  # Replace with your actual filename

# Load data
df = load_data()

# Create tabs
tab1, tab2, tab3 = st.tabs(["🔤 Vowel Flashcard", "📘 App 2", "📗 App 3"])

# --- Tab 1: Flashcard App ---
with tab1:
    st.header("🔤 Vowel Flashcard App")

    # User input
    user_input = st.text_input("Enter a word to look up:", "").strip().lower()

    # Search and display
    if user_input:
        matched = df[df['WORD'].str.lower() == user_input]

        if not matched.empty:
            for _, row in matched.iterrows():
                with st.container():
                    st.markdown("---")
                    st.markdown(f"### **{row['WORD']}**")
                    st.markdown(f"**Part of Speech:** {row['POS']}")
                    st.markdown(f"**Vowel Type:** {row['Vowel_Type']}")
                    st.markdown(f"**Stressed Vowel:** `{row['Stressed_Vowel']}`")
        else:
            st.warning("No matching word found.")

# --- Tab 2 Placeholder ---
with tab2:
    st.header("📘 App 2")
    st.write("You can implement a different app here.")

# --- Tab 3 Placeholder ---
with tab3:
    st.header("📗 App 3")
    st.write("You can implement another app here.")
