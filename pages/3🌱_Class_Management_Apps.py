import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import qrcode
from PIL import Image
from wordcloud import WordCloud
import streamlit.components.v1 as components  # For embedding YouTube videos
from gtts import gTTS
import io
from io import BytesIO

    

# Function to create word cloud
def create_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    return wordcloud

# Streamlit tabs
tabs = st.tabs(["📈 QR", "⏳ Timer", "👥 Grouping", "🔊 Text-to-Speech", "⛅ Word Cloud", "🌀 TypeIPA","Name Caller"])

# QR Code tab
with tabs[0]:
    st.caption("QR code generator")

    # ✅ Place link input, caption input, and button in the same row
    col1, col2, col3 = st.columns([4, 2, 2])  # Adjust width ratios for better layout

    with col1:
        qr_link = st.text_input("📌 Enter URL link:", key="qr_link")
    with col2:
        caption = st.text_input("Enter a caption (optional):", key="qr_caption")
    with col3:
        st.write("")  # Add spacing for alignment
        generate_qr_button = st.button("🔆 Click to Generate QR", key="generate_qr")

    if generate_qr_button and qr_link:
        # ✅ Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_link)
        qr.make(fit=True)

        qr_img = qr.make_image(fill='black', back_color='white')

        # ✅ Convert the QR code image to RGB format and resize
        qr_img = qr_img.convert('RGB')
        qr_img = qr_img.resize((600, 600))

        # ✅ Display the QR code with caption
        st.image(qr_img, caption=caption if caption else "Generate", use_container_width=False, width=400)


# Timer tab
with tabs[1]:
    # Embed the Hugging Face space as an iframe
    huggingface_space_url = "https://MK-316-mytimer.hf.space"
    
    # Use Streamlit components to embed the external page
    st.components.v1.html(f"""
        <iframe src="{huggingface_space_url}" width="100%" height="600px" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """, height=600)

