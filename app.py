from pathlib import Path

import streamlit as st
from PIL import Image


#Path settings
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles"/"main.css"
resume_file = current_dir /"assets" / "CV.pdf"
profile_pic = current_dir /"assets" / "profile-pic.png"



#general settings
PAGE_TITLE ="Digital CV | Gaurav Bansode"
PAGE_ICON =":wave:"
NAME ="Gaurav Bansode"
DESCRIPTION="""Crafting Code with Precision and Passion """
EMAIL ="bansodegaurav97@gmail.com"
SOCIAL_MEDIA ={
    "LinkedIn":"- www.linkedin.com/in/gauravb2603",
    "GitHub":"- https://github.com/Gaurav-Bansode-07",
}

PROJECTS ={
    "🏆Online Toy Shop"  : "https://github.com/Gaurav-Bansode-07/Online-Toy-Shop",

     "🏆Online Bag Shopping" : "https://github.com/Gaurav-Bansode-07/Online-Bag-Shopping"

    #   "XYZ   : XYZ"
    #    "XYZ   : XYZ"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# load css, pdf and profile pic

with open(css_file)as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
    profile_pic=Image.open(profile_pic)

    #hero section

    col1, col2 = st.columns(2, gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume" ,
            data= PDFbyte,   
            file_name=resume_file.name, 
            mime="application/octet-stream",
        )
        st.write("📧", EMAIL)

        #social links

        st.write("#")
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]{link}")
        

        #experience and qualifications

        st.write("#")
        st.subheader("Experience & Qualifications")
        st.write(
            """
        - ✔ A Recent Computer Science graduate with a CGPA of 8.85
        - ✔ Skilled in Python, Java, JavaScript, and SQL.
        - ✔ Experienced in web development with HTML, CSS, PHP
        - ✔ Committed to continuous learning and active participation

"""
        )


        #skills

        st.write("#")
        st.subheader("Hard Skills")
        st.write(
            """
        - Python
        - Java
        - Html
        - Css
        - Sql
        - Javascript
        - Data Science
        - Artificial Intelligence
        - Computer Networks
        - Pandas
        - Numpy
        - Matplotlib

"""
        )



        #projects and accomplishments

        st.write("#")
        st.subheader("Projects & Accomplishments")
        st.write("---")
        for project, link in PROJECTS.items():
            st.write(f"[{PROJECTS}]({link})")