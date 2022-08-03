import pyttsx3
import speech_recognition as sr
import datetime
import pywhatkit
import wikipedia
import pyjokes
import smtplib
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Good Morning')
        speak('Good Morning')

    elif hour>=12 and hour<18:
        print('Good Afternoon')
        speak('Good Afternoon')
    else:
        print('Good Evening')
        speak('Good Evening')

    print("I am Sheldon, How may I help you")
    speak("I am Sheldon, How may I help you")
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("recognizing...")
        text = r.recognize_google(audio,language='en-IN')
        text = text.lower()
        if 'sheldon' in text:
            text = text.replace('sheldon','')
            print(text)

    except Exception as e:
        print('Say that again please...')
        return None

    return text

def sendEmail(to,content):
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.login('seemasingh72001@gmail.com', 'fzgxgvfeaumjsjmf')
     server.sendmail('aman', 'amangoel096@gmail.com', content)
     server.close()

def run():
    command = takecommand().lower()
    print(command)
    if 'play' in command:                       # to play any video on youtube
        song = command.replace('play','')
        speak('playing ' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in command:                     # tells the current time
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        speak('Current time is ' + time)
    elif 'who is' in command:                   # give a brief about anyone
        person = command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        speak(info)
    elif 'are you single' in command:
        print('I am in a relationship with wifi')
        speak('I am in a relationship with wifi')
    elif 'joke' in command:                      # tells some interesting jokes
        print(pyjokes.get_joke())

    elif 'send an email' in command:             # to send an email to anyone
        try:
            speak("What is the message you want to send?")
            content = takecommand().lower()
            print(content)
            to = "amangoel096@gmail.com"
            sendEmail(to,content)
            print("Email has been sent!")
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry,I am not able to send this email")
        else:
            print("Can't understand")
    elif 'good bye' in command:                 # to exit
        speak('GoodBye')
        exit(0)

if __name__ == '__main__':
    greet()
    while True:
        run()