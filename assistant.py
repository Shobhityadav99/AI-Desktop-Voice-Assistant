import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init()

voices= engine.getProperty('voices')
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
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__=="__main__":
    # wishme()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open_new_tab('youtube.com')

        elif 'open google' in query:
            webbrowser.open_new_tab('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open_new_tab('stackoverflow.com')

        elif 'play music' in query:
            music_dir='D:\\Songs'
            songs=os.listdir(music_dir)
            print(songs)
            no = random.randrange(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[no]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is {strTime}")
        
        elif 'open code' in query:
            codepath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)