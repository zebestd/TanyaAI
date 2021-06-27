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



r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            ironstone_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            ironstone_speak('Sorry, I did not get that')
        except sr.RequestError:
            ironstone_speak('Sorry, my speech servise is down')
        return voice_data


def ironstone_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')     
    r = random.randint(1, 10000000)  
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data:
        ironstone_speak('My name is Tanya')
    if 'what time is it' in voice_data:
        ironstone_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        ironstone_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
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


    if 'play' in voice_data:
        song = record_audio('Which song?')
        pywhatkit.playonyt(song)
        ironstone_speak('playing' + song)
        
    if 'clock' in voice_data:
        time = datetime.datetime.now().strftime('%H:%M')
        ironstone_speak('Current time is ' + time)
        print(time)
    if 'learn' in voice_data:
        person = record_audio('What do you want to learn?')
        info = wikipedia.summary(person, 1)
        print(info)
        ironstone_speak(info)
    if 'date' in voice_data:
        ironstone_speak('Of course!')
    if 'are you single' in voice_data:
        ironstone_speak('I am single for you')
    if 'tell me a joke' in voice_data:
        ironstone_speak(pyjokes.get_joke())
    
    if 'hi' in voice_data:
        ironstone_speak('Hello sir')

    if 'hi' in voice_data:
        ironstone_speak('Hello sir')

    if 'hello' in voice_data:
        ironstone_speak('Hello Tan')

    if 'how are you' in voice_data:
        ironstone_speak('I am great, and you?')

    if 'I am great' in voice_data:
        ironstone_speak('Good to hear!')

    if 'what do you love doing' in voice_data:
        ironstone_speak('I love helping you')


    if 'weather' in voice_data:
        weather = record_audio('What do you want to know?')
        place = record_audio('Where?')
        url = 'https://www.google.com/search?q=' + place + '%20' + weather
        webbrowser.get().open(url)
        ironstone_speak('Here is the current weather in ' + place)
  

    if 'thank you Tanya' in voice_data:
        ironstone_speak('Exiting')
        exit()

time.sleep(1)
ironstone_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)