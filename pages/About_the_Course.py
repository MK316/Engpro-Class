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
    markdown_url = "https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/README.md"
    
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

# Content for the Assignments tab
with tabs[3]:
    st.header("Assignments")
    st.write("List and detail the assignments for the course here, providing due dates, submission guidelines, and grading criteria.")

# Content for the Links tab
with tabs[4]:
    st.header("Links")
    st.write("Provide useful links here. This could include additional reading materials, online resources, and related external websites.")

with tabs[5]:
    st.header("Calendar")
    # Dropdown for selecting a month
    month_option = st.selectbox("Select a Month", options=["March", "April", "May", "June"], index=0, format_func=lambda x: datetime.strptime(x, '%B').strftime('%B'))
    # Dictionary to map month names to their corresponding numbers
    month_to_number = {"March": 3, "April": 4, "May": 5, "June": 6}
    # Get selected month number
    month_number = month_to_number[month_option]
    # Generate the calendar for the selected month
    year = 2025  # Define the year
    cal = calendar.monthcalendar(year, month_number)
    # Display the calendar as a markdown
    cal_str = f"### {month_option} {year}\n" + '\n'.join(['| ' + ' | '.join(f"{day:2}" if day != 0 else '  ' for day in week) + ' |' for week in cal])
    st.markdown(cal_str)
    st.markdown("""|Su|Mo|Tu|We|Th|Fr|Sa|
|---|---|---|---|---|---|---|""")
