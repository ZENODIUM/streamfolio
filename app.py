import streamlit as st
import pandas as pd

st.set_page_config(page_title="My Portfolio", page_icon=":star:", layout="wide")

main_image = "logo.png"

with st.sidebar:
    st.title("Streamfolio")
    st.image("logo.png")
    selection = st.radio("Navigate to:", ["Home", "Projects", "Skills & Experience", "Contact"], label_visibility="collapsed")
    st.write("---")
    with open("resume.pdf", "rb") as file:
        st.download_button(label="📄 Download Resume", data=file, file_name="resume.pdf", mime="application/pdf")
    st.write("Rate my site")
    selected = st.feedback("stars")
    if selected is not None:
        st.markdown(f"Thank You for rating")

def home():
    st.title("Welcome to My Streamfolio")
    st.subheader("Hello! I am Code with monk")
    col1, col2 = st.columns(2)
    col1.image(main_image, use_container_width=True, caption="Code with monk")
    col1.write(
        '''I am a dedicated Data Scientist with a strong foundation in machine learning, data analysis, 
        and web development. Over the past five years, I have developed expertise in Python, SQL, and cloud platforms 
        like AWS, allowing me to work effectively across the data pipeline. I am particularly passionate about applying AI.'''
    )
    about_me_data = {
        "Data": ["Name","email","location","Hobbies"],
        "About me": ["Monk","monk@gmail.com","New York","Painting"]
    }
    col2.table(pd.DataFrame(about_me_data).set_index("Data"))
    new_york_location = pd.DataFrame({"lat": [40.7128], "lon": [-74.0060]})
    col2.map(new_york_location)

def projects():
    st.title("Projects")
    col1, col2, col3 = st.columns(3)
    col1.subheader("Project 1")
    col1.image(main_image, use_container_width=True)
    col1.write("Description of Project 1")
    selected_1 = col1.feedback("thumbs", key="project1_feedback")
    col2.subheader("Project 2")
    col2.image(main_image, use_container_width=True)
    col2.write("Description of Project 2")
    selected_2 = col2.feedback("thumbs", key="project2_feedback")
    col3.subheader("Project 3")
    col3.image(main_image, use_container_width=True)
    col3.write("Description of Project 3")
    selected_3 = col3.feedback("thumbs", key="project3_feedback")

def skills_and_experience():
    st.title("Skills & Experience")
    skilloption = st.selectbox("Skill Set", ("Programming languages", "Frameworks", "Cloud"))
    if skilloption == "Programming languages":
        skill_levels = {"Python": 90, "Java": 70}
    elif skilloption == "Frameworks":
        skill_levels = {"Angular": 30, "Django": 50}
    else:
        skill_levels = {"AWS": 90, "Azure": 80}
    for skill, level in skill_levels.items():
        st.write(f"{skill}")
        st.progress(level / 100)
    st.write("### Experience Timeline (2020-2024)")
    years = ["2020", "2021", "2022", "2023", "2024"]
    education = [0.5, 1, 1.5, 2,2]
    internships = [0, 0, 0.5, 1,1]
    jobs = [0, 0, 1, 1, 2]
    timeline_data = pd.DataFrame({
        "Year": years,
        "University Y": education,
        "Company A": internships,
        "Company B": jobs
    }).set_index("Year")
    st.line_chart(timeline_data)

def contact():
    st.title("Contact")
    st.write("### Let's connect!")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send")
    if submit_button:
        st.success(f"Thank you, {name}! Your message has been sent.")
    st.write("### Or find me on:")
    st.link_button("💼 Linkedin", "https://streamlit.io/gallery")
    st.link_button("💻 Github", "https://streamlit.io/gallery")

if selection == "Home":
    home()
elif selection == "Projects":
    projects()
elif selection == "Skills & Experience":
    skills_and_experience()
elif selection == "Contact":
    contact()

st.sidebar.write("---")
