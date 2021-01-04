#This file will download all the requirements needed for the project
import subprocess
subprocess.call(["sudo", "apt", "update"])
subprocess.call(["sudo", "apt", "install", "python3-pip"])
list = ["pip3", "install", "pyaudio", "cryptography", "gTTS", "mpyg321", "Pillow", "selenium", "SpeechRecognition", "beautifulsoup4"]
subprocess.call(list)
