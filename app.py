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

# ------------------ ADVANCED CSS ------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

/* MAIN BACKGROUND */
.stApp {
    background:
        linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
        url("https://images.unsplash.com/photo-1526378722484-bd91ca387e72");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Poppins', sans-serif;
}

/* MAIN CONTAINER */
.block-container {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
    border-radius: 30px;
    padding: 35px;
    box-shadow: 0 0 50px rgba(0,0,0,0.45);
}

/* TITLE */
.title {
    font-size: 52px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #00f2fe, #4facfe, #f093fb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 30px rgba(255,255,255,0.3);
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #f1f1f1;
    margin-bottom: 35px;
    opacity: 0.9;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.15);
    border-radius: 25px;
    border: 2px dashed rgba(255,255,255,0.7);
    padding: 25px;
    transition: all 0.3s ease;
}

[data-testid="stFileUploader"]:hover {
    background: rgba(255,255,255,0.25);
    transform: scale(1.02);
}

/* BUTTON */
.stButton button {
    background: linear-gradient(135deg, #ff512f, #f09819);
    color: white;
    font-size: 18px;
    font-weight: 600;
    border-radius: 40px;
    padding: 14px 45px;
    border: none;
    transition: all 0.4s ease;
    box-shadow: 0 0 25px rgba(255,120,0,0.8);
    position: relative;
    overflow: hidden;
}

/* BUTTON GLOW EFFECT */
.stButton button::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(
        120deg,
        transparent,
        rgba(255,255,255,0.6),
        transparent
    );
    transition: all 0.6s ease;
}

.stButton button:hover::before {
    left: 100%;
}

.stButton button:hover {
    transform: translateY(-4px) scale(1.08);
    box-shadow: 0 0 45px rgba(255,160,0,1);
}

/* IMAGE */
img {
    border-radius: 25px;
    border: 3px solid rgba(255,255,255,0.6);
    box-shadow: 0 0 35px rgba(0,0,0,0.6);
    transition: transform 0.4s ease;
}

img:hover {
    transform: scale(1.03);
}

/* CAPTION BOX */
.caption-box {
    margin-top: 30px;
    padding: 30px;
    border-radius: 25px;
    font-size: 22px;
    font-weight: 600;
    text-align: center;
    background: rgba(255,255,255,0.18);
    color: #ffffff;
    backdrop-filter: blur(18px);
    border: 2px solid rgba(255,255,255,0.5);
    animation: fadeUp 1s ease;
}

/* CAPTION ANIMATION */
@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(40px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* FOOTER */
.footer {
    text-align: center;
    color: #ffffff;
    opacity: 0.85;
    margin-top: 50px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ------------------ TITLE ------------------
st.markdown('<div class="title">🖼️ AI Image Caption Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload an image and let AI describe it beautifully ✨</div>', unsafe_allow_html=True)

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
        with st.spinner("AI is thinking... 🤖✨"):
            inputs = processor(image, return_tensors="pt")
            output = model.generate(**inputs)
            caption = processor.decode(output[0], skip_special_tokens=True)

        st.markdown(
            f'<div class="caption-box">📸 {caption}</div>',
            unsafe_allow_html=True
        )

# ------------------ FOOTER ------------------
st.markdown('<div class="footer">Made with ❤️ | Streamlit × AI</div>', unsafe_allow_html=True)
