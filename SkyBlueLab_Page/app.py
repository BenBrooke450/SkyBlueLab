import streamlit as st
from streamlit_option_menu import option_menu
import os
from streamlit_lottie import st_lottie
import base64
from openai import OpenAI
import requests
import pandas as pd


import sys
import os
from Dairy_Calculations_PySpark.THI_map import map_of_europe
from Dairy_Calculations_PySpark.Cheese_price_map import get_cheddar_price
from Dairy_Calculations_PySpark.Dairy_stats_map import get_dairy_stats



st.set_page_config(page_title="SkyBlueLab | Benjamin Brooke", page_icon="🌐", layout="wide",initial_sidebar_state="expanded")


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
    options=["HOME", "RESEARCH & CERTIFICATES","PROJECTS", "OCEAN", "TEST"],
    icons=["flower1", "file-earmark-person","bi bi-floppy-fill", "tsunami", "calculator"],
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

        def get_base64_image(image_path):
            with open(image_path, "rb") as img_file:
                return base64.b64encode(img_file.read()).decode()


        img_path = "SkyBlueLab_Page/Assets/Gemini_Generated_Image_xvmap5xvmap5xvma.png"

        if choice == "TEST" or choice == "OCEAN":
            img_path = "SkyBlueLab_Page/Assets/SkyBlueLab.png"


        if os.path.exists(img_path):
            img_base64 = get_base64_image(img_path)

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
    st.caption("**Senior Clinical Data Scientist & AI Engineer**")
    st.caption("*Madrid, Spain*")
    st.caption("*London, UK*")
    st.write("Ben.brooke97@icloud.com")
    with st.container(border=True):
        st.write("SPAIN +34 641 565 991")
        st.write("UK +44 7306 382 896")



if choice == "HOME":

    with st.sidebar:
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

    col_main, col_spacer = st.columns([2, 1])
    with col_main:
        st.info("**Please navigate through the tabs for more information**")
        st.markdown("""
        
        #### **Professional Profile**
        Senior Clinical Data Scientist with **5+ years of experience** building high-performance ETL and ML systems for **clinical research**.
        
        #### **Education & Research**
        * **MSc in Artificial Intelligence** | *Walsh College* (June 2026) 
            * Research focus on **AI Agents** and **Transformer Architecture**
            * **Research publication view Research tab**
        * **BSc in Mathematics & Statistics** | *University of Strathclyde* 
        
        ---""")

        st.markdown("""
             <style>
             .tech-pill {
                 display: inline-block;
                 padding: 4px 12px;
                 margin: 5px 4px;
                 border-radius: 15px;
                 background-color: #E1F5FE; /* Light Blue Background */
                 color: #01579B;            /* Dark Blue Text */
                 font-weight: 600;
                 font-size: 0.85rem;
                 border: 1px solid #81D4FA; /* Soft Blue Border */
                 transition: 0.3s;
                 cursor: default;
             }
             .tech-pill:hover {
                 background-color: #B3E5FC; /* Slightly darker on hover */
                 border-color: #0288D1;
             }
             </style>
         """, unsafe_allow_html=True)

        st.markdown("### Artificial Intelligence & Machine Learning")

        st.markdown("""
            **Clinical NLP & Machine Learning**
            - Developed transformer-based pipelines (ClinicalBERT) for entity recognition and information extraction in clinical datasets
            
            **Data Engineering (Databricks)**
            - Built distributed ETL pipelines processing 100k+ clinical records daily using PySpark and Delta Lake
            
            **Applied ML Systems**
            - Implemented MLflow pipelines for experiment tracking, reproducibility, and deployment
        """)

        st.divider()

        st.markdown("### Clinical & Regulatory Experience")

        st.markdown("""
        - Worked with clinical trial datasets in regulated environments  
        - Experience supporting data pipelines aligned with CDISC standards (SDTM/ADaM)  
        - Ensured data integrity, traceability, and reproducibility in clinical workflows  
        """)

        st.divider()

        stack = {
            "Languages": ["Python", "SQL", "PySpark", "PyTorch", "SAS", "Scikit-Learn"],
            "AI/ML": ["Transformers", "Vision Transformers", "Vector Databases", "LoRA", "RAG", "LangGraph", "HuggingFace"],
            "Engineering": ["Databricks", "Azure", "ETL","Docker"]
        }

        for cat, tools in stack.items():
            st.write(f"**{cat}:**")
            st.markdown(" ".join([f'<span class="tech-pill">{t}</span>' for t in tools]), unsafe_allow_html=True)




        with col_spacer:

            st.markdown("### Key Impact")
            st.metric("Data Volume", "100k Records/Day", "Clinical ETL")
            st.metric("Spark Efficiency Gain with ETL", "50% Reduction", "Processing Time")
            st.metric("Experience", "5+ Years", "Senior Level")
            st.metric("AI Agents Triage", "20% Reduction", "Manual Triage")






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

        st.success("Ready for queries. OceanBlue is online.")

        client = OpenAI()

        SYSTEM_PROMPT = """
        You are SkyBlueLab AI.

        You help users understand AI, machine learning, and clinical NLP.
        Be clear, concise, and helpful.
        """


        if "messages" not in st.session_state:
            st.session_state.messages = []


        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.write("You:", msg["content"])
            else:
                st.write("OceanBlue:", msg["content"])


        user_input = st.text_input("Ask a question")

        if st.button("Send") and user_input:
            st.session_state.messages.append(
                {"role": "user", "content": user_input}
            )

            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            messages += st.session_state.messages

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=messages
            )

            reply = response.choices[0].message.content

            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

            st.write("OceanBlue:", reply)



    else:
        st.info("Please authenticate using the sidebar to access the LLM.")












