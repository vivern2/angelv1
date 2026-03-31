#Speak.py controls how angel will speak

import os

#below imports the pyttsx3 library which is used for text to speech conversion
import pyttsx3

import subprocess

#this function initializes the pyttsx3 engine and sets the voice properties
engine = pyttsx3.init(driverName='espeak')
#this function takes a string input and uses the pyttsx3 engine to speak it out loud
def speak(text):
     subprocess.run(["espeak-ng", text])
