import librosa
import numpy as np
from tensorflow.keras.models import load_model

model = load_model("speech_model.h5")

emotions = ['neutral','happy','sad','angry']

def detect_speech_emotion(file):
    audio, sr = librosa.load(file, duration=3)

    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc = np.mean(mfcc.T, axis=0)

    mfcc = np.expand_dims(mfcc, axis=0)

    pred = model.predict(mfcc)
    return emotions[np.argmax(pred)]