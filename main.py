import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import smtplib
import webbrowser

print('Initializing Jarvis!')
MASTER = "Enwidth"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()
speak("Initializing jarvis")

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
    elif hour>=18 and hour<20:
        speak("Good Evening" + MASTER)
    else:
        speak("Good Night" + MASTER)
    speak("I am Jarvis. How may I help you?")
wishme()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:  {query}\n")

    except:
        query = "Say that again please!"
        print(query)
        speak(query)
    return query

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()


query = takeCommand()

if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif 'open youtube' in query.lower():
    url = 'youtube.com'
    chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open(url)
elif 'play music' in query.lower():
    songs_dir = "D:\\Music"
    songs = os.listdir("D:\\Music")
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))
elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H,%M,%S")
    speak(f'{MASTER} the time is {strTime}')
elif 'open code' in query.lower():
    speak('Opening visual studio code')
    codePath = "C:\\Users\\pramod\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)
elif 'search for' in query.lower():
    query = query.replace('search for','')
    speak('Searching for '+query)
    chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
    webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open('https://www.google.com/search?q='+query)
elif 'send email' in query.lower():
    try:
        speak('Whom do you want to mail')
        to = takeCommand()
        speak('Your are sending email to '+ to.lower())
        speak("What should I send?")
        content = takeCommand()
        sendEmail(to, content)
        speak("Email sent successfully!")
    except Exception as e:
        print(e)


elif 'stop jarvis' in query.lower():
    speak('Terminating jarvis')


