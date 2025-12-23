import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Image Caption Generator",
    layout="centered"
)

# ------------------ CUSTOM CSS (BUTTON ENHANCED ONLY) ------------------
st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {
    background: linear-gradient(270deg, #ff6ec4, #7873f5, #4ADEDE, #F9D423);
    background-size: 800% 800%;
    animation: gradientBG 15s ease infinite;
    font-family: 'Segoe UI', sans-serif;
}

/* BACKGROUND ANIMATION */
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* TITLE */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(90deg, #ffffff, #ffeb3b);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ffffff;
    margin-bottom: 30px;
}

/* ----------- ENHANCED BUTTON ----------- */
.stButton button {
    background: linear-gradient(
        135deg,
        #ff0080,
        #ff8c00,
        #40e0d0
    );
    background-size: 300% 300%;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 40px;
    padding: 14px 42px;
    border: none;
    cursor: pointer;
    animation: buttonGradient 4s ease infinite;
    box-shadow: 0 0 20px rgba(255, 0, 150, 0.6);
    transition: all 0.3s ease;
}

/* BUTTON GRADIENT ANIMATION */
@keyframes buttonGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* BUTTON HOVER EFFECT */
.stButton button:hover {
    transform: scale(1.12);
    box-shadow: 0 0 35px rgba(255, 255, 255, 0.9);
}

/* BUTTON CLICK EFFECT */
.stButton button:active {
    transform: scale(1.05);
}

/* CAPTION BOX */
.caption-box {
    margin-top: 25px;
    padding: 25px;
    border-radius: 25px;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.25);
    color: #ffffff;
    backdrop-filter: blur(15px);
    border: 2px solid rgba(255,255,255,0.4);
}

/* FOOTER */
.footer {
    text-align: center;
    color: white;
    opacity: 0.8;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown('<div class="title">🖼️ AI Image Caption Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and let AI describe it magically ✨</div>', unsafe_allow_html=True)

# ------------------ LOAD MODEL ------------------
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# ------------------ IMAGE UPLOAD ------------------
uploaded_file = st.file_uploader("📤 Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="✨ Uploaded Image ✨", use_container_width=True)

    if st.button("✨ Generate Caption"):
        with st.spinner("AI is creating magic... 🤖✨"):
            inputs = processor(image, return_tensors="pt")
            output = model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True)

        st.markdown(
            f'<div class="caption-box">📸 {caption}</div>',
            unsafe_allow_html=True
        )

# ------------------ FOOTER ------------------
st.markdown('<div class="footer">Made with ❤️ | Streamlit × AI</div>', unsafe_allow_html=True)

