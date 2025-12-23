import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="AI Image Caption Generator",
    page_icon="🖼️",
    layout="centered"
)

# ------------------ ADVANCED CUSTOM CSS ------------------
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
    animation: glowText 2s infinite alternate;
}

/* TITLE GLOW */
@keyframes glowText {
    from { text-shadow: 0 0 10px #fff; }
    to { text-shadow: 0 0 25px #ffeb3b; }
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #ffffff;
    margin-bottom: 30px;
    opacity: 0.9;
}

/* UPLOAD BOX */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.15);
    border-radius: 20px;
    border: 2px dashed #ffffff;
    padding: 20px;
    backdrop-filter: blur(10px);
}

/* BUTTON */
.stButton button {
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 30px;
    padding: 12px 30px;
    border: none;
    transition: all 0.4s ease;
    box-shadow: 0 0 20px rgba(255, 0, 150, 0.6);
}

.stButton button:hover {
    transform: scale(1.08);
    box-shadow: 0 0 35px rgba(255, 0, 150, 0.9);
}

/* IMAGE CARD */
img {
    border-radius: 20px;
    border: 4px solid transparent;
    background: linear-gradient(white, white) padding-box,
                linear-gradient(135deg, #ff6ec4, #7873f5) border-box;
    animation: pulseBorder 3s infinite;
}

/* IMAGE BORDER ANIMATION */
@keyframes pulseBorder {
    0% { box-shadow: 0 0 10px #ff6ec4; }
    50% { box-shadow: 0 0 30px #7873f5; }
    100% { box-shadow: 0 0 10px #ff6ec4; }
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
    animation: fadeInUp 1.2s ease;
}

/* CAPTION ANIMATION */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
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
