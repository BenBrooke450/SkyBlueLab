import streamlit as st
from streamlit_option_menu import option_menu
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="SkyBlueLab | Benjamin Brooke", page_icon="🌐", layout="wide",initial_sidebar_state="expanded")

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



with st.sidebar:

    try:
        import base64
        import os


        # 1. Function to convert local image to base64
        def get_base64_image(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()


        # 2. Set your image path (make sure this matches your file name exactly!)
        img_path = "SkyBlueLab/Gemini_Generated_Image_xvmap5xvmap5xvma.png"

        if os.path.exists(img_path):
            img_base64 = get_base64_image(img_path)

            # 3. CSS for the circle
            st.markdown(f"""
                <style>
                .circular-image {{
                    width: 200px;
                    height: 200px;
                    border-radius: 50%;
                    overflow: hidden;
                    display: block;
                    margin: 20px auto;
                    border: 3px solid #f0f2f6;
                    object-fit: cover;
                    box-shadow: 0px 4px 10px rgba(0,0,0,0.1); /* Optional shadow */
                }}
                </style>
                <img src="data:image/png;base64,{img_base64}" class="circular-image">
                """, unsafe_allow_html=True)
        else:
            st.error(f"Could not find the image at: {img_path}")
    except:
        st.icon("person_circle", size="large")

    st.markdown("### Benjamin Brooke")
    st.caption("**Senior Data Scientist & AI Engineer**  |  *Madrid, Spain*")
    st.write("Ben.brooke97@icloud.com")
    st.write("SPAIN +34 641 565 991")
    st.write("UK +44 7306 382 896")
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
    st.markdown(""" **Fine tuned using LoRA (Low-Rank Adaptation) on Llama-3 with medical Q&A datasets.**""")

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
        st.info("Please authenticate using the sidebar to access the LLM.")

elif choice == "PROJECTS":
    st.title("Project Portfolio")
    st.info("Detailed Projects of my work in Artificial Intelligence and Data Engineering.")

    with st.container(border=True):
        st.subheader("IBM AI Engineering")
        col1, col2 = st.columns([1, 2])

        with col1:
            # A clean diagram or UI screenshot
            st.metric("Pytorch", "400 Hours", "Machine Learning")

        with col2:
            st.subheader("Building Artificial Intelligence")
            st.write("Built a Decoder Transformer Model & RAG Agent")
            st.markdown("""
                <style>
                .tech-badge {
                    display: inline-block;
                    padding: 4px 12px;
                    margin: 4px;
                    border-radius: 16px;
                    background-color: #f0f2f6;
                    color: green;
                    font-weight: bold;
                    font-size: 0.8rem;
                    border: 1px solid #d1d5db;
                }
                </style>
                """, unsafe_allow_html=True)

            st.markdown("""
                <span class="tech-badge">Apache Spark</span>
                <span class="tech-badge">Generative AI</span>
                <span class="tech-badge">Keras (Neural Network Library)</span>
                <span class="tech-badge">Prompt Engineering</span>
                <span class="tech-badge">PyTorch</span>
                <span class="tech-badge">Vector Databases</span>
                <span class="tech-badge">Machine Learning</span>
                <span class="tech-badge">Large Language Modeling</span>
                <span class="tech-badge">Retrieval-Augmented Generation</span>


                 - 1.Machine Learning with Python
                 - 2.Introduction to Deep Learning & Neural Networks with Keras
                 - 3.Deep Learning with Keras and Tensorflow  
                 - 4.Introduction to Neural Networks and PyTorch
                 - 5.Deep Learning with PyTorch
                 - 6.AI Capstone Project with Deep Learning 
                 - 7.Generative AI and LLMs: Architecture and Data Preparation
                 - 8.Gen AI Foundational Models for NLP & Language Understanding
                 - 9.Generative AI Language Modeling with Transformers
                 - 10.Generative AI Engineering and Fine-Tuning Transformers
                 - 11.Generative AI Advance Fine-Tuning for LLMs 
                 - 12.Fundamentals of AI Agents Using RAG and LangChain
                 - 13.Project: Generative AI Applications with RAG and LangChain
                """, unsafe_allow_html=True)

            st.link_button("View Code on GitHub", "https://github.com/BenBrooke450/IBM-AI-Engineering",
                           use_container_width=True)

    with st.container(border=True):
        st.subheader("Project Databricks Formula 1")
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
            st.subheader("Production-Grade Databricks Medallion Architecture")
            st.write("Developed and managed a Data Pipeline using Databricks and Azure to analyze and visualize Formula 1 race results. ")
            st.markdown("""
                <style>
                .tech-badge {
                    display: inline-block;
                    padding: 4px 12px;
                    margin: 4px;
                    border-radius: 16px;
                    background-color: #f0f2f6;
                    color: green;
                    font-weight: bold;
                    font-size: 0.8rem;
                    border: 1px solid #d1d5db;
                }
                </style>
                """, unsafe_allow_html=True)

            st.markdown("""
                <span class="tech-badge">Databricks</span>
                <span class="tech-badge">PySpark</span>
                <span class="tech-badge">Azure</span>
                <span class="tech-badge">SQL</span>
                <span class="tech-badge">Spark</span>
                <span class="tech-badge">Pandas</span>
                """, unsafe_allow_html=True)

            button_label = "Close Deep Dive" if st.session_state.show_deep_dive_1 else "View Deep Dive"
            st.button(button_label, key="project1", on_click=toggle_deep_dive)

        if st.session_state.show_deep_dive_1:
            st.divider()
            st.write("### Technical Architecture")
            st.write("""
            - 1.ingestion - Contains notebooks to ingest all data files from the raw layer to the ingested layer. Handles the incremental data for files: results, pitstops, laptimes, and qualifying.
            - 2.trans - Contains notebooks to transform the data from the ingested layer to the presentation layer. Performs transformations to set up for analysis.
            - 3.set-up - Notebooks to mount ADLS storages (raw, ingested, presentation) in Databricks.
            - 4.includes - Contains notebooks with helper functions used in transformations.
            - 5.analysis - Contains SQL files for finding the dominant drivers and teams. Prepares results for visualization.
            - 6.raw - Contains SQL files to create ingested tables using Spark SQL.
            - 7.utils - Contains SQL files to drop all databases for incremental load.
            - 8.data - Contains sample raw data from the Ergast API.
            """)
            st.link_button("View Code on GitHub", "https://github.com/BenBrooke450/Project-Databricks-Formula1", use_container_width=True)


    with st.container(border=True):
        st.subheader("Evolution of Image Detection for Deep Neural Networks")
        col1, col2 = st.columns([1, 2])

        if 'show_Image_1' not in st.session_state:
            st.session_state.show_Image_1 = False

        def toggle_deep_dive():
            st.session_state.show_Image_1 = not st.session_state.show_Image_1

        with col1:
             # A clean diagram or UI screenshot
            st.metric("Databricks & Azure", "150 Hours", "Medallion Architecture")
            st.metric("Scale", "10k+", "Records")

        with col2:
            st.subheader("Analysing Accuracy and Efficiency in the Training of Evolution of Image Classification")
            st.write("Eevolution of image classification models, focusing on major architectural milestones from early convolutional neural networks to modern transformer-based approaches")
            st.markdown("""
                <style>
                .tech-badge {
                    display: inline-block;
                    padding: 4px 12px;
                    margin: 4px;
                    border-radius: 16px;
                    background-color: #f0f2f6;
                    color: green;
                    font-weight: bold;
                    font-size: 0.8rem;
                    border: 1px solid #d1d5db;
                }
                </style>
                """, unsafe_allow_html=True)

            st.markdown("""
                <span class="tech-badge">Databricks</span>
                <span class="tech-badge">PySpark</span>
                <span class="tech-badge">Azure</span>
                <span class="tech-badge">SQL</span>
                <span class="tech-badge">Spark</span>
                <span class="tech-badge">Pandas</span>
                """, unsafe_allow_html=True)

            button_label = "Close Deep Dive" if st.session_state.show_Image_1 else "View Deep Dive"
            st.button(button_label, key="project2", on_click=toggle_deep_dive)

        if st.session_state.show_Image_1:
            st.divider()
            st.write("### Technical Architecture")
            st.write("""
            - 1.ingestion - Contains notebooks to ingest all data files from the raw layer to the ingested layer. Handles the incremental data for files: results, pitstops, laptimes, and qualifying.
            - """)
            st.link_button("View Code on GitHub", "https://github.com/BenBrooke450/Python-PyTorch/tree/main/IT%20599%20Research%20Paper", use_container_width=True)







elif choice == "RESEARCH & CERTIFICATES":
    st.title("Research & Credentials")
    st.write("Published papers and professional certifications.")




