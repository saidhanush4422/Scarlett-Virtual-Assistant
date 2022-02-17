import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Scarlett. how may I be in your service")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('scarlettvirtualai@gmail.com', 'scarlett!123#')
    server.sendmail('scarlettvirtualai@gmail.com', to, content)
    server.close()

#def exit():
#    return

if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif ('tell me about yourself'or'who are you'or'what the hell are you') in query:
            speak("I am you personal assistant to manage your system, you can find more about me in this webpage")
            codePath = "F:\\New folder\\scarlett\\new site\\Dewi\\Dewi\\index.html"
            os.startfile(codePath)

        elif 'email to dhanush' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "saidhanush4422@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry dear. I am unable to send this mail, I hope you understand")

        elif 'do you know siri' in query:
            speak(f"Who is that, is that my mother")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")

        elif 'open oracle' in query:
            webbrowser.open("https://www.oracle.com/index.html")

        elif 'open postgre sql' in query:
            webbrowser.open("https://www.postgresql.org/")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")

        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")

        elif 'open twitter' in query:
            webbrowser.open("twitter.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'open my github repository' in query:
            webbrowser.open("https://github.com/saidhanush4422/Scarlett-Virtual-Assistant")

        elif 'open data stacs' in query:
            webbrowser.open("https://auth.cloud.datastax.com/auth/realms/CloudUsers/protocol/openid-connect/registrations?client_id=auth-proxy&response_type=code&scope=openid+profile+email&redirect_uri=https://astra.datastax.com/welcome&utm_medium=referral&utm_source=youtube&utm_campaign=datastaxdevs&utm_content=Netflix-Clone-6-10")

        elif 'open google developers' in query:
            webbrowser.open("https://developers.google.com/")

        elif 'open atom' in query:
            codePath = "C:\\Users\\msdha\\AppData\\Local\\atom\\atom.exe"
            os.startfile(codePath)

        elif ('open internet') in query:
            codePath = "C:\\Users\\msdha\\Documents\\dist\\browlett\\browlett.exe"
            os.startfile(codePath)

#        elif 'exit' in query:
#            exit()

        else:
            print("Sorry I do not have that command")
