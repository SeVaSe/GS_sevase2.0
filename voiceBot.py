import pyttsx3   # https://pyttsx3.readthedocs.io/en/lat...

engine = pyttsx3.init()

def scoreStndart():
	engine.setProperty('rate', 230)				#скорость речи

def scoreSlow():
	engine.setProperty('rate', 180)

def scoreFast():
	engine.setProperty('rate', 300)

def speaker(text):

	engine.say(text)
	engine.runAndWait()