elif choice == "PROJECTS":

    with st.sidebar:
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

    st.title("Project Portfolio")
    st.info("Detailed Projects of my work in Artificial Intelligence and Data Engineering.")

    with st.container(border=True):
        st.subheader("IBM AI Engineering")
        col1, col2 = st.columns([1, 2])

        with col1:

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


                 - 1. Machine Learning with Python
                 - 2. Introduction to Deep Learning & Neural Networks with Keras
                 - 3. Deep Learning with Keras and Tensorflow  
                 - 4. Introduction to Neural Networks and PyTorch
                 - 5. Deep Learning with PyTorch
                 - 6. AI Capstone Project with Deep Learning 
                 - 7. Generative AI and LLMs: Architecture and Data Preparation
                 - 8. Gen AI Foundational Models for NLP & Language Understanding
                 - 9. Generative AI Language Modeling with Transformers
                 - 10. Generative AI Engineering and Fine-Tuning Transformers
                 - 11. Generative AI Advance Fine-Tuning for LLMs 
                 - 12. Fundamentals of AI Agents Using RAG and LangChain
                 - 13. Project: Generative AI Applications with RAG and LangChain
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
        st.subheader("Building Deep Neural Networks")
        col1, col2 = st.columns([1, 2])

        if 'show_Image_1' not in st.session_state:
            st.session_state.show_Image_1 = False

        def toggle_deep_dive():
            st.session_state.show_Image_1 = not st.session_state.show_Image_1

        with col1:
             # A clean diagram or UI screenshot
            st.metric("Pytorch", "Over 100 Hours", "FFN - CNN - Transformers")

        with col2:
            st.subheader("Deep Learning Artificial intelligence Sandbox")
            st.write("This Github is where I have developed many different types of AI systems, from encoder transformers for sentiment analysis to simple FFNs")
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
                <span class="tech-badge">Pytorch</span>
                <span class="tech-badge">FFNs</span>
                <span class="tech-badge">CNNs</span>
                <span class="tech-badge">Transformers</span>
                <span class="tech-badge">RAG</span>
                <span class="tech-badge">Langchain</span>
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
    with st.sidebar:
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

    st.title("Research & Credentials")
    st.write("Published papers and professional certifications.")

    col1, col2 = st.columns([1, 1])
    with col1:
        with st.container(border=True):
            st.markdown("Image Classification Research Paper: LeNet-5 to Vision Transformers")
            st.caption("Deep dive into CNN and Vision Transformer Architecture")
            st.image("SkyBlueLab_Page/Assets/Screenshot_15-3-2026_121838_.png")
            st.write("This paper explores the Accuracy and Efficiency in the Evolution of Image Classification in Deep Neural Networks")

            try:
                with open("SkyBlueLab_Page/Assets/ResearchPaper.pdf", "rb") as f:
                    st.download_button(
                        label="Download: Image Classification Research Paper ",
                        data=f,
                        file_name="SkyBlueLab_Page/ResearchPaper_AI_Engineer.pdf",
                        mime="application/pdf",
                        use_container_width=True  # Makes the button fill the box
                    )
            except FileNotFoundError:
                st.error("PDF file not found in directory.")

    with col2:
        with st.container(border=True):
            st.markdown("Multi-Agent Systems Research Paper")
            st.caption("Automation of Workplace Tasks to Increase Efficiency")
            st.image("SkyBlueLab_Page/Assets/Walsh-College-social-thumbnail.png")
            st.markdown("""**[Publish in May]**""")
            st.write("This paper explores the AI frameworks composed of multiple interacting, autonomous agents that collaborate or compete to solve complex, large-scale tasks to improve productivity.")


    with col1:
        with st.container(border=True):
            st.markdown("SAS for Clinical Data")
            st.caption("Data Management of Drug Trials")
            st.image("SkyBlueLab_Page/Assets/SAS.png")

            try:
                with open("SkyBlueLab_Page/Assets/Coursera SAS Programmer.pdf", "rb") as f:
                    st.download_button(
                        label="Download Certificate: SAS for Clinical Data",
                        data=f,
                        file_name="Coursera SAS Programmer",
                        mime="application/pdf",
                        use_container_width=True
                    )
            except FileNotFoundError:
                st.error("PDF file not found in directory.")

    with col2:
        with st.container(border=True):
            st.markdown("IBM AI Engineering")
            st.caption("Machine Learning & Artificial Intelligence")
            st.image("SkyBlueLab_Page/Assets/IBM.png")

            try:
                with open("SkyBlueLab_Page/Assets/IBM AI Engineering.pdf", "rb") as f:
                    st.download_button(
                        label="Download: IBM AI Engineering",
                        data=f,
                        file_name="IBM AI Engineering.pdf",
                        mime="SkyBlueLab_Page/application/pdf",
                        use_container_width=True
                    )
            except FileNotFoundError:
                st.error("PDF file not found in directory.")



