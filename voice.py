from time import sleep
import sys
import speech_recognition as sr
from gtts import gTTS
import formatting
import subprocess
import os
import formatting
import subprocess
import concurrent.futures


path = os.getcwd()

#this function will tell if the error occur or not
def error_status(mytext):
    if(mytext == 0):
        return True
    else:
        return False


def recognize_audio(r, audio, result):
  result[0] = r.recognize_google(audio)
  return


#this function converts speech to text
def speech_to_text(flag = 0):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        if(flag == 1):
            subprocess.call(['clear'])
        formatting.show_list()
        formatting.text_box('Listening...')
        audio = r.listen(source)
    try:
        subprocess.call(['clear'])
                        
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
          future = executor.submit(r.recognize_google, audio)
          # Loading 
          i = 0
          stages = ['Processing.', 'Processing..', 'Processing...']
          while(future.running()):
            subprocess.call(['clear'])
            formatting.text_box(stages[i])
            i += 1
            if(i >= 3):
              i = 0
            sleep(0.5)
          mytext = future.result()
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
        myObj = gTTS(text = mytext, lang = 'en')
        myObj.save(path + '/main.mp3')
        os.system('mpg321 -q ' + path + '/main.mp3')
        return
