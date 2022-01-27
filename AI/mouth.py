import pyttsx3

engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 160)

engine.say("I'm Jarvis, online and ready sir! Can you tell me how I may help you")
engine.runAndWait()