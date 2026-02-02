

import streamlit as st
from PIL import Image

st.set_page_config(page_title="SkyBlueLab")
st.title("SkyBlueLab: Vision AI")
st.sidebar.image("Website/Cropped.png", width=50)




# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model_type = st.radio("Choose Model", ["EfficientNet-B0", "Vision Transformer"])
