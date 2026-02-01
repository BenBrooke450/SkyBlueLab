

import streamlit as st
from PIL import Image

st.set_page_config(page_title="SkyBlueLab", page_icon="🔬")
st.title("SkyBlueLab: Vision AI")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model_type = st.radio("Choose Model", ["EfficientNet-B0", "Vision Transformer"])
