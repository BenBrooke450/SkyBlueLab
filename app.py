

import streamlit as st

import streamlit as st
st.set_page_config(layout="wide")

# --- 1. TOP NAVIGATION (TABS) ---
import streamlit as st

# 1. Create a "Navigation" selector (This acts as your Tabs)
# You can put this in the sidebar or at the top
choice = st.radio(" ", ["HOME", "SCIENCE & EXPLORATION", "MISSIONS"], horizontal=True)

# 2. Use 'if' statements to define the content AND the sidebar for each
if choice == "HOME":
    # --- SIDEBAR FOR TAB 1 ---
    with st.sidebar:  # Your new circle logo!
        st.title("Home Settings")
        st.radio("View Mode", ["Standard", "Compact"])
        st.checkbox("Show Lab Announcements")

    # --- MAIN CONTENT FOR TAB 1 ---
    st.header("Welcome to the Lab")
    st.title("🏠 SkyBlueLab Gateway")
    st.write("Welcome to the main portal.")

elif choice == "SCIENCE & EXPLORATION":
    # --- SIDEBAR FOR TAB 2 ---
    with st.sidebar:
        st.title("Science Filters")
        st.date_input("Research Date")
        st.button("Download ESA Data")

    # --- MAIN CONTENT FOR TAB 2 ---
    st.header("Exploration Hub")
    st.write("Deep space telemetry goes here.")

elif choice == "MISSIONS":
    # --- SIDEBAR FOR TAB 3 ---
    with st.sidebar:
        st.title("Mission Status")
        st.success("All Systems Nominal")

    # --- MAIN CONTENT FOR TAB 3 ---
    st.header("Active Missions")
    st.write("Tracking SkyBlue-1 Satellite.")