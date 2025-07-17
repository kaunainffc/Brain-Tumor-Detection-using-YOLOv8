import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="🧠 Tumor Detector", layout="centered")
st.title("🧠 Brain Tumor Detection using YOLOv8")

API_URL = "https://tumour-medi-er9c.onrender.com/predict"  # Your FastAPI URL

uploaded_file = st.file_uploader("📤 Upload Brain MRI Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image to bytes for API request
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="JPEG")
    image_bytes.seek(0)

    with st.spinner("🔍 Detecting tumor..."):
        response = requests.post(API_URL, files={"file": image_bytes})

    if response.status_code == 200:
        result = response.json()

        boxes = result.get("boxes", [])
        scores = result.get("scores", [])
        classes = result.get("classes", [])

        if boxes:
            max_score = max(scores)  # Get the most confident prediction
            label = "Tumor Detected" if 1 in classes else "No Tumor Detected"
            st.success(f"🧠 **{label}** with **{max_score * 100:.2f}%** confidence")
        else:
            st.info("✅ No tumor detected in the image.")
    else:
        st.error("⚠️ API Error. Could not get prediction. Please try again.")
