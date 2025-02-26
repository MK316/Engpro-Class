import streamlit as st
import webbrowser
import requests
import pandas as pd
import io  # ✅ Fixed StringIO issue



# Function to load wordlist data
@st.cache_data
def load_wordlist(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for invalid requests

        # ✅ Fixed: Using io.StringIO instead of pd.compat.StringIO
        df = pd.read_csv(io.StringIO(response.text), sep='\t', usecols=['SID', 'WORD'], dtype=str)

        # Strip whitespace and convert SID to integer
        df.columns = df.columns.str.strip()
        df['SID'] = df['SID'].str.extract('(\d+)')[0].astype(int)  # Extract numbers and convert
        df['WORD'] = df['WORD'].str.strip()  # Clean up words

        return df
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        return pd.DataFrame(columns=["SID", "WORD"])  # Return empty DataFrame on error



def main():
    st.title('Online Resources')
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["💻 Online links", "Oxford5K", " 📌 Digital tools" ,"🍒 Customized apps","💿 More web resources"])
    
    with tab1:
        st.header('Classroom Connections')
        st.write("Web links frequently used in class")
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
            "🌈 TED": {
                "url": "https://ted.com",
                "description": "Listen to public talks (& Choose your final presentation)"
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
        st.caption("🔎 The B2 and C1 word lists contain a total of 725 and 1,380 words, respectively. Select the word numbers you want, then click the Show button.")
        
        # Custom button with a link
        app_url = "https://mk316voca.streamlit.app/"
        button_html = f"""
        <a href="{app_url}" target="_blank">
            <button style='color: white; background-color: #2ca02c; border: none; border-radius: 5px; padding: 10px 20px; text-align: center; display: inline-block; font-size: 16px;'>
                Go to CEFR Voca Application
            </button>
        </a>
        """
        st.markdown(button_html, unsafe_allow_html=True)
        
        st.markdown("---")


        # Load wordlist

        # URLs for wordlists
        urls = "🍐 Wordlist B2": "https://raw.githubusercontent.com/MK316/CEFR/refs/heads/main/data/B2.txt"      
        wordlist = load_wordlist(url)

        if not wordlist.empty:
            total_words = len(wordlist)  # Get total words in the wordlist
            
            # User selects SID range
            col1, col2 = st.columns(2)
            with col1:
                start_sid = st.number_input(f"From SID (Total: {total_words} words)", min_value=1, max_value=wordlist['SID'].max(), value=1)
            with col2:
                end_sid = st.number_input(f"To SID (Total: {total_words} words)", min_value=start_sid, max_value=wordlist['SID'].max(), value=min(start_sid+19, wordlist['SID'].max()))

            # Filter selected range
            filtered_words = wordlist[(wordlist['SID'] >= start_sid) & (wordlist['SID'] <= end_sid)].reset_index(drop=True)

            # ✅ "Show Words" Button with number of selected words
            num_selected = len(filtered_words)
            if st.button(f"🔍 Show {num_selected} Words", key=f"show_words_{idx}"):
                st.table(filtered_words.set_index("SID"))

        else:
            st.error("No data available for this wordlist.")
    with tab3:
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
    
    with tab4:
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

        
    with tab5:
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
