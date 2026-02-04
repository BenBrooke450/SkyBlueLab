

import streamlit as st
from streamlit_option_menu import option_menu
import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#from BlueOcean.ocean_app import run_ocean
#from Other_project.train import run_lab

#st.set_page_config(layout="wide")

choice = option_menu(
    menu_title=None,
    options=["HOME", "OCEAN", "LAB", "PROJECTS"],
    icons=["flower1", "tsunami", "infinity", "map"],
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
        st.radio("View Mode", ["Standard", "Compact"])
        st.checkbox("Show Lab Announcements")


    st.header("Welcome to the Lab")
    st.title("SkyBlueLab Gateway")
    st.write("Welcome to the main portal.")

elif choice == "OCEAN":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png", width=75)
        st.title("Science Filters")
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
                    st.error("Invalid Code")
        else:
            if st.button("Log Out of Science Hub"):
                st.session_state.science_auth = False
                st.rerun()

            from BlueOcean.ocean_app import run_ocean
            run_ocean()

    st.header("OceanBlue")
    st.write("This is my personal LLM, please use the tab on the left for access")

elif choice == "LAB":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png", width=75)
        st.title("Mission Status")
        st.success("All Systems Nominal")

    st.header("Active Missions")
    st.write("Tracking SkyBlue-1 Satellite.")

elif choice == "PROJECTS":
    with st.sidebar:
        st.image("SkyBlueLab/Cropped.png", width=75)
        st.title("Mission Status")
        st.success("All Systems Nominal")

    st.header("Active Missions")
    st.write("Tracking SkyBlue-1 Satellite.")