import subprocess
import os
import formatting
import voice
#this file contains all the modules

def prompt(mytext):
    formatting.text_box(mytext)
    voice.text_to_speech(mytext)
    var = voice.speech_to_text()
    if(voice.error_status(var)):
        prompt('Please try again')
    else:
        return var

def send_mail():
    import smtplib
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    sender_email = 'muhammadfahad325302@gmail.com'
    sender_password = 'rjcxwpzfgovmjmnr'
    smtpObj.login(sender_email, sender_password)
    receiver_email = []
    formatting.line()
    n = input('Please enter total number of receivers: ')
    formatting.line()
    for i in range(int(n)):
        receiver_email.append(input('Enter email of receiver ' + str(i+1) + ': '))
    formatting.line()
    sub = prompt('Please tell subject.')
    body = prompt('Please tell your message')
    content = 'Subject:' + sub + '\n' + body
    formatting.head('Message')
    formatting.table_content('*', 'From', sender_email, 12, 58)
    formatting.table_content('*', 'To', str(receiver_email), 12, 58)
    formatting.table_content('*', 'Subject', sub, 12, 58)
    formatting.text_box(body)
    temp = 'y'
    temp = input('Are you sure to send mail?(Y/n): ')
    if(temp == 'y' or temp == 'Y'):
        for i in range(int(n)):
            smtpObj.sendmail(sender_email, receiver_email[i], content)
        print('Email sent successfully!')
        return
    else:
        print('Email not sent!')
        return


def weather_update():
  import urllib.request, json
  url = "http://api.weatherapi.com/v1/current.json?key=d8693f806abe4a0a9e7165056212501&q=Karachi"
  json_url = urllib.request.urlopen(url)
  data = json.loads(json_url.read())
      
  print(data)
  formatting.head('Current Weather')
  formatting.table_content('1', 'Location', data['location']['name'] )
  formatting.table_content('2', 'Last Updated', data['current']['last_updated'])
  formatting.table_content('3', 'Temperature', str(data['current']['temp_c']) + "°")
  formatting.table_content('4', 'Wind', str(data['current']['wind_mph']) + " mph, " + data['current']['wind_dir'])
  formatting.table_content('5', 'Humidity', str(data['current']['humidity']))
  formatting.table_content('6', 'Cloud', str(data['current']['cloud']))
  formatting.table_content('7', 'Pressure', str(data['current']['pressure_mb']) + " Millibar")
  formatting.table_content('8', 'Visibility', str(data['current']['vis_km']) + " Kilo Meters")
  formatting.table_content('9', 'Ultra Violet', str(data['current']['uv']))
  # subprocess.call(["sudo","tiv", "https:" + data['current']['condition']['icon']])

  return
  




def list_files():
    list = os.listdir('.')
    formatting.head('Files in current Directory')
    for i in range(len(list)):
        formatting.text_box(list[i])
    return

def today_date():
    from datetime import date
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    today = date.today()
    day = str(today.day)
    month = months[int(today.month) - 1]
    year = str(today.year)
    formatting.text_box("Today's date is " + day + " " + month + " " + year)
    return

def shutdown_now():
    formatting.text_box("Shutting down the computer...")
    subprocess.call(["shutdown", "-h", "now"])
    return

def reboot_now():
    print("Rebooting the computer...")
    subprocess.call(["shutdown", "-r", "now"])
    return

def create_file():
    temp = 'y'
    formatting.line()
    file_name = input('Enter the name of file: ')
    formatting.line()
    temp = input("Are you sure to create file with name " + file_name + "(Y/n): ")
    formatting.line()
    if temp == 'n' or temp == 'N':
        formatting.text_box("File creation cancelled!")
        return
    else:
        subprocess.call(["touch", file_name])
        formatting.text_box("File with name " + file_name + " created Successfully!")
        return
      
def create_folder():
    temp = 'y'
    formatting.line()
    folder_name = input('Enter the name of Folder: ')
    formatting.line()
    temp = input("Are you sure to create Folder with name " + folder_name + "(Y/n): ")
    formatting.line()
    if temp == 'n' or temp == 'N':
        formatting.text_box("Folder creation cancelled!")
        return
    else:
        subprocess.call(["mkdir", folder_name])
        formatting.text_box("Folder with name " + folder_name + " created Successfully!")
        return

def file_type():
    formatting.line()
    file_name = input("Enter the name of file: ")
    formatting.line()
    list = os.listdir('.')
    if file_name in list:
        formatting.line()
        subprocess.call(["file", file_name])
        formatting.line()
        return
    else:
        formatting.text_box("The file is not in current Directory")
        return

def create_user():
    import crypt
    formatting.line()
    user_name = input("Enter user name: ")
    formatting.line()
    user_password = input("Enter password: ")
    formatting.line()
    encrypted_password = crypt.crypt(user_password)
    user_add = "sudo useradd -m " + user_name + " -p " + encrypted_password
    try:
        os.system(user_add)
        return
    except:
        formatting.text_box("Problem creating user!")
        return

def delete_user():
    formatting.line()
    user_name = input("Enter user name: ")
    formatting.line()
    del_user = subprocess.call(["sudo", "deluser", user_name])
    formatting.text_box("User: " + str(del_user) + " deleted Successfully!")

def current_working_dir():
    path = os.getcwd()
    formatting.text_box(path)
    return

def create_dir():
    formatting.line()
    folder_name = input("Enter the name of new Directory: ")
    formatting.line()
    subprocess.call(["mkdir", folder_name])
    print("New Folder created successfully!!")
    return

def change_dir():
    formatting.line()
    folder_name = input("Enter the name of directory: ")
    formatting.line()
    current_dir = os.getcwd()
    os.chdir(current_dir +  "/" + folder_name)
    formatting.text_box(os.getcwd())
    return

def back():
    os.chdir("../")
    formatting.text_box(os.getcwd())
    return

def delete_file():
    formatting.line()
    file_name = input("Enter the name of the file: ")
    formatting.line()
    subprocess.call(["rm", file_name])
    return

def delete_dir():
    formatting.line()
    dir_name = input("Enter the name of the Directory: ")
    formatting.line()
    subprocess.call(["rmdir", dir_name])
    return