# ==============================
# Grouping tab
# ==============================
with tabs[2]:
    import pandas as pd
    from io import BytesIO

    st.subheader("👥 Grouping Tool")
    st.caption("Your csv file must have at least one column named as'Names.'")
    st.markdown(
        "[S25 Roster](https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/Engpro-roster25.csv)"
    )

    # ------------------------------
    # Helper: robust CSV reader
    # (handles UTF-8 / Korean encodings)
    # ------------------------------
    def read_csv_robust(uploaded_file):
        raw = uploaded_file.getvalue()

        for enc in ("utf-8", "utf-8-sig", "cp949", "euc-kr"):
            try:
                return pd.read_csv(BytesIO(raw), encoding=enc)
            except Exception:
                pass

        # fallback (raise error normally)
        return pd.read_csv(BytesIO(raw))

    # ------------------------------
    # Upload section
    # ------------------------------
    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

    members_per_group = st.number_input(
        "Members per Group",
        min_value=1,
        value=5
    )

    fixed_groups_input = st.text_input(
        "Fixed Groups (separated by semicolon;)",
        placeholder="Name1, Name2; Name3, Name4"
    )

    # ------------------------------
    # Grouping function
    # ------------------------------
    def group_names(file, members_per_group, fixed_groups_input):

        df = read_csv_robust(file)

        if "Names" not in df.columns:
            st.error("CSV must contain a column named 'Names'.")
            return None

        fixed_groups = [
            g.strip() for g in fixed_groups_input.split(";") if g.strip()
        ]

        fixed_groups_df_list = []
        remaining_df = df.copy()

        # Process fixed groups
        for group in fixed_groups:
            group_names_list = [
                name.strip() for name in group.split(",") if name.strip()
            ]

            matched_rows = remaining_df[
                remaining_df["Names"].isin(group_names_list)
            ]

            fixed_groups_df_list.append(matched_rows)

            remaining_df = remaining_df[
                ~remaining_df["Names"].isin(group_names_list)
            ]

        # Shuffle remaining students
        remaining_df = remaining_df.sample(frac=1).reset_index(drop=True)

        # Fill fixed groups to required size
        for i, group_df in enumerate(fixed_groups_df_list):
            while len(group_df) < members_per_group and not remaining_df.empty:
                group_df = pd.concat(
                    [group_df, remaining_df.iloc[[0]]],
                    ignore_index=True
                )
                remaining_df = remaining_df.iloc[1:].reset_index(drop=True)

            fixed_groups_df_list[i] = group_df

        # Create remaining groups
        groups = fixed_groups_df_list

        for i in range(0, len(remaining_df), members_per_group):
            groups.append(remaining_df.iloc[i:i + members_per_group])

        # Determine max group size
        max_group_size = max(len(g) for g in groups) if groups else 0

        # Build output dataframe
        grouped_data = {
            "Group": [f"Group {i+1}" for i in range(len(groups))]
        }

        for i in range(max_group_size):
            grouped_data[f"Member{i+1}"] = [
                g["Names"].tolist()[i] if i < len(g) else ""
                for g in groups
            ]

        return pd.DataFrame(grouped_data)

    # ------------------------------
    # Run grouping
    # ------------------------------
    if st.button("Submit"):
        if uploaded_file is None:
            st.error("Please upload a CSV file before submitting.")
        else:
            grouped_df = group_names(
                uploaded_file,
                members_per_group,
                fixed_groups_input
            )

            if grouped_df is not None:
                st.write(grouped_df)

                # ------------------------------
                # Excel download (NO encoding issues)
                # ------------------------------
                output = BytesIO()

                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    grouped_df.to_excel(
                        writer,
                        index=False,
                        sheet_name="Groups"
                    )

                output.seek(0)

                st.download_button(
                    label="Download Grouped Names as Excel (.xlsx)",
                    data=output,
                    file_name="grouped_names.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )

# Grouping tab
# with tabs[2]:
#     st.subheader("👥 Grouping Tool")
#     st.caption("Your csv file must have 'Names' column")
#     st.markdown("[Spring 2026 Roster](https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/data/engpro-roster-260224.csv)")

#     # Upload file section
#     uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    
#     # User input for group size
#     members_per_group = st.number_input("Members per Group", min_value=1, value=5)
    
#     # Input for fixed groups (optional)
#     fixed_groups_input = st.text_input("Fixed Groups (separated by semicolon;)", placeholder="Name1, Name2; Name3, Name4")

#     # Submit button to trigger grouping process
#     if st.button("Submit"):
#         if uploaded_file is not None:
#             # Function to group names
#             def group_names(file, members_per_group, fixed_groups_input):
#                 # Read the CSV file
#                 df = pd.read_csv(file)

#                 # Parse fixed groups input
#                 fixed_groups = [group.strip() for group in fixed_groups_input.split(';') if group.strip()]
#                 fixed_groups_df_list = []
#                 remaining_df = df.copy()

#                 # Process fixed groups and create a list for additional members to be added
#                 for group in fixed_groups:
#                     group_names = [name.strip() for name in group.split(',') if name.strip()]
#                     # Find these names in the DataFrame
#                     matched_rows = remaining_df[remaining_df['Names'].isin(group_names)]
#                     fixed_groups_df_list.append(matched_rows)
#                     # Remove these names from the pool of remaining names
#                     remaining_df = remaining_df[~remaining_df['Names'].isin(group_names)]

#                 # Shuffle the remaining DataFrame
#                 remaining_df = remaining_df.sample(frac=1).reset_index(drop=True)
                
#                 # Adjusting fixed groups to include additional members if they're under the specified group size
#                 for i, group_df in enumerate(fixed_groups_df_list):
#                     while len(group_df) < members_per_group and not remaining_df.empty:
#                         group_df = pd.concat([group_df, remaining_df.iloc[[0]]])
#                         remaining_df = remaining_df.iloc[1:].reset_index(drop=True)
#                     fixed_groups_df_list[i] = group_df  # Update the group with added members

#                 # Grouping the remaining names
#                 groups = fixed_groups_df_list  # Start with adjusted fixed groups
#                 for i in range(0, len(remaining_df), members_per_group):
#                     groups.append(remaining_df[i:i + members_per_group])

#                 # Determine the maximum group size
#                 max_group_size = max(len(group) for group in groups)
                
#                 # Creating a new DataFrame for grouped data with separate columns for each member
#                 grouped_data = {'Group': [f'Group {i+1}' for i in range(len(groups))]}
#                 # Add columns for each member
#                 for i in range(max_group_size):
#                     grouped_data[f'Member{i+1}'] = [group['Names'].tolist()[i] if i < len(group) else "" for group in groups]

#                 grouped_df = pd.DataFrame(grouped_data)
                
#                 return grouped_df

#             # Call the group_names function and display the grouped names
#             grouped_df = group_names(uploaded_file, members_per_group, fixed_groups_input)
            
#             # Display the grouped names
#             st.write(grouped_df)
            
#             # Option to download the grouped names as CSV
#             csv = grouped_df.to_csv(index=False).encode('utf-8')
#             st.download_button(
#                 label="Download Grouped Names as CSV",
#                 data=csv,
#                 file_name='grouped_names.csv',
#                 mime='text/csv',
#             )

#         else:
#             st.error("Please upload a CSV file before submitting.")

# Text-to-Speech tab
with tabs[3]:
    st.subheader("Text-to-Speech Converter (using Google TTS)")
    text_input = st.text_area("Enter the text you want to convert to speech:")
    language = st.selectbox("Choose a language: 🇰🇷 🇺🇸 🇬🇧 🇷🇺 🇫🇷 🇪🇸 🇮🇹 🇯🇵 ", ["Korean", "English (American)", "English (British)", "Russian", "Spanish", "French", "Italian", "Japanese"])

    tts_button = st.button("Convert Text to Speech")
    
    if tts_button and text_input:
        # Map human-readable language selection to language codes and optionally to TLDs for English
        lang_codes = {
            "Korean": ("ko", None),
            "English (American)": ("en", 'com'),
            "English (British)": ("en", 'co.uk'),
            "Russian": ("ru", None),
            "Spanish": ("es", None),
            "French": ("fr", None),
            "Italian": ("it", None),
            "Chinese": ("zh-CN", None),
            "Japanese": ("ja", None)
        }
        language_code, tld = lang_codes[language]

        # Assuming you have a version of gTTS that supports tld or you have modified it:
        # This check ensures that the tld parameter is only used when not None.
        if tld:
            tts = gTTS(text=text_input, lang=language_code, tld=tld, slow=False)
        else:
            tts = gTTS(text=text_input, lang=language_code, slow=False)
        
        speech = io.BytesIO()
        tts.write_to_fp(speech)
        speech.seek(0)

        # Display the audio file
        st.audio(speech.getvalue(), format='audio/mp3')

    st.markdown("---")
    st.caption("🇺🇸 English text: Teacher-designed coding applications create tailored learning experiences, making complex concepts easier to understand through interactive and adaptive tools. They enhance engagement, provide immediate feedback, and support active learning.")
    st.caption("🇰🇷 Korean text: 교사가 직접 만든 코딩 기반 애플리케이션은 학습자의 필요에 맞춘 학습 경험을 제공하고, 복잡한 개념을 쉽게 이해하도록 돕습니다. 또한 학습 몰입도를 높이고 즉각적인 피드백을 제공하며, 능동적인 학습을 지원합니다.")
    st.caption("🇫🇷 French: Les applications de codage conçues par les enseignants offrent une expérience d'apprentissage personnalisée, rendant les concepts complexes plus faciles à comprendre grâce à des outils interactifs et adaptatifs. Elles améliorent l'engagement, fournissent un retour immédiat et soutiennent l'apprentissage actif.")
    st.caption("🇷🇺 Russian: Созданные учителями кодированные приложения предлагают персонализированный опыт обучения, упрощая понимание сложных концепций с помощью интерактивных и адаптивных инструментов. Они повышают вовлеченность, предоставляют мгновенную обратную связь и поддерживают активное обучение.")
    st.caption("🇨🇳 Chinese: 由教师设计的编程应用程序为学习者提供个性化的学习体验，通过互动和适应性工具使复杂的概念更容易理解。它们增强学习参与度，提供即时反馈，并支持主动学习。")
    st.caption("🇯🇵 Japanese: 教師が設計したコーディングアプリケーションは、学習者のニーズに合わせた学習体験を提供し、複雑な概念をインタラクティブで適応性のあるツールを通じて理解しやすくします。また、学習への集中力を高め、即時フィードバックを提供し、主体的な学習をサポートします。")
      

# Word Cloud tab
with tabs[4]:
    st.subheader("🌌 Word Cloud Generator")

    # Input text for generating the word cloud
    user_input = st.text_area("Enter text to generate a word cloud:")

    # Button to generate the word cloud
    if st.button("Generate Word Cloud"):
        if user_input.strip():
            # Generate word cloud only when there is valid input
            wordcloud = create_wordcloud(user_input)
            fig, ax = plt.subplots()
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis("off")
            st.pyplot(fig)
        else:
            st.warning("Please enter some text to generate a word cloud.")
with tabs[5]:
    st.caption("https://ipa.typeit.org/")
    
    # URL you want to embed
    url_to_embed = "https://ipa.typeit.org/"
    
    # Embed the URL using an iframe
    components.iframe(url_to_embed, width=600, height=600, scrolling=True)

with tabs[6]:

   
    # Function to generate audio from text
    def text_to_speech(text):
        tts = gTTS(text, lang='en')  # Correct language code if needed
        audio_buffer = BytesIO()
        tts.write_to_fp(audio_buffer)
        audio_buffer.seek(0)
        return audio_buffer
    
    def main():
        st.title("😍 Name Caller")
        st.markdown("### Teacher's Talk")
        intro = text_to_speech("Calling will begin shortly. Please listen to your name and respond with 'Present'.")
        st.audio(intro, format='audio/mp3')
    
        st.write("1. Roll call (Male teacher)")
        roster_audio1 = "https://github.com/MK316/Engpro-Class/raw/main/audio/roll-call-S25.mp3"
        st.audio(roster_audio1, format='audio/mp3')
    
        st.write("2. Roll call (Female teacher)")
        roster_audio2 = "https://github.com/MK316/Engpro-Class/raw/main/audio/roll-call-S25-F.mp3"
        st.audio(roster_audio2, format='audio/mp3')
        
        # User selects the CSV file column for names
        url = "https://raw.githubusercontent.com/MK316/Engpro-Class/main/data/s25engpro-roster2.csv"
        data = pd.read_csv(url)
        # st.write("Data columns:", data.columns)  # This will display the actual column names for debugging
    
        # Let the user choose which column of names to use, ensuring the exact case from the data
        name_column = st.radio("Choose which names to call:", ('Names', 'ENames'))
    
        # Check if the selected column exists in the DataFrame to avoid KeyErrors
        if name_column in data.columns:
            names = data[name_column].tolist()
    
            # Initialize or reset the name ID (nid) using Streamlit's session state
            if 'nid' not in st.session_state or st.button("Reset Counter"):
                st.session_state.nid = 1  # Resets or initializes the counter
    
            if st.button("Start Calling Names"):
                for name in names:
                    st.write(f"Now calling: {st.session_state.nid}")
                    audio_response = text_to_speech(name)
                    st.audio(audio_response, format='audio/mp3')
                    st.session_state.nid += 1  # Increment nid in the session state
        else:
            st.error(f"Selected column '{name_column}' does not exist in the data.")
    
    if __name__ == "__main__":
        main()