elif choice == "TEST":





    if "test" not in st.session_state:
        st.session_state.test = False

    if "dairy_reports" not in st.session_state:
        st.session_state.dairy_reports = None

    if "price_reports" not in st.session_state:
        st.session_state.price_reports = None

    if "expanded" not in st.session_state:
        st.session_state.expanded = True







    if not st.session_state.test:
        st.warning("Access Restricted")
        pin = st.text_input("Enter Access Code", type="password")

        if st.button("Unlock System", use_container_width=True):
            if pin == "1234":
                st.session_state.test = True
                st.rerun()
            else:
                st.error("Invalid Code")

    else:
        if st.button("Secure Log Out", use_container_width=True):
            st.session_state.test = False
            st.rerun()

    if st.session_state.test:
        with st.expander("Summary", expanded=True):
            st.info("""
                        Market data on European agriculture provided by the European Commission:

                        * https://agridata.ec.europa.eu/extensions/DataPortal/agricultural_markets.html
                        * https://ec.europa.eu/eurostat/databrowser/view/apro_mk_colm/default/table?lang=en
                        * https://cds.climate.copernicus.eu/datasets/reanalysis-uerra-europe-single-levels?tab=download

                        ---

                        ### Project Summary: End-to-End AI & Data Engineering Platform

                        This project is a full-stack data engineering and machine learning platform designed to ingest, process, and analyse real-time data through scalable cloud infrastructure.

                        The system uses Scaleway as the backend engine. Real-time and historical data are collected via external APIs, ensuring that the system continuously operates on up-to-date information.

                        A distributed data processing pipeline is implemented using Apache Spark with PySpark, where raw data is cleaned, transformed, and structured into analysis-ready formats. This ETL layer is designed for scalability and performance.

                        On top of this data layer, machine learning and deep learning models are developed using both scikit-learn and PyTorch. Traditional ML techniques are applied for predictive analytics, while neural networks are used for more advanced modelling tasks.

                        * Cloud infrastructure (Scaleway)
                        * Real-time API ingestion
                        * Distributed data processing (Spark)
                        * Machine learning & deep learning (scikit-learn, PyTorch)
                        * Interactive data applications (Streamlit)
                        * LLM integration for intelligent assistance

                        """)

            st.warning(
                "**This system uses Apache Spark instead of Databricks, as both are built on Spark but the free-tier UI in Databricks is very limited. I implemented all ETL pipelines using PySpark that clean and process all the ingested data.**")






        st.divider()






        with st.expander("European Dairy Heat Stress (THI)", expanded=True):

            st.markdown("## **Interactive map for THI calculated using seasonal temperatures and humidity from EuroStats.**")

            fig = map_of_europe()
            st.plotly_chart(fig, use_container_width=True)





        st.divider()



        with st.expander("Cheese Price Volatility across the European Union", expanded=True):

            with st.container(border=True):

                st.markdown("## **Data Analysis - Comparative market analysis of cheese price volatility across the European Union.**")

                col1, col2 = st.columns([3, 1])

                YEARS = list(range(2020, 2026))

                with col1:
                    selected_year = st.selectbox(
                        "Select Period:",
                        options=YEARS,
                        index=YEARS.index(2023),
                        label_visibility="collapsed"
                    )

                with col2:
                    generate_clicked_button = st.button("Run Spark Job - Cheese Price Data", key="Dairy_Price_Data", use_container_width=True, type="primary")

            if generate_clicked_button:

                status_text = st.empty()
                status_text.status(f"Running Spark Session for {selected_year}...", expanded=True)

                fig, final_df_for_table = get_cheddar_price(selected_year)

                st.session_state.price_reports = {
                    "year": selected_year,
                    "fig": fig,
                    "df": final_df_for_table
                }

                st.toast(f"Data for {selected_year} processed successfully!")
                st.rerun()

            else:
                st.info("**Pro-Tip:** This report uses a distributed Spark engine to calculate multi-country price trends.")

            if st.session_state.price_reports is not None:
                r = st.session_state.price_reports

                st.plotly_chart(r["fig"], use_container_width=True)

                with st.expander(f"View Spark Output (Raw Data: {r['year']})", expanded=False):
                    st.dataframe(r["df"].head(500), use_container_width=True)



        st.divider()


        with st.expander("Dairy Content Breakdown", expanded=True):

            with st.container(border=True):

                st.markdown("## **Data Analysis - Interactive bar chart for showing Dairy Content in the European Union.**")

                col1, col2 = st.columns([3, 1])

                YEARS = list(range(2020, 2025))

                COUNTRIES = [
                    "Belgium","Bulgaria","Czechia","Denmark","Germany","Estonia",
                    "Ireland","Greece","Spain","France","Croatia","Italy","Cyprus",
                    "Latvia","Lithuania","Luxembourg","Hungary","Malta","Netherlands",
                    "Austria","Poland","Portugal","Romania","Slovenia","Slovakia",
                    "Finland","Sweden","Iceland","Norway","Switzerland",
                    "United Kingdom","Montenegro","North Macedonia","Albania",
                    "Serbia","Türkiye"
                ]

                with col1:
                    selected_year = st.selectbox(
                        "Select Analysis Period:",
                        options=YEARS,
                        index=YEARS.index(2023),
                        label_visibility="collapsed"
                    )

                    selected_country = st.selectbox(
                        "Select Country:",
                        options=COUNTRIES,
                        index=COUNTRIES.index("United Kingdom"),
                        label_visibility="collapsed"
                    )

                with col2:
                    generate_clicked = st.button("Run Spark Job - Dairy Data", key="Dairy_Data", use_container_width=True, type="primary")

            if generate_clicked:

                status_text = st.empty()
                status_text.status(f"Running Spark Session for {selected_year} & {selected_country}...", expanded=True)

                fig, df_filtered = get_dairy_stats(selected_year, selected_country)

                st.session_state.dairy_reports = {
                    "year": selected_year,
                    "country": selected_country,
                    "fig": fig,
                    "df": df_filtered
                }

                st.toast(f"Data for {selected_year} & {selected_country} processed successfully!")
                st.rerun()

            else:
                st.info("**Pro-Tip:** This report uses a distributed Spark engine to process large-scale stats data.")

            if st.session_state.dairy_reports is not None:
                r = st.session_state.dairy_reports

                st.plotly_chart(r["fig"], use_container_width=True)

                with st.expander(f"View Spark Output (Raw Data: {r['year']} & {r['country']})", expanded=False):
                    st.dataframe(r["df"].head(500), use_container_width=True)


        st.divider()


        with st.expander("Dairy Prices and Cheddar Prices across the European Union", expanded=True):

            st.info("**Pro-Tip:** Use the filters to see dairy prices across Europe")


            col1, col2 = st.columns([1, 1])

            EU_COUNTRIES = [
                "AT","BE","BG","HR","CY","CZ","DK","EE","FI","FR","DE","EL",
                "HU","IE","IT","LV","LT","LU","MT","NL","PL","PT","RO","SK",
                "SI","ES","SE"
            ]

            YEARS = list(range(2020, 2026))
            MONTHS = list(range(1, 13))

            if st.session_state.expanded:

                with col1:
                    with st.expander("Dairy Filters", expanded=True):
                        selected_years = st.multiselect("Select years for Dairy", YEARS, default=[2023])
                        selected_countries = st.multiselect("Select countries for Dairy", EU_COUNTRIES, default=["FR","DE"])
                        selected_months = st.multiselect("Select months for Dairy", MONTHS, default=[1,2,3,4,5,6])

                with col2:
                    with st.expander("Cheddar Filters", expanded=True):
                        WEEKS = list(range(1, 53))
                        selected_years_C = st.multiselect("Select years for Cheddar", YEARS, default=[2023])
                        selected_countries_C = st.multiselect("Select countries for Cheddar - Only ['IE','DE','NL','PL'] - report cheddar", EU_COUNTRIES, default=['IE','DE','NL','PL'])
                        selected_weeks_C = st.multiselect("Select weeks for Cheddar", WEEKS, default=[1,2,3,4,5,6,7,8,9])

                def build_url_milk(years, countries, months):
                    milk = "https://www.ec.europa.eu/agrifood/api/rawMilk/prices?"
                    params = []
                    if years: params.append("years=" + ",".join(map(str, years)))
                    if countries: params.append("memberStateCodes=" + ",".join(countries))
                    if months: params.append("months=" + ",".join(map(str, months)))
                    return milk + "&".join(params) + "&products=Raw%20milk"

                def build_url_cheddar(years, countries, weeks):
                    cheddar = f"https://www.ec.europa.eu/agrifood/api/dairy/prices?"
                    params_c = []
                    if years: params_c.append("years=" + ",".join(map(str, years)))
                    if countries: params_c.append("memberStateCodes=" + ",".join(countries))
                    if weeks: params_c.append("weeks=" + ",".join(map(str, weeks)))
                    return cheddar + "&".join(params_c) + "&products=Cheddar"

                st.session_state.milk_url = build_url_milk(selected_years, selected_countries, selected_months)
                st.session_state.cheddar_url = build_url_cheddar(selected_years_C, selected_countries_C, selected_weeks_C)

            if st.button("Fetch data"):
                st.session_state.expanded = False
                st.rerun()

            if not st.session_state.expanded:

                if st.button("Show Filters"):
                    st.session_state.expanded = True
                    st.rerun()

                response_milk = requests.get(st.session_state.milk_url, timeout=30)
                response_cheddar = requests.get(st.session_state.cheddar_url, timeout=30)

                data_milk = response_milk.json()
                data_cheddar = response_cheddar.json()

                col3, col4 = st.columns([1, 1])

                with col3:
                    try:
                        df = pd.DataFrame(data_milk) if isinstance(data_milk, list) else pd.json_normalize(data_milk)
                        st.success("Dairy Data Loaded Successfully")
                        st.dataframe(df)
                    except Exception as e:
                        st.error(f"Error fetching data: {e}")

                with col4:
                    try:
                        df = pd.DataFrame(data_cheddar) if isinstance(data_cheddar, list) else pd.json_normalize(data_cheddar)
                        st.success("Cheddar Data Loaded Successfully")
                        st.dataframe(df)
                    except Exception as e:
                        st.error(f"Error fetching data: {e}")