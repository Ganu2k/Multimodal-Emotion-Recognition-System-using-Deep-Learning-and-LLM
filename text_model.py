import requests
import gradio as gr

#Deepseek API Url
OLLAMA_URL = "http://localhost:11434/api/generate"

def detect_text_emotion(text):
    """
    Deepseek AI to classify sentiment as positive, negative, or neutral.
    """
    #prompt = f"classify the sentiment of the following text as Possitive, Negative, or Neutral:\n\n{text}"
    prompt = f"Classify the emotion of the text into one word happy, sad, angry, neutral:\n\n{text}"
    #prompt = f"classify the sentiment of this text (in {language}) as Positive, Negative, or Neutral:\n\n{text}"
    payload={
        "model":"deepseek-r1:1.5b",
        "prompt": prompt,
        "stream": False
    }
    
    response = requests.post(OLLAMA_URL, json=payload)
    
    return response.json()["response"].strip().lower()