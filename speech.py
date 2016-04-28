#!/usr/bin/python

class Speech:
	def __init__(self, gender, language):
		self.__gender=gender
		self.__language=language 
	
	def set_gender(self, gender):
		self.__gender=gender
	
	def get_gender(self):
		return self.__gender
		
def speak(self, text_file):
	contents = ''
	with open(text_file, 'r') as handle:
		for line in handle.readlines():
			contents += line.strip() + ' '
	contents=contents.replace("\xe2\x80\x98", "")
	contents=contents.replace("'", '')
	contents=contents.replace("\\", '')
	print repr(contents)
	os.remove(text_file)
	voice=""
	if gender.lower()=="male":
		voice = ""     #Please add the appropriate command option
	else:
		voice = ""	#same here for female
	os.system('espeak -s 100 --gender=' + self.__gender + ' --language=' + self.__language + '--stdout ' + repr(contents) + ' | aplay')
