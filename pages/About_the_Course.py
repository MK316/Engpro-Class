import streamlit as st
import requests
import calendar
from datetime import datetime

# Include custom CSS to justify text in the markdown
# Include custom CSS to justify text in the markdown
st.markdown("""
<style>
.justify-text p {
    text-align: justify;
    text-justify: inter-word;
}
.calendar-table {
    margin-left: auto;
    margin-right: auto;
    border-collapse: collapse;
}
.calendar-table td, .calendar-table th {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Create tabs for different sections of the course
tabs = st.tabs(["🍐 Course Overview", "🍓 Schedule", "🍏 Evaluation", "🍒 Assignments", "🍋 Links", "📆 Calendar"])

# Content for the Course Overview tab
with tabs[0]:
    st.caption("🔎 Course Overview")
    
    st.markdown("""
    <div class="justify-text">

    This course is specifically designed for future English teachers, aiming to enhance their English language proficiency with an emphasis on developing clear and intelligible pronunciation. It includes a series of targeted activities that improve speaking and listening skills, complemented by a variety of authentic materials such as TED Talks and online videos, enhanced by digital resources and advanced AI technologies.
    
    The curriculum provides an in-depth study of English linguistic features, focusing on pronunciation. Instruction covers the International Phonetic Alphabet (IPA) and the importance of stress and intonation in communication. Practical applications complement this theoretical knowledge, fostering a holistic approach to mastering English pronunciation.

    Assignments are crafted to reinforce learned concepts and encourage the development of teaching methodologies. By the course's end, participants will not only master English pronunciation but also be equipped with effective strategies to teach these skills in various educational settings.
    </div>
    """, unsafe_allow_html=True)

# Content for the Schedule tab
with tabs[1]:
    st.caption("Spring 2025")
    # URL of the raw markdown file on GitHub
    markdown_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/pages/readme.md"
    
    try:
        response = requests.get(markdown_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        markdown_content = response.text
        st.markdown(markdown_content, unsafe_allow_html=True)
    except requests.exceptions.HTTPError as err:
        st.error(f"Failed to retrieve Markdown content: {err}")
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        
# Content for the Evaluation tab
with tabs[2]:
    st.header("Evaluation")
    st.write("This section outlines the evaluation criteria and methods, such as grading rubrics, tests, projects, and participation requirements.")
    # Bulleted List using Markdown
    st.markdown("""
    - 5 Homeworks (20%)
    - Written midterm (40%)
    - Final presentation (30%)
    - Attendance & Class Participation (15%)
    """)
    st.caption("Students can earn up to 105% in total, with an additional 5% available through extra credit.")
# Content for the Assignments tab
with tabs[3]:
    st.header("Assignments")
    st.write("List and detail the assignments for the course here, providing due dates and submission guidelines.")
    # Bulleted List using Markdown
    st.markdown("""
    - HW#1: Recording (diagnosis)
    - HW#2: Transcript searching
    - HW#3: Song practice
    - HW#4: Recording (diagnosis)
    - HW#5: Final recording
    """)
    st.caption("Details will be announced in time.")
# Content for the Links tab
with tabs[4]:
    st.header("Links")
    st.write("Provide useful links here. This could include additional reading materials, online resources, and related external websites.")

# Content for the Calendar tab
with tabs[5]:
    # Dropdown for selecting a month
    month_option = st.selectbox("Select a Month", options=["March", "April", "May", "June"], index=0)
    # Dictionary to map month names to their corresponding numbers
    month_to_number = {"March": 3, "April": 4, "May": 5, "June": 6}
    # Get selected month number
    month_number = month_to_number[month_option]
    year = 2025  # Define the year

    # Define a list of holidays as tuples (day, month)
    holidays = [
        (1, 3),  # Example: March 1
        (3, 3),  # Example: May 25
        (5, 5),
        (6, 5),
        (6, 6)
        # Add more holidays as needed
    ]

    # Generate the calendar for the selected month
    cal = calendar.monthcalendar(year, month_number)

    # Display the calendar as a table using HTML
    cal_html = "<table class='calendar-table'><thead><tr>"
    cal_html += "".join(f"<th>{day}</th>" for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
    cal_html += "</tr></thead><tbody>"

    for week in cal:
        cal_html += "<tr>"
        for day in week:
            if day == 0:  # Empty cell for days outside the month
                cal_html += "<td></td>"
            else:
                # Check if the day is a holiday
                if (day, month_number) in holidays:
                    cal_html += f"<td style='color: red; font-weight: bold;'>{day}</td>"
                else:
                    cal_html += f"<td>{day}</td>"
        cal_html += "</tr>"
    cal_html += "</tbody></table>"

    st.markdown(cal_html, unsafe_allow_html=True)

