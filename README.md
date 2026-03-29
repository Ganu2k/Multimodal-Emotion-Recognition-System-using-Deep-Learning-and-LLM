# Multimodal-Emotion-Recognition-System-using-Deep-Learning-and-LLM

> 🔥 A next-generation AI system that understands human emotions by combining **Face + Voice + Text** in real-time.

---

## 🧠 Overview

This project builds an **intelligent multimodal AI system** capable of analyzing human emotions from three different sources:

- 👤 Facial Expressions (Computer Vision)
- 🎤 Speech Signals (Audio Processing)
- 💬 Text Input (LLM-based Sentiment Analysis)

The system intelligently fuses these inputs to produce a **more accurate and human-like emotion prediction**.

---

## ✨ Key Highlights

🚀 Real-time emotion detection  
🧠 Combines Deep Learning + LLM  
🎯 Higher accuracy using multimodal fusion  
🌐 Interactive web app (Gradio UI)  
⚡ Lightweight and efficient models  


## 🏗️ Architecture

User Input
│
├── 👤 Face Image ──▶ CNN Model ──▶ Face Emotion
├── 🎤 Audio File ──▶ MFCC + NN ──▶ Speech Emotion
└── 💬 Text Input ──▶ Ollama LLM ──▶ Text Emotion
│
▼
🧠 Fusion Engine (Voting)
│
▼
🎯 Final Emotion Output

---

## 🛠️ Tech Stack

| Domain              | Technology Used |
|--------------------|----------------|
| Programming        | Python         |
| Deep Learning      | TensorFlow / Keras |
| Computer Vision    | OpenCV         |
| Speech Processing  | Librosa (MFCC) |
| NLP / LLM          | Ollama         |
| UI / Deployment    | Gradio         |

---

## 📂 Project Structure
emotion_project/
│
├── app.py # Main Gradio App
├── face_model.py # Face Emotion Detection
├── speech_model.py # Speech Emotion Detection
├── text_model.py # Text Emotion (LLM)
├── fusion_module.py # Emotion Fusion Logic
├── face_model.h5 # Trained Face Model
├── speech_model.h5 # Trained Speech Model
├── ravdess_dataset/ # Audio Dataset
└── README.md

---

## ⚙️ Installation

```bash
pip install -r requirements.txt

# Run application
python app.py

🧪 How It Works

1️⃣ Upload a face image
2️⃣ Enter text input
3️⃣ Upload speech audio
4️⃣ System predicts:

Face Emotion 👤
Speech Emotion 🎤
Text Emotion 💬
Final Emotion 🎯

🧠 AI Models Used
Face Model → CNN trained on facial expressions
Speech Model → MFCC feature extraction + Neural Network
Text Model → Ollama LLM for sentiment understanding
Fusion Model → Majority Voting Algorithm
📊 Why Multimodal?

Humans express emotions in multiple ways.
This system mimics human perception by combining:

✔ Visual cues
✔ Vocal tone
✔ Language meaning

👉 Result: More accurate & robust emotion detection

🔥 Future Enhancements
🎥 Live webcam emotion detection
🎤 Real-time speech recognition
📊 Emotion analytics dashboard
🌐 Cloud deployment (Streamlit / HuggingFace)
🤖 Emotion-aware chatbot integration
👨‍💻 Author

👨‍💻 Author
🎯 Aspiring AI/ML Engineer
🚀 Passionate about building intelligent systems

🌐 GitHub Repository
https://github.com/yourusername/multimodal-emotion-recognition
