import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


from googletrans import Translator

import subprocess





r = sr.Recognizer()

def record_audio(ask = False):
    while True:
        try:
            with sr.Microphone() as source:
                if ask:
                    ironstone_speak(ask)
                r = sr.Recognizer()
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)
                voice_data = ''
                
                
                voice_data = r.recognize_google(audio)
                return voice_data
        except sr.UnknownValueError:
                r = sr.Recognizer()
                continue
        except sr.RequestError:
                r = sr.Recognizer()
                continue
    


def ironstone_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')     
    r = random.randint(1, 10000000)  
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):

    if "go back" in voice_data:
        ironstone_speak('All systems ready.')
        while 1:
            voice_data = record_audio()
            respond(voice_data)

    if 'what is your name' in voice_data:
        ironstone_speak('My name is Tanya')
    if 'what time is it' in voice_data:
        ironstone_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        if "go back" in search:
            ironstone_speak('All systems ready.')
            while 1:
                voice_data = record_audio()
                respond(voice_data)
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        ironstone_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        ironstone_speak('Here is the location of ' + location)
    if 'open channel' in voice_data:
        channel = record_audio('Which Youtube channel?')
        url = 'https://www.youtube.com/c/' + channel
        webbrowser.get().open(url)
        ironstone_speak('Here is ' + channel)
    if 'find video' in voice_data:
        video = record_audio('Which Youtube video?')
        url = 'https://www.youtube.com/results?search_query=' + video
        webbrowser.get().open(url)
        ironstone_speak('Here is ' + video)
    if 'mail' in voice_data:   
        url = 'https://mail.google.com/'
        webbrowser.get().open(url)
        ironstone_speak('Here is Google Mail')

    if 'google.com' in voice_data:   
        url = 'https://www.google.com/'
        webbrowser.get().open(url)
        ironstone_speak('Here is Google.com')


    if 'play' in voice_data:
        song = record_audio('Which video?')
        pywhatkit.playonyt(song)
        ironstone_speak('playing' + song)
        
    if 'clock' in voice_data:
        time = datetime.datetime.now().strftime('%H:%M %p')
        ironstone_speak('Current time is ' + time)
        print(time)
    if 'learn' in voice_data:
        person = record_audio('What do you want to learn?')
        info = wikipedia.summary(person, 1)
        print(info)
        ironstone_speak(info)
    if 'tell me a joke' in voice_data:
        ironstone_speak(pyjokes.get_joke())
    


    if 'hello Tanya' in voice_data:
        ironstone_speak('Hello Tan')

    if 'how are you' in voice_data:
        ironstone_speak('I am great, and you?')

    if 'I am great' in voice_data:
        ironstone_speak('Good to hear!')

    if 'what do you love doing' in voice_data:
        ironstone_speak('I love helping you')

    
    if 'thank you Tanya' in voice_data:
        ironstone_speak('Any time!')

    if 'Tanya you there' in voice_data:
        ironstone_speak('For you sir always')

    if 'Tanya you up' in voice_data:
        ironstone_speak('For you sir always')

    if 'weather' in voice_data:
        weather = record_audio('What do you want to know?')
        place = record_audio('Where?')
        url = 'https://www.google.com/search?q=' + place + '%20' + weather
        webbrowser.get().open(url)
        ironstone_speak('Here is the current weather in ' + place)
  


    if 'translation' in voice_data:
        url = 'https://translate.google.com/'
        webbrowser.get().open(url)
        ironstone_speak('Here is Google Translate')

       



    if 'turn off' in voice_data:
        ironstone_speak('Exiting')
        exit()


    


    if "make a note" in voice_data:
        ironstone_speak("What would you like me to write down? ")
        write_down = record_audio()
        if "go back" in write_down:
            ironstone_speak('All systems ready.')
            while 1:
                voice_data = record_audio()
                respond(voice_data)
        respond(write_down)
        ironstone_speak("I've made a note of that.")
        file_name = "ironstone" + "_note.txt"
        with open(file_name, "w") as f:
            f.write(write_down)

        subprocess.Popen(["notepad.exe", file_name])


time.sleep(1)
ironstone_speak('All systems ready.')
while 1:
    voice_data = record_audio()
    respond(voice_data)