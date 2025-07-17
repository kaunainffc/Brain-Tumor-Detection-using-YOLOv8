
Here's a **professional and well-structured `README.md`** for your **Brain Tumor Detection API + Streamlit App using YOLOv8**:

---

# 🧠 Brain Tumor Detection – YOLOv8 + FastAPI + Streamlit

This project detects brain tumors from MRI images using a custom-trained **YOLOv8 model**, deployed via **FastAPI** and visualized using a **Streamlit frontend**.

---

## 🚀 Demo Links

* 🔗 **Live API (FastAPI Render)**: [https://tumour-medi-er9c.onrender.com](https://tumour-medi-er9c.onrender.com)
* 🔗 **Streamlit App (Local or Deployable)**: `http://localhost:8501` or \[Streamlit Cloud (Optional)]

---

## 📌 Features

✅ Upload MRI image
✅ Detect presence of tumor using YOLOv8
✅ Displays result:
    • **"Tumor Detected"** with confidence %
    • **"No Tumor Detected"**
✅ FastAPI-powered backend
✅ Streamlit-based frontend
✅ Easily extendable for other medical image detection tasks

---

## 🛠 Tech Stack

| Component        | Technology              |
| ---------------- | ----------------------- |
| Object Detection | YOLOv8 (Ultralytics)    |
| Backend API      | FastAPI                 |
| Frontend UI      | Streamlit               |
| Deployment       | Render (for API), Local |
| Language         | Python                  |

---

## 📂 Project Structure

```
brain-tumor-detector/
├── app.py                      # Streamlit frontend
├── main.py                     # FastAPI backend
├── yolov8_handler.py           # YOLO prediction logic
├── weights/
│   └── best.pt                 # Trained YOLOv8 model
├── requirements.txt
├── README.md
└── dataset/                    # Custom training data
```

---

## ▶️ How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/kaunainffc/YOLO-PERSON-DETECTOR.git
cd YOLO-PERSON-DETECTOR
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Start FastAPI (API Server)

```bash
uvicorn main:app --reload
```

> API will be live at `http://127.0.0.1:8000`
> Try Swagger docs at `http://127.0.0.1:8000/docs`

### 4️⃣ Start Streamlit (Frontend)

```bash
streamlit run app.py
```

> Opens the UI at `http://localhost:8501`

---

## 📊 Model Accuracy

The YOLOv8 model was trained on a labeled brain tumor dataset with:

* 📷 Images: 800+ MRI scans
* 📈 Classes: `['notumor', 'tumor']`
* 🎯 Accuracy: \~91% mAP\@0.5 on validation set

> You can retrain using `train.py` with your dataset.

---

## 📦 `requirements.txt`

```txt
ultralytics
fastapi
pillow
python-multipart
requests
uvicorn
streamlit
```

---

## 🙋‍♂️ Want to Collaborate?

If you're passionate about **AI in healthcare**, **medical imaging**, or **real-time detection systems**, feel free to:

* ⭐ Star the repo
* 🛠 Suggest new features
* 🤝 Connect on [LinkedIn](https://www.linkedin.com/in/kaunainffc)

---

## 📸 Example Output

![Sample Prediction](https://user-images.githubusercontent.com/your-image-url.png)

---

## 🔖 License

This project is licensed under the **MIT License**.
Free to use, modify, and build upon for academic or commercial purposes.

---

Let me know if you'd like a **PDF version**, **GitHub badge**, or **deployment guide for Streamlit Cloud**!
