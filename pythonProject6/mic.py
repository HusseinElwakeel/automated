
import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from time import ctime
from gtts import gTTS
import datetime


r = sr.Recognizer()
mic = sr.Microphone(1)
s = sr.Microphone.list_microphone_names()
print(s)
