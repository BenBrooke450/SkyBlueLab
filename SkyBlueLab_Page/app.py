import streamlit as st
from streamlit_option_menu import option_menu
import os
from streamlit_lottie import st_lottie
import base64
from openai import OpenAI



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

        if choice == "TEST":
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

    import streamlit as st
    import requests
    import pandas as pd

    if "test" not in st.session_state:
        st.session_state.test = False

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
        if "year_pick" not in st.session_state:
            st.session_state.year_pick = False

        if not st.session_state.year_pick:

            EU_COUNTRIES = [
                "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL",
                "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK",
                "SI", "ES", "SE"
            ]

            YEARS = list(range(2020, 2025))
            MONTHS = list(range(1, 13))
            WEEKS = list(range(1, 52))


            st.header("Filters")

            with st.expander("Dairy Filters", expanded=True):
                selected_years = st.multiselect("Select years", YEARS, default=[2024])
                selected_countries = st.multiselect("Select countries", EU_COUNTRIES, default=["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL","HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK","SI", "ES", "SE"])
                selected_months = st.multiselect("Select months", MONTHS, default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])


            def build_url_milk(years, countries, months):
                milk = "https://www.ec.europa.eu/agrifood/api/rawMilk/prices?"
                params = []
                if years:
                    params.append("years=" + ",".join(map(str, years)))
                if countries:
                    params.append("memberStateCodes=" + ",".join(countries))
                if months:
                    params.append("months=" + ",".join(map(str, months)))
                return milk + "&".join(params)



            with st.expander("Cheddar Filters", expanded=True):
                selected_years_C = st.multiselect("Select years", YEARS, default=[2024])
                selected_countries_C = st.multiselect("Select countries - Only 'IE','DE','NL','PL' report cheddar", EU_COUNTRIES, default=['IE','DE','NL','PL'])
                selected_weeks = st.slider("Select weeks", WEEKS, default=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52])


            def build_url_cheddar(years, countries, weeks):
                cheddar = f"https://ec.europa.eu/agrifood/api/dairy/prices?"
                params = []
                if years:
                    params.append("years=" + ",".join(map(str, years)))
                if countries:
                    params.append("memberStateCodes=" + ",".join(countries))
                if weeks:
                    params.append("weeks=" + ",".join(map(str, weeks)))

                return cheddar + "&".join(params) + "&products=CHEDDAR"

            milk_url = build_url_milk(selected_years, selected_countries, selected_months)
            cheddar_url = build_url_cheddar(selected_years, selected_countries, selected_months)

            if st.button("Fetch data"):
                try:
                    response_milk = requests.get(milk_url, timeout=30)
                    response_cheddar = requests.get(cheddar_url, timeout=30)
                    data_milk = response_milk.json()
                    data_cheddar = response_cheddar.json()


                    # Try to normalize response
                    if isinstance(data_milk, list):
                        df = pd.DataFrame(data_milk)
                    elif isinstance(data_milk, dict) and "data" in data_milk:
                        df = pd.DataFrame(data_milk["data"])
                    else:
                        df = pd.json_normalize(data_milk)

                    st.success("Dairy Data Loaded Successfully")
                    st.dataframe(df)

                    if isinstance(data_cheddar, list):
                        df = pd.DataFrame(data_cheddar)
                    elif isinstance(data_cheddar, dict) and "data" in data_cheddar:
                        df = pd.DataFrame(data_cheddar["data"])
                    else:
                        df = pd.json_normalize(data_cheddar)

                    st.success("Cheddar Data Loaded Successfully (Only 'IE','DE','NL','PL' report cheddar)")
                    st.dataframe(df)

                except Exception as e:
                    st.error(f"Error fetching data: {e}")

