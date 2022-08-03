import speech_recognition as sr
#import pyttsx3
listener = sr.Recognizer()
"""engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('I am your Nina')
engine.say('What can I do for you')
engine.runAndWait()"""

try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice,language='en-in')
        print(command)
except:
    pass