import speech_recognition as sr
import pyaudio
init_rec = sr.Recognizer()
print("speak")
with sr.Microphone() as source:
    audio_data=init_rec.record(source, duration=30)
    print ("recognizing")
    text=init_rec.recognize_google(audio_data, language="ru_RU")
    print(text)
