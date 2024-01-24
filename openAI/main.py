import speech_recognition as sr
import os
import webbrowser
import openai
import datetime

def say(text):
    os.system(f"say {text}")

def takeCmnd():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=0.5
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Sorry"

if __name__=='__main__':
    print("HELLO UMMA")
    say("HELLO I AM CHATBOT FROM A.I")
    while(True):
        print("Listening....")
        query=takeCmnd()
        sites=[["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        
        exit_loop = False
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
            # if f"open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Mam")
                webbrowser.open(site[1])
                exit_loop = True
        # say(query)

        if "open music" in query:
            musicPath="/Users/umabisht/Downloads/music.mp3"
            os.system(f"open {musicPath}")

        if "what's the time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Mam the time is {strfTime}")

        if "ok bye" in query  :
            say(f"Bye See you next time")
            break