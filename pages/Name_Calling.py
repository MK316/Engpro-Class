import pandas as pd
import streamlit as st

def load_names(url):
    data = pd.read_csv(url)
    return data['Names'].tolist()

def main():
    st.title("Class Name Caller")
    st.markdown("### Teacher's Talk")
    st.markdown("🔊 Calling will begin shortly. Please listen to your name and respond with 'Present'.")

    # GitHub raw URL of the CSV file
    url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/data/Engpro-roster25.csv"

    try:
        names = load_names(url)
        if st.button("Start Calling Names"):
            for name in names:
                # Assuming you have a function to handle the text-to-speech generation
                st.write(f"Now calling: {name}")
                # Additional code for text-to-speech would go here
    except Exception as e:
        st.error(f"Failed to load names: {e}")

if __name__ == "__main__":
    main()
