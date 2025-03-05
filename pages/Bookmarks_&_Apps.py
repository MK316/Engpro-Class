import streamlit as st
import webbrowser
import requests
import pandas as pd
import io  # ✅ Fixed StringIO issue



# ✅ Load wordlist from GitHub
@st.cache_data
def load_wordlist(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails

        # Read as DataFrame
        df = pd.read_csv(io.StringIO(response.text), sep='\t', usecols=['SID', 'WORD', 'POS'], dtype=str)

        # Clean and convert SID to integer
        df.columns = df.columns.str.strip()
        df['SID'] = df['SID'].str.extract('(\d+)')[0].astype(int)
        df['WORD'] = df['WORD'].str.strip()  # Remove extra spaces

        return df
    except Exception as e:
        st.error(f"❌ Failed to load data: {e}")
        return pd.DataFrame(columns=["SID", "WORD"])

# ✅ URLs for wordlists
wordlist_url1 = "https://raw.githubusercontent.com/MK316/CEFR/refs/heads/main/data/B2.txt"
wordlist_url2 = "https://raw.githubusercontent.com/MK316/CEFR/refs/heads/main/data/C1f.txt"

def main():
    st.title('Bookmarks & Apps')
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🔆 Weblinks", "🌈 Oxford5K", "🌈 Padlet", " 🔆 Digital tools" ,"🔆 Customized apps","🔆 More web resources"])
    
    with tab1:

        # Dictionary of useful links and their descriptions
        resources = {
            "🔎 GNU LMS": {
                "url": "https://rec.ac.kr/gnu",
                "description": "GNU 학습시스템"
            },
            "🌈 TED": {
                "url": "https://ted.com",
                "description": "Listen to public talks (& Choose your final presentation)"
            },
            "Dictionary.com": {
                "url": "https://dictionary.com",
                "description": "Online dictionary."
            },
            "👫 Grouping - Google sheet": {
                "url": "https://docs.google.com/spreadsheets/d/1vi-wOJEFpXNWInfcKEZKqiuNFzOQtib5_1R3qyT6N9E/edit?usp=sharing",
                "description": "Engpro Grouping."
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
    
        # ✅ Custom-styled blue button for external CEFR Voca Application
        button_html = """
        <style>
            .blue-button {
                background-color: #99004C; /* Bootstrap Blue */
                color: white !important;
                border: none;
                border-radius: 8px;
                padding: 12px 20px;
                font-size: 16px;
                font-weight: bold;
                text-decoration: none !important;
                display: inline-block;
                text-align: center;
                width: auto;
            }
            .blue-button:hover {
                background-color: #0056b3; /* Darker Blue */
            }
            .blue-button a {
                color: white !important;
                text-decoration: none !important;
            }
        </style>
        <a href="https://mk316voca.streamlit.app/" target="_blank" class="blue-button">Go to Voca Application: Practice with Sound</a>
        """
        st.markdown(button_html, unsafe_allow_html=True)

    
        st.markdown("---")
    
        # ✅ Selection for Level B or Level C
        level_choice = st.radio("🔍 Select a Wordlist Level:", ["📗 Level B (B2)", "📕 Level C (C1)"], key="wordlist_selection")
    
        # Assign the correct dataset based on selection
        if level_choice == "🍐 Level B (B2)":
            wordlist_url = wordlist_url1
            level_key = "b2"
        else:
            wordlist_url = wordlist_url2
            level_key = "c1"
    
        # ✅ Load wordlist
        wordlist = load_wordlist(wordlist_url)
    
        if not wordlist.empty:
            total_words = len(wordlist)  # Get total words in the wordlist
            
            # ✅ User selects SID range
            col1, col2 = st.columns(2)
            with col1:
                start_sid = st.number_input(f"From SID (Total: {total_words} words)", min_value=1, max_value=wordlist['SID'].max(), value=1, key=f"start_sid_{level_key}")
            with col2:
                end_sid = st.number_input(f"To SID (Total: {total_words} words)", min_value=start_sid, max_value=wordlist['SID'].max(), value=min(start_sid+19, wordlist['SID'].max()), key=f"end_sid_{level_key}")
    
            # ✅ Filter selected range
            filtered_words = wordlist[(wordlist['SID'] >= start_sid) & (wordlist['SID'] <= end_sid)].reset_index(drop=True)
    
            # ✅ "Show Words" Button with number of selected words
            num_selected = len(filtered_words)
            if st.button(f"🔍 Show {num_selected} Words", key=f"show_words_{level_key}_{start_sid}"):
                st.table(filtered_words.set_index("SID"))
    
        else:
            st.error("❌ No data available for this wordlist.")

    with tab3:
        st.markdown("#### 🐾 Class activities and assignment submission: on Padlet")
        st.caption("This Padlet serves as a dynamic hub for class activities. Secure submissions will be managed through the LMS.")
        st.markdown("To access the page, click 🌀 [here](https://padlet.com/mirankim316/S25Engpro)")
        st.components.v1.iframe("https://padlet.com/mirankim316/S25Engpro", width=700, height=800)
    
    with tab4:
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
    
    with tab5:
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

        
    with tab6:
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
