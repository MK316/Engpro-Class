import streamlit as st
import requests
import calendar
from datetime import datetime
from PIL import Image
import os


# CSS to adjust the alignment of the dropdown to match the buttons
st.markdown("""
    <style>
    .stSelectbox div[data-baseweb="select"] {
        margin-top: -30px;  /* Adjust this value to align with the buttons */
    }
    </style>
    """, unsafe_allow_html=True)

# Set up the path to the slides folder
slides_path = "pages/intro_slides/"  # Ensure this is correct relative to your app's location
slide_files = sorted([f for f in os.listdir(slides_path) if f.endswith(".png")])
num_slides = len(slide_files)

# Initialize session state variables if they do not exist

# Initialize session state variables if they do not exist
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0  # Start with the first slide

# Check if there are slides in the folder
if num_slides == 0:
    st.error("No slides found in the specified folder.")
    st.stop()  # Stop the app if there are no slides
# Function to load and display the image based on the current index with resizing
def display_image():
    slide_path = os.path.join(slides_path, slide_files[st.session_state.slide_index])
    image = Image.open(slide_path)
    
    # Set your desired width for resizing
    desired_width = 1200  # Adjust this value as needed
    aspect_ratio = image.height / image.width
    new_height = int(desired_width * aspect_ratio)
    resized_image = image.resize((desired_width, new_height))

    st.image(resized_image, caption=f"Slide {st.session_state.slide_index + 1} of {num_slides}")




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
tabs = st.tabs(["🍐 Course Overview", "Intro_Slides", "🍓 Schedule", "💙 Padlet", "🍏 Evaluation", "🍒 Assignments", "📆 Calendar"])

# Content for the Course Overview tab
with tabs[0]:
    st.caption("🔎 Course Overview")
    
    st.markdown("""
    <div class="justify-text">

    This course is specifically designed for future English teachers, aiming to enhance their English language proficiency with an emphasis on developing clear and intelligible pronunciation. It includes a series of targeted activities that improve speaking and listening skills, complemented by a variety of authentic materials such as TED Talks and online videos, enhanced by digital resources and advanced AI technologies.
    </div>
    """, unsafe_allow_html=True)
    st.audio("https://github.com/MK316/Engpro-Class/raw/main/audio/engpro-overview1.mp3", format='audio/mp3')
    
    st.markdown("""
    <div class="justify-text">
    The curriculum provides an in-depth study of English linguistic features, focusing on pronunciation. Instruction covers the International Phonetic Alphabet (IPA) and the importance of stress and intonation in communication. Practical applications complement this theoretical knowledge, fostering a holistic approach to mastering English pronunciation.
    </div>
    """, unsafe_allow_html=True)
    st.audio("https://github.com/MK316/Engpro-Class/raw/main/audio/engpro-overview2.mp3", format='audio/mp3')
    
    st.markdown("""
    <div class="justify-text">
    Assignments are crafted to reinforce learned concepts and encourage the development of teaching methodologies. By the course's end, participants will not only master English pronunciation but also be equipped with effective strategies to teach these skills in various educational settings.
    </div>
    """, unsafe_allow_html=True)
    st.audio("https://github.com/MK316/Engpro-Class/raw/main/audio/engpro-overview3.mp3", format='audio/mp3')
    
##############################
with tabs[1]:

    # Arrange 'Start', 'Previous', 'Next', and 'Slide Selector' in a single row
    col1, col2, col3, col4 = st.columns([1, 1, 1, 5])
    
    with col1:
        if st.button("⛳", key="start", help="Reset to the first slide"):
            st.session_state.slide_index = 0

    with col2:
        if st.button("◀️", key="previous", help="Go back to the previous slide"):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
            else:
                st.warning("This is the first slide.")

    with col3:
        if st.button("▶️", key="next", help="Go to the next slide"):
            if st.session_state.slide_index < num_slides - 1:
                st.session_state.slide_index += 1
            else:
                st.warning("Final slide")

    with col4:
        # Display slide selector dropdown
        selected_slide = st.selectbox("",
                                      options=[f"Slide {i + 1}" for i in range(num_slides)],
                                      index=st.session_state.slide_index)

        # Update slide index if dropdown selection changes
        selected_slide_index = int(selected_slide.split()[-1]) - 1
        if selected_slide_index != st.session_state.slide_index:
            st.session_state.slide_index = selected_slide_index

    # Display the image
    display_image()



##############################
# Content for the Schedule tab
with tabs[2]:
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

with tabs[3]:
    st.header("🐾 Files to share: on Padlet")
    st.write("This Padlet serves as a dynamic hub for our Acoustics course. Here, you'll find additional course materials, additional reading resources, and online tools. It's also a space for sharing files and submitting assignments.")
    st.components.v1.iframe("https://padlet.com/mirankim316/S25Engpro", width=700, height=800)


# Content for the Evaluation tab
with tabs[4]:
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
with tabs[5]:
    st.header("Assignments")
    st.write("List and detail the assignments for the course here, providing due dates and submission guidelines.")
    # Bulleted List using Markdown
    st.markdown("""
    - HW#1: Recording (diagnosis)
    - HW#2: Transcript searching
    - HW#3: Recording (presentation)
    - HW#4: Song practice
    - HW#5: Final recording
    """)
    st.caption("Details will be announced in time.")

# Content for the Calendar tab
with tabs[6]:
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

