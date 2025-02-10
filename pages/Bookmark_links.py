import streamlit as st

def main():
    st.title('English Pronunciation Practice Resources')

    st.header('Welcome to English Pronunciation Practice Links!')
    st.subheader('Explore the resources below') 
    st.write("to improve your English pronunciation skills.")

    # Dictionary of useful links and their descriptions
    resources = {
        "🔎 YouGlish": {
            "url": "https://youglish.com/",
            "description": "Use YouTube videos to practice pronunciation in context and see how words are used in real-life speeches."
        },
        "🔎 Minimal Pairs Practice": {
            "url": "https://www.englishclub.com/pronunciation/minimal-pairs.htm",
            "description": "Interactive exercises to help you master minimal pairs and improve your ability to distinguish between similar sounds."
        },
        "BBC Learning English": {
            "url": "https://www.bbc.co.uk/learningenglish/english/features/pronunciation",
            "description": "Provides a wide range of activities and video lessons to help you improve your English pronunciation."
        },
        "Rachel's English": {
            "url": "https://rachelsenglish.com/",
            "description": "Offers comprehensive videos focusing on American English pronunciation, including the nuances of phonetic sounds."
        },
        "English Club Pronunciation": {
            "url": "https://www.englishclub.com/pronunciation/",
            "description": "Features lessons and advice on different aspects of English pronunciation, suitable for all levels."
        }
    }

    # Display links and descriptions
    for name, info in resources.items():
        st.markdown(f"##### {name}")
        st.markdown(f"[Visit the site]({info['url']})")
        st.markdown(info['description'])
        st.write(" ")  # Add some space between entries

if __name__ == "__main__":
    main()
