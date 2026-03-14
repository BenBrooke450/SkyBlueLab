import streamlit as st
from streamlit_option_menu import option_menu
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="SkyBlueLab | Benjamin Brooke", page_icon="🌐", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Remove whitespace at top */
    .block-container { padding-top: 5rem; }

    /* Modern Card Hover Effects */
    .social-card {
        border: 1px solid #eee;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        transition: 0.3s;
        background: white;
    }
    .social-card:hover {
        border-color: #007BFF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        transform: translateY(-2px);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #eee;
    }
    </style>
""", unsafe_allow_html=True)






choice = option_menu(
    menu_title= "",
    options=["HOME", "OCEAN", "PROJECTS", "RESEARCH & CERTIFICATES","HOBBIES"],
    icons=["flower1", "tsunami", "bi bi-floppy-fill", "file-earmark-person","bi bi-signpost-2"],
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


with st.sidebar:

    try:
        st.image("SkyBlueLab/Cropped.png", width=80)
    except:
        st.icon("person_circle", size="large")

    st.markdown("### Benjamin Brooke")
    st.caption("**Senior Data Scientist & AI Engineer**  |  *Madrid, Spain*")
    st.write("Ben.brooke97@icloud.com")
    st.write("+34 641 565 991")
    st.divider()

# --- PAGE CONTENT ---
if choice == "HOME":
    with st.sidebar:
        st.write("**Contact & Socials**")
        sc1, sc2 = st.columns(2)
        with sc1:
            st.markdown("""
                <a href="https://github.com/BenBrooke450" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="social-card">
                        <i class="fa-brands fa-github" style="font-size:24px;"></i><br><small>GitHub</small>
                    </div>
                </a>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
            """, unsafe_allow_html=True)
        with sc2:
            st.markdown("""
                <a href="https://www.linkedin.com/in/benjamin-brooke-097063159/" target="_blank" style="text-decoration:none; color:inherit;">
                    <div class="social-card">
                        <i class="fa-brands fa-linkedin" style="font-size:24px; color:#0077b5;"></i><br><small>LinkedIn</small>
                    </div>
                </a>
            """, unsafe_allow_html=True)

    # Main Home Content
    col_main, col_spacer = st.columns([2, 1])
    with col_main:
        st.info("**Please navigate through the tabs for more information**")
        st.markdown("""
        
        #### **Professional Profile**
        Senior Data Scientist with **5+ years of experience** building high-performance ETL and ML systems for **clinical research**.
        
        #### **Education & Research**
        * **MSc in Artificial Intelligence** | *Walsh College* (June 2026) 
            * Research focus on **AI Agents** and **Transformer Architecture**;
            * **Research publication view Research tab**
        * **BSc in Mathematics & Statistics** | *University of Strathclyde* 
        
        ---""")

        st.info("""
        * **Clinical AI Expert:** Clinical NLP & LLMOps Architect: Fine-tuned **Encoder-based Transformers** (Clinical-BERT) for high-precision **NER** and Information Extraction, utilising **Parameter-Efficient Fine-Tuning (PEFT)** on **Decoder** models (Llama-3) to automate clinical summarization and **RAG-driven** decision support.
        
        * **Big Data Architect:** I assisted in engineering a distributed pipeline that processed over **100K** records daily and enforced schema validation and clinical entity resolution, reducing the latency between patient data entry and therapeutic insight by **50%**.
        
        * **AI Agents:** In my academic work I designed multi-agent workflows using LangGraph to automate technical support operations, achieving a **20% reduction in manual triage**.
        """)

        st.write("---")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Data Volume", "100k Records/Day", "Clinical ETL")
        col2.metric("Efficiency Gain", "50% Reduction", "Processing Time")
        col3.metric("Experience", "5+ Years", "Senior Level")
        col4.metric("AI Agents", "20% Reduction", "Manual Triage")
        st.write("---")

        st.markdown("""
        #### **Technical Stack**
        | Category | Tools & Technologies |
        | :--- | :--- |
        | **Programming** | Python, PySpark, SQL, Scikit-Learn, PyTorch  |
        | **AI/ML** | NLP, LLMs, RAG, CNNs, Transformers, LangChain, LangGraph  |
        | **Data Engineering** | Spark, Medallion Architecture, ETL Pipelines  |
        | **Platforms** | Databricks, Spotfire, HuggingFace, Ollama  |
        """)






elif choice == "OCEAN":
    st.title("OceanBlue")
    st.subheader("Personal LLM & Research Assistant")
    st.info("""Fine tuned using LoRA (Low-Rank Adaptation) on Llama-3 with medical Q&A datasets.""")

    with st.sidebar:
        if "science_auth" not in st.session_state:
            st.session_state.science_auth = False

        if not st.session_state.science_auth:
            st.warning("Access Restricted")
            pin = st.text_input("Enter Access Code", type="password")
            if st.button("Unlock System", use_container_width=True):
                if pin == "2026":
                    st.session_state.science_auth = True
                    st.rerun()
                else:
                    st.error("Invalid Code")
        else:
            st.success("Authenticated")
            if st.button("Secure Log Out", use_container_width=True):
                st.session_state.science_auth = False
                st.rerun()

    if st.session_state.science_auth:
        st.write("---")
        # run_ocean() would go here
        st.success("Ready for queries. OceanBlue is online.")
    else:
        st.write("Please authenticate using the sidebar to access the LLM.")

elif choice == "PROJECTS":
    st.title("Project Portfolio")
    st.info("Detailed case studies of my work in AI and Data Engineering.")

    with st.container(border=True):
        st.subheader("Project Databricks Formula1")
        col1, col2 = st.columns([1, 2])

        if 'show_deep_dive_1' not in st.session_state:
            st.session_state.show_deep_dive_1 = False

        def toggle_deep_dive():
            st.session_state.show_deep_dive_1 = not st.session_state.show_deep_dive_1

        with col1:
             # A clean diagram or UI screenshot
            st.metric("Databricks & Azure", "150 Hours", "Medallion Architecture")
            st.metric("Scale", "10k+", "Records")

        with col2:
            st.subheader("Clinical Data Classification Engine")
            st.write("Built a production-grade Medallion architecture to automate disease classification.")
            st.markdown("`Databricks` `PyTorch` `Hugging Face` `LoRA` `Spark` ")

            button_label = "Close Deep Dive" if st.session_state.show_deep_dive_1 else "View Deep Dive"
            st.button(button_label, key="project1", on_click=toggle_deep_dive)

        if st.session_state.show_deep_dive_1:
            st.divider()
            st.write("### Technical Architecture")
            st.image("https://via.placeholder.com/600x300")
            st.write("""
            - **Bronze:** Ingestion via PySpark.
            - **Silver:** Entity extraction via ClinicalBERT.
            - **Gold:** Pattern recognition for 1M+ records.
            """)
            st.link_button("View Code on GitHub", "https://github.com/your-repo", use_container_width=True)




elif choice == "RESEARCH & CERTIFICATES":
    st.title("Research & Credentials")
    st.write("Published papers and professional certifications.")

elif choice == "HOBBIES":
    st.title("Research & Credentials")
    st.write("Published papers and professional certifications.")