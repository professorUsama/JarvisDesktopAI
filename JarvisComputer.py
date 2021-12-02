'''
Author: M Usama Amjid
NickName = DarkWeb
Purpose: Learn
Created Date = December 02, 2021
Facebook page: https://www.facebook.com/informationTechnology5256/
YouTube Channel: https://www.youtube.com/channel/UC6NrVQEqUXQq4tHdDrfMipw
'''


import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
from random import randint
import getpass
from platform import platform


#Globals Variables section###################

ind_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-IN_HEERA_11.0' #indian voice

# setting for using default browser in windows
browser_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox',None,webbrowser.BackgroundBrowser(browser_path))

# get computer user name
userName = getpass.getuser()
# get windows version 
win_version = platform()

#defining functions=============================

def speak(text):
    '''
    this function take a string and convert it into voice...
    '''
    engine = pyttsx3.init()
    engine.getProperty('voices')
    engine.setProperty('voice',ind_voice_id)
    engine.setProperty('rate',150) #to increase or decrease speed voice if need
    engine.say(text)
    engine.runAndWait()


def greetingMessage():
    '''
    this function is define to give greeting message when the program starts...
    '''
    hour = int(datetime.datetime.now().hour) # to store the current hour in integer type
    if hour <= 12:
        speak("Good Morning Sir. Have a nice day.")
    elif hour >= 12 and hour <= 17:
        speak("Good Afternoon Sir. Have a nice day.")
    elif hour >=18:
        speak("Good Evening Sir. Have a nice day.")
    
    speak(f"Asslam-O-Alaikum! I am {userName}. How may I help you.")

def takeAudioCommands():
    '''
    this function take query using microphone and then perform tasks
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening...")
        audio = r.listen(source,phrase_time_limit=4)

    try:
        print("Recognize...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}")

    except Exception as e:
        print("say that again...")
        return "None"
    
    return query



if __name__ == '__main__':
    # speak("Sir, Please tell me time.")
    greetingMessage()
    while(True):
        query = takeAudioCommands().lower()

        #use logic to perform query tasks
        if 'quit' in query or 'quit jarvis' in query or 'exit' in query or 'exit jarvis' in query:
            speak("Thanks for using me Sir.")
            break
        elif 'who are you' in query:
            speak(f"I am {userName}. And {win_version} system installed.")
        
        elif 'play music' in query:
            try:
                music_folder_path = "D:\\fvt videos\\Martab ali"
                songs = os.listdir(music_folder_path)
                os.startfile(os.path.join(music_folder_path,songs[randint(0,len(songs)-1)]))
            except Exception:
                speak(f"Sorry, Folder doesn't exist.")

        elif 'tell me time' in query or 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak(f"The time is {time}")
        elif 'tell me date' in query or 'date' in query:
            date = datetime.date.today().strftime('%B %d, %Y')
            print(date)
            speak(f"The date is {date}")
        
        elif 'open vs code' in query:
            path = f"C:\\Users\\{userName}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif 'wikipedia' in query:
            query = query.replace('wikipedia','')
            speak("searching...")
            try:
                result = wikipedia.summary(query,sentences=4)
                print(result)
                speak(result)
            except Exception as e:
                speak("Connection Error")
        elif 'open firefox' in query:
            firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
            os.startfile(firefox_path)
        elif 'open google' in query:
            webbrowser.get('firefox').open('google.com')
        elif 'open facebook' in query:
            webbrowser.get('firefox').open('facebook.com')
        elif 'open whatsapp' in query or 'whatsapp' in query:
            webbrowser.get('firefox').open('whatsapp.com')

        