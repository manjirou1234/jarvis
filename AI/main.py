import speech_recognition
import pyttsx3
import webbrowser
import re
import wikipedia
from datetime import date
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from youtube_search import YoutubeSearch
import os

jarvis_ear = speech_recognition.Recognizer()
jarvis_brain = ""
wikipedia.set_lang("en")
path = ChromeDriverManager().install()
s = Service(path)

def hear():
	with speech_recognition.Microphone() as mic:
		print("Jarvis: I'm listening...")
		audio = jarvis_ear.listen(mic, timeout=5, phrase_time_limit=5)
	try:
		you = jarvis_ear.recognize_google(audio)
		return you
		print("You: ", you)
	except:
		you = ""
		return you

def hear_vie():
	with speech_recognition.Microphone() as mic:
		print("Jarvis: I'm listening...")
		audio = jarvis_ear.listen(mic, timeout=5, phrase_time_limit=5)
	try:
		you = jarvis_ear.recognize_google(audio, language='vi-VN')
		return you
		print("You: ", you)
	except:
		you = ""
		return you

def speak(jarvis_brain):
	jarvis_mouth = pyttsx3.init('sapi5')
	voices = jarvis_mouth.getProperty('voices')
	rate = jarvis_mouth.getProperty('rate')

	jarvis_mouth.setProperty('voices', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_Cortana')
	jarvis_mouth.setProperty('rate', 160)
		
	jarvis_mouth.say(jarvis_brain)
	print("Jarvis: ", jarvis_brain)
	jarvis_mouth.runAndWait()

def website(you):
	you = hear()
	if "open" in you:
		reg_ex = re.search('open (.+)', you)
		if reg_ex:
			domain = reg_ex.group(1)
			url = 'https://www.' + domain + '.com'
			webbrowser.open(url)
			speak("As you wish sir!")
		else:
			speak("Sorry sir! I'm afraid the website you want is unable to be found! Please try again sir")
	else:
		try:
			url = 'https://www.' + you + '.com'
			webbrowser.open(url)
			speak("As you wish sir!")
		except:
			speak("Sorry sir! I'm afraid the website you want is unable to be found! Please try again sir")

def tell_me_about():
	while True:
		you = hear()
		if "tell me about" in you:
			try:
				text = you.split("tell me about", 1)[1]
				contents = wikipedia.summary(text, sentences=3)
				speak(contents)
			except:
				speak("Looks like the information you want is unable to be found sir!")
		elif "stop" in you:
			speak("It's look like you have all the information you want")
			break
		elif "search for" in you:
			try:
				text = you.split("search for", 1)[1]
				contents = wikipedia.summary(text, sentences=3)
				speak(contents)
			except:
				speak("Looks like the information you want is unable to be found sir!")
		elif you == "":
			speak("Is there any information you want me to find sir?")
		else:
			try:
				contents = wikipedia.summary(you, sentences=3)
				speak(contents)
			except:
				speak("Looks like the information you want is unable to be found sir!")

def today():
	today = date.today()
	jarvis_brain = today.strftime("Today is %B %d, %Y")
	speak(jarvis_brain)

def time():
	now = datetime.now()
	jarvis_brain = now.strftime("It's %H hours %M minutes and %S seconds")
	speak(jarvis_brain)

def search_google():
	while True:
		you = hear()
		if "search for" in you:
			search = you.split("search for", 1)[1]
			driver = webdriver.Chrome(service=s)
			driver.get("http://www.google.com")
			que = driver.find_element_by_name("q")
			que.send_keys(str(search))
			que.send_keys(Keys.RETURN)
			speak("There you go sir!")
			break
		elif "Vietnamese" in you:
			speak("Switch to searching Google in Vietnamese successfully! What are you looking for sir?")
			while True:
				you = hear_vie()
				if you == "":
					speak("Is there anything you want me to search in Google sir?")
				else:
					driver = webdriver.Chrome(service=s)
					driver.get("http://www.google.com")
					que = driver.find_element_by_name("q")
					que.send_keys(str(you))
					que.send_keys(Keys.RETURN)
					speak("There you go sir!")
					break
				break
		elif "stop" in you:
			speak("As you wish! Stop searching Google funtion")
			break
		elif you == "":
			speak("Is there anything you want me to search in Google sir?")
		else:
			driver = webdriver.Chrome(service=s)
			driver.get("http://www.google.com")
			que = driver.find_element_by_name("q")
			que.send_keys(str(you))
			que.send_keys(Keys.RETURN)
			speak("There you go sir!")
			break

def search_ytb():
	while True:
		you = hear()
		if you == "":
			speak("Is there any video you want to search for sir?")
		if "search for" in you:
			text = you.split("search for", 1)[1]
			results = YoutubeSearch(text, max_results=10).to_dict()
			if results:
				break
		if "Vietnamese" in you:
			speak("Switch to searching YouTube in Vietnamese successfully! What are you looking for sir?")
			you = hear_vie()
			text = you.split("search for", 1)[1]
			results = YoutubeSearch(text, max_results=10).to_dict()
			if results:
				break
		else:
			results = YoutubeSearch(you, max_results=10).to_dict()
			if results:
				break
	url = 'https://www.youtube.com' + results[1]['url_suffix']
	webbrowser.open(url)
	speak("There you go sir! Enjoy!")
	raise SystemExit(0)

def play_game():
	speak("Your wish is my command!")
	os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks 5.lnk")
	

while True:
	you = hear()
	if you == "":
		speak("Is there anything you want me to help sir?")
	elif "website" in you:
		speak("Can you tell me the website which you want to open sir?")
		website(you)
	elif "Wikipedia" in you:
		speak("What information do you want me to find sir?")
		tell_me_about()
	elif "date" in you:
		today()
	elif "time" in you:
		time()
	elif "Google" in you:
		speak("What do you want me to search for sir?")
		search_google()
	elif "YouTube" in you:
		speak("What video do you want to search on Youtube sir?")
		search_ytb()
	elif "game" in you:
		play_game()
	elif "stop" in you:
		speak("OK sir!")
		break
	elif "goodbye" in you:
		speak("Goodbye sir! Have a nice day!")
		break
	else:
		speak("Sorry, I'm afraid I can't meet your command sir!")