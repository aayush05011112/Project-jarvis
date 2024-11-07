import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibary
import requests

r = sr.Recognizer()
engine = pyttsx3.init()
newsapi="b20e9d72e3cd4eac8918b691090e5893"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            #Extract the articles
            articles = data.get("articles", [])

            #print the headlines
            for articles in articles:
                speak(articles["title"])
    else:
        #let OpenAi handel the request
        print("Not advance enough:")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        # Listen for the wake word "Jarvis"
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        print("Recognizing...")

        # Recognize speech using Sphinx
        try:
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Ready for command")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processcommand(command)
        except Exception as e:
            print("Error: {0}".format(e))
