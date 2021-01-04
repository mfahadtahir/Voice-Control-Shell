import formatting
import voice
import modules
import subprocess

#this function will print out the welcome window
def welcome_window():
    subprocess.call(['clear'])
    formatting.head('Voice Controlled Shell')
    formatting.text_box('Hi, I am your virtual Assistant and you can ask me to perform the following tasks.')
    formatting.table_head('Command', 'Description')
    formatting.table_content('Send Email', 'Can send mails to several receivers')
    formatting.table_content('Weather Update', 'Will display the current weather Report')
    formatting.table_content('List Files', 'Will List files of current Directory')
    formatting.table_content('Date', "Today's date will be displayed")
    formatting.table_content('Shutdown', 'The computer will be powered off')
    formatting.table_content('Reboot', 'The computer will restart')
    formatting.table_content('Create File', 'New file will be created in the current folder')
    formatting.table_content('File type', 'The file information will be displayed')
    formatting.table_content('Create User', 'The new user will be created.')
    formatting.table_content('Delete User', 'Deletes the user.')
    formatting.table_content('Current Directory', 'Current working Directory will be displayed')
    formatting.table_content('Create Directory', 'New Directory will be created')
    formatting.table_content('Go Back', 'Move to the previous directory')
    formatting.table_content('Change Directory', 'Move to the specified directory')
    formatting.table_content('Delete file', 'Deletes the specified file')
    formatting.table_content('Delete Directory', 'Deletes the specified directory')
    formatting.table_content('Exit', 'Exit Program')
    # voice.text_to_speech('Hi, I am your virtual Assistant and you can ask me to perform the following tasks.')
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
    elif(mytext.lower() == 'exit'):
        modules.exit_Program()
        return
    else:
        formatting.text_box('Invalid Command!')
        return

if __name__ == '__main__':
    voice.text_to_speech('Hi, I am your virtual Assistant and you can ask me to perform the following tasks.')
    flag = 1
    welcome_window()
    input('Press Enter and Say any Command...')
    subprocess.call(['clear'])
    while 1:
        if(flag == 1):
            mytext = voice.speech_to_text(1)
            flag = 0
        else:
            mytext = voice.speech_to_text()
        if(voice.error_status(mytext)):
            formatting.text_box('Please, try again!')
            continue
        elif(mytext == 'exit'):
            formatting.text_box('Good Bye!')
            voice.text_to_speech('Good Bye!')
            exit()
        else:
            subprocess.call(['clear'])
            execute(mytext)
            input('Press Enter and Say any Command...')
            subprocess.call(['clear'])
