import pyttsx3

engine = pyttsx3.init()

voices= engine.getProperty('voices') #getting details of current voice
print(voices)

engine.setProperty('voice', voices[0].id)