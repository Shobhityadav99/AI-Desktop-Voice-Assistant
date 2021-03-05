import pyttsx3

engine = pyttsx3.init()

voices= engine.getProperty('voices') #getting details of current voice
# print(voices)

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__=="__main__":
    speak("Shobhit!")