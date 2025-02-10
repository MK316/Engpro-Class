import streamlit as st
import webbrowser

def main():
    st.title('Online Resources')
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs(["💻 Online materials", " 📌 Digital tools" ,"🍒 Customized apps","💿 Pronunciation Lessons"])
    
    with tab1:
        st.header('Classroom Connections')
        st.write("Web links commonly used")
        st.markdown("---")
        # Dictionary of useful links and their descriptions
        resources = {
            "🔎 GNU LMS": {
                "url": "https://rec.ac.kr/gnu",
                "description": "GNU 학습시스템"
            },
            "🔎 Padlet for activities": {
                "url": "https://padlet.com/mirankim316/S25Engpro",
                "description": "Files to upload and share"
            },
            "Dictionary.com": {
                "url": "https://dictionary.com",
                "description": "Online dictionary."
            }
        }

        # Display links and descriptions
        for name, info in resources.items():
            st.markdown(f"##### {name}")
            st.markdown(f"[Visit the site]({info['url']})")
            st.markdown(info['description'])
            st.write(" ")  # Add some space between entries


    with tab2:
        st.header('Digital & AI tools')
        st.write("Get familiar with digital tools online")
        st.markdown("---")
        # Dictionary of useful links and their descriptions
        resources = {
            "🔎 YouGlish": {
                "url": "https://youglish.com/",
                "description": "Use YouTube videos to practice pronunciation in context and see how words are used in real-life speeches."
            },
            "🔎 Speechnotes": {
                "url": "https://speechnotes.co",
                "description": "a web-based voice recognition tool that transforms speech into text, perfect for students and professionals."
            },
            "🔎 Elevenlabs": {
                "url": "https://elevenlabs.io",
                "description": "A voice synthesis platform that enables realistic and customizable voice generation for various applications."
            }
        }

        # Display links and descriptions
        for name, info in resources.items():
            st.markdown(f"##### {name}")
            st.markdown(f"[Visit the site]({info['url']})")
            st.markdown(info['description'])
            st.write(" ")  # Add some space between entries
    
with tab3:
    st.header('Explore More Applications')
    st.subheader('Check out these tools to enhance your learning experience:')
    
    # Button for the first application with a blue color
    if st.button('Go to Speechnotes', key='btn1', on_click=None, args=None, kwargs=None, help=None, disabled=False, label_visibility="visible"):
        st.write('You are redirected to Speechnotes.')
        st.experimental_singleton('https://speechnotes.co')

    # Button for the second application with a green color
    if st.button('Visit ElevenLabs', key='btn2', on_click=None, args=None, kwargs=None, help=None, disabled=False, label_visibility="visible"):
        st.write('You are redirected to ElevenLabs.')
        st.experimental_singleton('https://elevenlabs.io')

    # Button for the third application with a red color
    if st.button('Access BBC Learning', key='btn3', on_click=None, args=None, kwargs=None, help=None, disabled=False, label_visibility="visible"):
        st.write('You are redirected to BBC Learning English.')
        st.experimental_singleton('https://www.bbc.co.uk/learningenglish')

    # Custom CSS to style the buttons
    st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
        }
        div.stButton > button:nth-child(2) {
            background-color: #2196F3;
            color: white;
        }
        div.stButton > button:nth-child(3) {
            background-color: #f44336;
            color: white;
        }
        </style>""", unsafe_allow_html=True)

    with tab4:
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
