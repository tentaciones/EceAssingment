import speech_recognition as sr

r = sr.Recognizer()



toText = sr.AudioFile('audio.wav')
with toText as source:
    audio = r.record(source)
    
r.recognize_google(audio)