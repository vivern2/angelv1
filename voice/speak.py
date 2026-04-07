#Speak.py controls how angel will speak



#Below allows us to run terminal commands safely 
from concurrent.futures import thread
import subprocess
#Below imports threading so we can add threads so voice can have its own thread from the gui
import threading 


#Below tracks if Angel is currently speaking 
speaking = False

#------------------------
# below Toggle for voice on/off
VOICE_MODE = True
def set_voice_enabled(value: bool):
    global VOICE_MODE
    VOICE_MODE = value


#Below is the speak function that takes in text as an argument and uses the pyttsx3 engine to convert it to speech
def speak(text):
     global speaking 

     if not VOICE_MODE or speaking:
        return
     speaking = True

     #below will prevent awkward pauses between sentences  
     text = text.replace("\n", " ")

    # below is the command that will be run in the terminal to convert text to speech using espeak-ng, this is a more natural sounding voice than the default espeak voice
    # also has customizations for speed, pitch, and voice type to make it sound more human like
     def run_speech():
        subprocess.run([
            "espeak-ng",
            #below we will give a british female accent
            "-v", "en-gb+f3" 
            #Below will give it a natural speed (lower = slower, more natural) 
            "-s", "150",     
            # Below will give it a more feminine pitch   (higher = more feminine)   
            "-p", "60",
            #Below will give a whisper like amplitude
            "-a", "80",
            text 
              
        ])
        speaking = False

        # Run in background thread
     thread = threading.Thread(target=run_speech)
     thread.start()
     
