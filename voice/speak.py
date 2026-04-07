#Speak.py controls how angel will speak

#below allows us to run system level commands 
import os

#below imports the pyttsx3 library which is used for text to speech conversion
import pyttsx3

#Below allows us to run terminal commands safely 
import subprocess

#this function initializes the pyttsx3 engine and sets the voice properties
engine = pyttsx3.init(driverName='espeak')

# below is the switch for wheather we want ot turn on the speak mode
VOICE_MODE = True

#Below is the speak function that takes in text as an argument and uses the pyttsx3 engine to convert it to speech
def speak(text):
     if not VOICE_MODE:
        return
     
     #below will prevent awkward pauses between sentences  
     text = text.replace("\n", " ")

    # below is the command that will be run in the terminal to convert text to speech using espeak-ng, this is a more natural sounding voice than the default espeak voice
    # also has customizations for speed, pitch, and voice type to make it sound more human like
    
     subprocess.run([
        "espeak-ng",
        #Below will give it a female voice
        "-v", "en-us+f3", 
        #Below will give it a natural speed (lower = slower, more natural) 
        "-s", "165",     
        # Below will give it a more feminine pitch   (higher = more feminine)   
        "-p", "50",      
    ])
     

#Below is making a new thread so that the speak function can run in the background and not block the main thread, this will allow angel to speak while still being able to process user input and give responses without any lag or delay




