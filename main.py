from time import sleep
import sys
import formatting
import voice
import threading
import modules
import subprocess


def welcome_message(msg):
  voice.text_to_speech(msg)

def welcome_heading():
    formatting.line(86)
    sleep(0.3)
    for x in '| Hi, I am your Virtual Assistant and you can ask me to perform the following tasks. |\n':
        print(x, end='')
        sys.stdout.flush()
        sleep(0.07)
    
    formatting.line(86)
    return
  
def welcome_window():
    subprocess.call(['clear'])
    formatting.head('✨ Voice Controlled Shell ✨')
    
    # Making a thread to synchronize the audio message and text message
    writingText = threading.Thread(target=welcome_message, name="Welcome Audio", args=('Hi, I am your virtual Assistant and you can ask me to perform the following tasks.',))
    writingText.start()
    welcome_heading()    
    return

def execute(mytext):
    if(mytext.lower() == 'send email'):
        modules.send_mail()
        return
    elif(mytext.lower() == 'weather update'):
        modules.weather_update()
        return
    elif(mytext.lower() == 'list files'):
        modules.list_files()
        return
    elif(mytext.lower() == 'date'):
        modules.today_date()
        return
    elif(mytext.lower() == 'shutdown'):
        modules.shutdown_now()
        return
    elif(mytext.lower() == 'reboot'):
        modules.reboot_now()
        return
    elif(mytext.lower() == 'create file'):
        modules.create_file()
        return
    elif(mytext.lower() == 'create folder'):
        modules.create_folder()
        return
    elif(mytext.lower() == 'file type'):
        modules.file_type()
        return
    elif(mytext.lower() == 'create user'):
        modules.create_user()
        return
    elif(mytext.lower() == 'delete user'):
        modules.delete_user()
        return
    elif(mytext.lower() == 'current directory'):
        modules.current_working_dir()
        return
    elif(mytext.lower() == 'create directory'):
        modules.create_dir()
        return
    elif(mytext.lower() == 'go back'):
        modules.back()
        return
    elif(mytext.lower() == 'change directory'):
        modules.change_dir()
        return
    elif(mytext.lower() == 'delete file'):
        modules.delete_file()
        return
    elif(mytext.lower() == 'delete directory'):
        modules.delete_dir()
        return
    else:
        formatting.text_box('Invalid Command!')
        return

if __name__ == '__main__':
    flag = 1
    welcome_window()
    input('Press Enter to continue...')
    subprocess.call(['clear'])
    while 1:
        # 
        if(flag == 1):
          mytext = voice.speech_to_text(1)
          flag = 0
        else:
            mytext = voice.speech_to_text()
        
        # Checking Errors 
        if(voice.error_status(mytext)):
          formatting.text_box('Please, try again!')
          continue
        # Checking exit
        elif(mytext == 'exit'):
          formatting.text_box('Good Bye!')
          voice.text_to_speech('Good Bye!')
          exit()
        # calling the functionality 
        else:
          subprocess.call(['clear'])
          execute(mytext)
          input('Press Enter to continue...')
          subprocess.call(['clear'])
