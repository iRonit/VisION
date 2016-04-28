#!/usr/bin/python
import pyttsx

def speak(text):
	speech_engine = pyttsx.init('espeak')         # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
	speech_engine.setProperty('rate', 100)        #print speech_engine.getProperty('voices')
  	speech_engine.say(text)
	speech_engine.runAndWait()
