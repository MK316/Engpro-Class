import streamlit as st
import pandas as pd

# Create a tab bar with three tabs
tab1, tab2 = st.tabs(["🎱 Group info", "🎾 Assignments"])

with tab1:
    st.markdown("### Grouping")
    st.markdown("#### [Oxford5K voca](https://docs.google.com/spreadsheets/d/1vi-wOJEFpXNWInfcKEZKqiuNFzOQtib5_1R3qyT6N9E/edit?usp=sharing)"

with tab2:
    st.markdown("### 📝 Assignments Details")

    # Sample data for the assignments table
    data = {
        "Assignment": ["HW#1: Pre-recording", "HW#2: TED selection", "HW#3: 1 min's video recording", "HW#4: Hey Jude", "HW#5: TBA"],
        "Due Date": ["2025-03-09", "2025-03-18", "2025-04-22", "2025-04-10", "2025-04-15"],
        "Status": ["Closed", "Closed", "Open", "TBA", "TBA"],
        "Grade": ["Complete/Incomplete", "C / I", "4 pts.", "4 pts.", "4 pts."],
        "Submission": ["LMS", "Google Sheet", "Padlet", "Padlet", "TBA"],
        "Remark":["","","","",""]
    }

    # Convert the dictionary into a DataFrame
    assignments_df = pd.DataFrame(data)

    # Display the DataFrame as a table in Streamlit
    st.table(assignments_df.set_index("Assignment"))
