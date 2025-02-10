import streamlit as st

def main():
    st.title('Online Resources')
    
    # Create tabs
    tab1, tab2, tab3 = st.tabs(["Online materials", "Digital tools", "Pronunciation Lessons"])
    
    with tab1:
        st.header('Welcome!')
        st.subheader('Begin Your Journey Here')
        st.write("Discover how you can improve your English pronunciation skills with our curated resources and tips.")

    with tab2
        st.header('Additional Resources')
        st.subheader('Further Explore')
        st.write("Check out more tools and guides to assist you in advancing your English language skills.")
        st.markdown("Here you can find extra materials, webinars, and community forums to support your learning journey.")
    
    
    with tab3:
        st.header('Explore the resources below')
        st.write("to improve your English pronunciation skills.")
        st.markdown("---")
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
