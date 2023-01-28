import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said:{query}")

    except Exception as e:
        speak("i can't get it sir say again...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning sir")
    elif hour>=12 and hour<17:
        speak("Good afternoon sir")
    elif hour>=17 and hour<23:
        speak("Good Evening sir:")
    else:
        speak("Good Night Sir:")
    speak("Hello Vanshikha pagal see")

if __name__ == '__main__':
    speak("system status is Ok. you are online")
    wish()

    while True:
        query = takeCommand().lower()

        if "open browser" in query:
            notepath = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            speak("ok. I am opening brave browser")
            os.startfile(notepath)


        elif "open fossil photo" in query:
            photopath="F:\\operations\\python learn\\jarvis project\\Photo.jpg"
            speak("ok. i am opening a fossil photo that present in default directory")
            os.startfile(photopath)

        elif "open kaushal photo" in query:
            photopath = "F:\\operations\\python learn\\jarvis project\\Photo.jpg"
            speak("ok. i am opening a fossil photo that present in default directory")
            os.startfile(photopath)

        elif "open my photo" in query:
            mypicpath = "F:\\operations\\python learn\\jarvis project\\my photo.jpg"
            speak("ok. i am opening one of your photo")
            os.startfile(mypicpath)
            speak("sir. i like this photo of you. you look hand some in this photo")

        elif "open family photo" in query:
            Fampath = "F:\\operations\\python learn\\jarvis project\\FamP.jpg"
            speak("ok. i am opening a family photo")
            os.startfile(Fampath)
            speak(" this photo clicked on Mr Ashif khan's ring ceremony. sir in this photo all of your family members are looking so young. just joking.")

        elif "who are you" in query:
            speak("i am noobi . a softwere based voice assisstant. that is under developing by Mr Fardeen khan. And my Hobby to run on terminal")

        elif "hello noobi" in query:
            speak("Oh Hello sir.")

        elif "what are you doing" in query:
            speak("sir, I am running on terminal. and making sure that you got comfort by me.")

        elif "tell me your birthday" in query:
            speak("17 july is my birth day.")

        elif "when you were born" in query:
            speak("Born is not right word for me. I was invented on 17 july 2021 by Mr Fardeen Khan. Thankyou Fardeen sir for giving me this opertunity.")

        elif "say hello to bhavya" in query:
            speak("Hello bhavya sir. i am noobi a softwere based voice assisstant.")


        else:
            speak("This feature is not added yet. i am under development so stay tune")
