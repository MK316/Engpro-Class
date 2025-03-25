import streamlit as st
import pandas as pd

# Create a tab bar with three tabs
tab1, tab2, tab3 = st.tabs(["🎱 Assignments", "👬 Group info", "🌵 Padlet"])


with tab1:
    st.markdown("### 📝 Individual Assignments Details")

    # Sample data for the assignments table
    data = {
        "Assignment": ["HW#1: Pre-recording", "HW#2: TED selection", "HW#3: 1 min's video recording", "HW#4: Hey Jude", "HW#5: TBA"],
        "Due Date": ["2025-03-09", "2025-03-18", "2025-04-22", "2025-04-10", "2025-04-15"],
        "Status": ["Closed", "Closed", "Open", "TBA", "TBA"],
        "Grade": ["Complete/Incomplete", "C / I", "4 pts.", "4 pts.", "4 pts."],
        "Submission": ["[LMS](https://rec.ac.kr/gnu)", "[Google Sheet](https://docs.google.com/spreadsheets/d/1vi-wOJEFpXNWInfcKEZKqiuNFzOQtib5_1R3qyT6N9E/edit?usp=sharing)", "[Padlet](https://padlet.com/mirankim316/S25Engpro)", "[Padlet](https://padlet.com/mirankim316/S25Engpro)", "TBA"],
        "Notes":["","","","",""]
    }

    # Convert the dictionary into a DataFrame
    assignments_df = pd.DataFrame(data)

    # Display the DataFrame as a table in Streamlit
    st.table(assignments_df.set_index("Assignment"))

    st.markdown("### 📝 Group Assignments Details")
    
    g_data = {
        "Assignment": ["1. Voca study (Level B & C)", "2: Help 1 min. TED recording"],
        "Due Date": ["2025-04-29", "2025-04-22"],
        "Status": ["Open", "Open"],
        "Grade": ["Complete/Incomplete", "C / I"],
        "Submission": ["[Google Sheet](https://docs.google.com/spreadsheets/d/1vi-wOJEFpXNWInfcKEZKqiuNFzOQtib5_1R3qyT6N9E/edit?usp=sharing)", "Padlet"],
        "Notes":["",""]
    }

    # Convert the dictionary into a DataFrame
    g_assignments_df = pd.DataFrame(g_data)

    # Display the DataFrame as a table in Streamlit
    st.table(g_assignments_df.set_index("Assignment"))
with tab2:
    st.markdown("### 1. [Groups](https://docs.google.com/spreadsheets/d/1vi-wOJEFpXNWInfcKEZKqiuNFzOQtib5_1R3qyT6N9E/edit?usp=sharing)")

with tab3:
    st.header("🐾 Files to share: on Padlet")
    st.write("This Padlet serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/S25Engpro", width=700, height=800)
