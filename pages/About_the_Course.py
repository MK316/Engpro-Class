import streamlit as st
import requests

# Create tabs for different sections of the course
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Course Overview", "Schedule", "Evaluation", "Assignments", "Links"])

# Content for the Course Overview tab
with tab1:
    st.header("Course Overview")
    st.write("Here you can provide a general description of the course, including its objectives, learning outcomes, and any prerequisites.")

# Content for the Schedule tab
with tab2:
    st.caption("Spring 2025")
    # URL of the raw markdown file on GitHub
    markdown_url = "https://github.com/MK316/Engpro-Class/blob/main/README.md"
    #https://raw.githubusercontent.com/MK316/Engpro-Class/refs/heads/main/README.md
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
with tab3:
    st.header("Evaluation")
    st.write("Describe the evaluation criteria and grading methods. Include information on exams, projects, participation, etc.")

# Content for the Assignments tab
with tab4:
    st.header("Assignments")
    st.write("List the assignments for the course here. Provide due dates, requirements, submission guidelines, etc.")

# Content for the Downloads tab
with tab5:
    st.header("Links")
    st.write("Provide online resources here. This could include syllabi, lecture slides, reading materials, additional resources, etc.")
