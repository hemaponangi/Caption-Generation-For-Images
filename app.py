# ------------------ CUSTOM CSS (FLORAL PASTEL PINK THEME) ------------------
st.markdown("""
<style>

/* MAIN BACKGROUND - FLORAL PASTEL PINK */
.stApp {
    background:
        linear-gradient(rgba(255, 240, 245, 0.6), rgba(255, 230, 240, 0.6)),
        url("https://images.unsplash.com/photo-1557682250-46e8d46b8b6f?auto=format&fit=crop&w=1470&q=80");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    font-family: 'Segoe UI', sans-serif;
}

/* COLOR-CHANGING TITLE */
.title {
    font-size: 48px;
    font-weight: 900;
    text-align: center;
    background: linear-gradient(
        90deg,
        #ff6ec4,
        #f9d423,
        #ffb6b9,
        #ffc1e3
    );
    background-size: 300% 300%;
    animation: textGradient 6s ease infinite;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* TEXT COLOR ANIMATION */
@keyframes textGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* SUBTITLE */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #444;
    margin-bottom: 30px;
}

/* FILE UPLOADER */
[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.55);
    border-radius: 20px;
    border: 2px dashed #f48fb1;
    padding: 20px;
}

/* COLORFUL BUTTON */
.stButton button {
    background: linear-gradient(
        135deg,
        #ff9a9e,
        #fad0c4,
        #fbc2eb
    );
    background-size: 300% 300%;
    color: #4a148c;
    font-size: 18px;
    font-weight: bold;
    border-radius: 40px;
    padding: 14px 42px;
    border: none;
    animation: buttonGradient 4s ease infinite;
    box-shadow: 0 0 18px rgba(255, 105, 180, 0.5);
    transition: all 0.3s ease;
}

@keyframes buttonGradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stButton button:hover {
    transform: scale(1.1);
    box-shadow: 0 0 30px rgba(255, 105, 180, 0.8);
}

/* IMAGE */
img {
    border-radius: 20px;
    box-shadow: 0 0 25px rgba(0,0,0,0.3);
}

/* CAPTION BOX */
.caption-box {
    margin-top: 25px;
    padding: 25px;
    border-radius: 25px;
    font-size: 22px;
    font-weight: bold;
    text-align: center;
    background: rgba(255,255,255,0.65);
    color: #4a148c;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(244,143,177,0.6);
}

/* FOOTER */
.footer {
    text-align: center;
    color: #555;
    opacity: 0.9;
    margin-top: 40px;
}

</style>
""", unsafe_allow_html=True)
