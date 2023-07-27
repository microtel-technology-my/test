from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", "openai/whisper-large-v2")

pipe("chinese.mp3")