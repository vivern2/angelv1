#Speak.py controls how angel will speak

#below allows us to run system level commands 
import os

#below imports the pyttsx3 library which is used for text to speech conversion
import pyttsx3

#Below allows us to run terminal commands safely 
import subprocess

#this function initializes the pyttsx3 engine and sets the voice properties
engine = pyttsx3.init(driverName='espeak')

#Below is the speak function that takes in text as an argument and uses the pyttsx3 engine to convert it to speech
def speak(text):
     subprocess.run(["espeak-ng", text])
