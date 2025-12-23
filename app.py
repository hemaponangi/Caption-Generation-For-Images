import streamlit as st
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Image Caption Generator",
    page_icon="🖼️",
    layout="centered"
)

st.title("🖼️ AI Image Caption Generator")
st.subheader("Hackathon Project – Vision Language AI Tool")

# ---------------- MODEL LOAD ----------------
@st.cache_resource
def load_model():
    processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )
    model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )
    return processor, model

processor, model = load_model()

# ---------------- UI ----------------
uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

caption_type = st.selectbox(
    "Select caption type",
    ["Simple", "Detailed", "Social Media"]
)

prompt_map = {
    "Simple": "a photo of",
    "Detailed": "describe the image in detail",
    "Social Media": "write a catchy social media caption for"
}

# ---------------- PROCESS ----------------
if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Caption"):
        with st.spinner("Generating caption using AI..."):
            inputs = processor(
                image,
                text=prompt_map[caption_type],
                return_tensors="pt"
            )

            output = model.generate(**inputs, max_length=50)
            caption = processor.decode(
                output[0],
                skip_special_tokens=True
            )

        st.success("Caption Generated!")
        st.write("### 📝 Generated Caption")
        st.write(caption)

        st.download_button(
            "Download Caption",
            caption,
            file_name="image_caption.txt"
        )

# ---------------- USE CASES ----------------
st.markdown("---")
st.markdown("""
### 🔍 Use Cases
- Accessibility for visually impaired users  
- Social media content automation  
- E-commerce product description  
- Digital marketing and blogging  
""")

st.markdown("""
### 🛠 Technology Stack
- Python  
- Streamlit (Web UI)  
- Hugging Face Transformers  
- BLIP Vision-Language Model  
""")
