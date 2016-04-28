import pyttsx

speech_engine = pyttsx.init('espeak')         # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
speech_engine.setProperty('rate', 100)        #print speech_engine.getProperty('voices')

def speak(text):
  speech_engine.say(text)
	speech_engine.runAndWait()
