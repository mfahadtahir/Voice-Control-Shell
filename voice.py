import speech_recognition as sr
from gtts import gTTS
import formatting
import subprocess
import os
#this file contains input output functions

path = os.getcwd()

#this function will tell if the error occur or not
def error_status(mytext):
    if(mytext == 0):
        return True
    else:
        return False

#this function converts speech to text
def speech_to_text(flag = 0):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if(flag == 1):
            subprocess.call(['clear'])
        formatting.text_box('Listening...')
        audio = r.listen(source)
    try:
        mytext = r.recognize_google(audio)
        return mytext
    except sr.UnknownValueError:
        formatting.text_box('Google Speech Recognition could not understand audio')
        return 0
    except sr.RequestError as e:
        formatting.text_box('Could not request results from Google Speech Recognition service; {0}'.format(e))
        return 0

#this function converts text to speech
def text_to_speech(mytext):
    global path
    if(error_status(mytext)):
        return
    else:
        myObj = gTTS(text = mytext, lang = 'en', slow = False)
        myObj.save(path + '/main.mp3')
        os.system('mpg321 -q ' + path + '/main.mp3')
        return
