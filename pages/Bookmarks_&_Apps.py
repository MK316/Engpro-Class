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
        st.header('Customized Applications')
        # CSS to style the markdown links as buttons
        button_style = """
        <style>
            a.button_link {
                display: inline-block;
                text-align: center;
                background-color: #009999;
                color: white;
                padding: 10px 20px;
                text-decoration: none;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            a.button_link:hover {
                background-color: #FF7878;
            }
        </style>
        """
    
        # Apply the CSS
        st.markdown(button_style, unsafe_allow_html=True)
    
        # Creating clickable markdown buttons
        st.markdown('<a href="https://mk-316-accuracyfeedback.hf.space" class="button_link" target="_blank">🍋 App 1: Accuracy Feedback</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-tts-pitch.hf.space" class="button_link" target="_blank">🍐 App 2: Intonation contour</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-foreignaccent.hf.space" class="button_link" target="_blank">🐼 App 3: Foreign accent examples</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://https://mk-316-pronunciationfeedback.hf.space/" class="button_link" target="_blank">📝 App 4: Pronunciation Feedback</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-korean-english.hf.space" class="button_link" target="_blank">🎧 App 5: Loanword English Pronunciation</a>', unsafe_allow_html=True)
        st.markdown('<a href="https://mk-316-oxford5k.hf.space" class="button_link" target="_blank">🐇 App 6: Oxford 5K Vocabulary practice</a>', unsafe_allow_html=True)

        
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
