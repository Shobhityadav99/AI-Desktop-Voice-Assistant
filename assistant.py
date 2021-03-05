import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

voices= engine.getProperty('voices') #getting details of current voice
# print(voices)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<=12:
        speak('Good Morning!')
    elif hour>12 and hour<=18:
        speak('Good Evening!')
    else:
        speak('Good Night!')
    speak("Hello i am chintu! How may i help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print('User said:',query)

if __name__=="__main__":
    wishme()