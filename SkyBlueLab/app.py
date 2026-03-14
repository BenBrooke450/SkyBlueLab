

import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os
import streamlit.components.v1 as components

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))




import sys
from pathlib import Path

folder_a_path = Path(__file__).resolve().parent.parent

if str(root_path) not in sys.path:
    sys.path.insert(0, str(root_path))

from BlueOcean.ocean_app import run_ocean





choice = option_menu(
    menu_title=None,
    options=["HOME", "OCEAN", "PROJECTS", "RESEARCH & CERTIFICATES"],
    icons=["flower1", "tsunami", "bi bi-floppy-fill", "file-earmark-person"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "#007BFF", "font-size": "25px"},
        "nav-link": {"font-size": "0px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#e0f2ff"},
    }
)


if choice == "HOME":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png",width=75)
        st.title("Home Information")
        st.header("Benjamin Brooke")
        st.subheader("Data Scientist & AI Engineer")
        col1, col2, col3 = st.columns(3)


        with col1:
            st.markdown("""
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
                
                <div style="
                    border:2px solid #ccc;
                    padding:20px;
                    border-radius:15px;
                    width:100px;
                    text-align:center;
                    ">
                
                <a href="https://github.com/BenBrooke450" target="_blank">
                    <i class="fa-brands fa-square-github" style="font-size:40px; color:grey; margin-right:0px;"></i>
                </a>
                
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

                    <div style="
                        border:2px solid #ccc;
                        padding:20px;
                        border-radius:15px;
                        width:100px;
                        text-align:center;
                        ">

                    <a href="https://www.linkedin.com/in/benjamin-brooke-097063159/">
                        <i class="fa-brands fa-linkedin" style="font-size:40px; color:grey;"></i>
                    </a>

                    </div>
                    """, unsafe_allow_html=True)




    st.header("Welcome to the SkyBlueLab")
    st.write("Senior Data Scientist with 5+ years of experience building ETL pipelines and 2+ years building ML systems for clinical research. Specialised in clinical NLP, distributed data pipelines (PySpark, Databricks), and deep learning with PyTorch. Deployed production ML systems that improved clinical data processing efficiency and decision support. Experienced in building end-to-end ML pipelines, including feature engineering, model training, deployment, and monitoring.")


elif choice == "OCEAN":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png", width=75)
        st.title("Ocean Blue")
        if "science_auth" not in st.session_state:
            st.session_state.science_auth = False

        if not st.session_state.science_auth:
            st.write("OceanBlue Restricted: Please Enter Pin")
            pin = st.text_input("Enter Code", type="password")

            if st.button("Unlock"):
                if pin == "2026":
                    st.session_state.science_auth = True
                    st.rerun()
                else:
                    st.error("Hmm... Invalid Code")
        else:
            if st.button("Log Out of Science Hub"):
                st.session_state.science_auth = False
                st.rerun()

            run_ocean()

    st.header("OceanBlue")
    st.write("This is my personal LLM, please use the tab on the left for access")

elif choice == "PROJECTS":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png", width=75)
        st.success("All Systems Nominal")

    st.write("Projects")

elif choice == "RESEARCH & CERTIFICATES":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png", width=75)
        st.title("")

    st.header("Research Papers and Certificates")

