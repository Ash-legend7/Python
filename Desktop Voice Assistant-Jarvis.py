import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import google.generativeai as genai
#from openai import OpenAI


recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="5583a8ee11f6418ea900a44481daec04"

def aiProcess(command):
    # Configure with your API key
    genai.configure(api_key="AIzaSyDdj5jgwhklHehpXItffjty5CecZrdDNGo")

    # Choose model (gemini-pro for text, gemini-pro-vision for text+image)
    model = genai.GenerativeModel("gemini-2.5-flash")

    # Send a prompt
    response = model.generate_content(command)

    # Print the output text
    return response.text

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
    elif "headlines" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code==200:
            #Parse json response
            data=r.json()
            #extract articles
            articles=data.get('articles',[])
            #speak articles
            for article in articles:
                speak(article['title'])

    elif "stop" in c.lower():
        speak("Exiting Jarvis...")
        exit()
    else:
        #let ai api handle request
        output=aiProcess(c)
        speak(output)


    

if __name__=="__main__":
   speak("Initializing Jarvis..")
   try: 
    while True:
        #listen for wake word "Jarvis"
        # Use microphone as source
        
        #print("Recognizing...")
        try:
            with sr.Microphone() as source:
              print("Listening...")
              audio = recognizer.listen(source)
            # Recognize speech using Google Speech Recognition
            word = recognizer.recognize_google(audio)
            if (word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source)
                    command=recognizer.recognize_google(audio)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
   except KeyboardInterrupt:
    print("Exiting Jarvis...")
