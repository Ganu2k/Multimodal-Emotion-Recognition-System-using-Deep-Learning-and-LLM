import gradio as gr
import cv2

from face_model import detect_face_emotion
from text_model import detect_text_emotion
from speech_model import detect_speech_emotion
from fusion import fuse_emotions

# =========================
# MAIN FUNCTION
# =========================
def multimodal_emotion(image, text, audio):
    
    # FACE
    if image is not None:
        face_emotion = detect_face_emotion(image)
    else:
        face_emotion = "neutral"

    # TEXT
    if text:
        text_emotion = detect_text_emotion(text)
    else:
        text_emotion = "neutral"

    # SPEECH
    if audio is not None:
        speech_emotion = detect_speech_emotion(audio)
    else:
        speech_emotion = "neutral"

    # FINAL
    final = fuse_emotions(face_emotion, text_emotion, speech_emotion)

    return face_emotion, text_emotion, speech_emotion, final


# =========================
# GRADIO UI
# =========================
interface = gr.Interface(
    fn=multimodal_emotion,
    inputs=[
        gr.Image(type="numpy", label="Upload Face Image"),
        gr.Textbox(label="Enter Text"),
        gr.Audio(type="filepath", label="Upload Audio")
    ],
    outputs=[
        gr.Textbox(label="Face Emotion"),
        gr.Textbox(label="Text Emotion"),
        gr.Textbox(label="Speech Emotion"),
        gr.Textbox(label="Final Emotion")
    ],
    title="Multimodal Emotion Recognition System 🔥",
    description="Upload face, text, and audio to detect emotion"
)

interface.launch(share=True)