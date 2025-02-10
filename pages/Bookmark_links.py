import streamlit as st

def main():
    st.title('English Pronunciation Practice Resources')

    st.header('Welcome to English Pronunciation Practice Links!')
    st.subheader('Explore the resources below to improve your English pronunciation skills.')

    # List of useful links
    resources = {
        "BBC Learning English": "https://www.bbc.co.uk/learningenglish/english/features/pronunciation",
        "YouGlish": "https://youglish.com/",
        "Rachel's English": "https://rachelsenglish.com/",
        "English Club Pronunciation": "https://www.englishclub.com/pronunciation/",
        "Minimal Pairs Practice": "https://www.englishclub.com/pronunciation/minimal-pairs.htm"
    }

    # Display links
    for name, url in resources.items():
        st.markdown(f"[{name}]({url}) - Click to visit")

if __name__ == "__main__":
    main()
