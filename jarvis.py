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
import sys
import random
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate , Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUI import Ui_MainWindow

jarvis_ear = speech_recognition.Recognizer()
jarvis_brain = ""
wikipedia.set_lang("en")
path = ChromeDriverManager().install()
s = Service(path)
RESPONSES = ["Right away sir!", "Your wish is my command!", "As you wish sir!", "I'm on it sir!", "Processing!"]

def hear():
	speak("I'm listening")
	with speech_recognition.Microphone() as mic:
		audio = jarvis_ear.listen(mic, phrase_time_limit=5)
	try:
		you = jarvis_ear.recognize_google(audio)
		return you
	except:
		you = ""
		return you

def hear_vie():
	with speech_recognition.Microphone() as mic:
		audio = jarvis_ear.listen(mic, phrase_time_limit=6)
	try:
		you = jarvis_ear.recognize_google(audio, language='vi-VN')
		return you
	except:
		you = ""
		return you

def speak(jarvis_brain):
	jarvis_mouth = pyttsx3.init("sapi5")
	voices = jarvis_mouth.getProperty('voices')
	rate = jarvis_mouth.getProperty('rate')

	jarvis_mouth.setProperty('voices', voices[0].id)
	jarvis_mouth.setProperty('rate', 140)
		
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
			speak(random.choice(RESPONSES))
		else:
			speak("Sorry sir! I'm afraid the website you want is unable to be found! Please try again sir")
	else:
		try:
			url = 'https://www.' + you + '.com'
			webbrowser.open(url)
			speak(random.choice(RESPONSES))
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
			speak(random.choice(RESPONSES))
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
					speak(random.choice(RESPONSES))
					break
		elif "stop" in you:
			speak(random.choice(RESPONSES))
			break
		elif you == "":
			speak("Is there anything you want me to search in Google sir?")
		else:
			driver = webdriver.Chrome(service=s)
			driver.get("http://www.google.com")
			que = driver.find_element_by_name("q")
			que.send_keys(str(you))
			que.send_keys(Keys.RETURN)
			speak(random.choice(RESPONSES))

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
			results = YoutubeSearch(you, max_results=10).to_dict()
			if results:
				break
		else:
			results = YoutubeSearch(you, max_results=10).to_dict()
			if results:
				break
	url = 'https://www.youtube.com' + results[1]['url_suffix']
	webbrowser.open(url)
	speak(random.choice(RESPONSES))

def play_game():
	speak(random.choice(RESPONSES))
	os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks 5.lnk")

def open_folder():
	speak("Which folder do you want to open sir?")
	while True:
		you = hear_vie()
		try:
			os.startfile("C:\\Users\\Phuc Nhat\\Documents\\" + you)
			speak(random.choice(RESPONSES))
			break
		except:
			speak("Sorry sir! I'm afraid the folder you want is unable to be found!")

def drive_google():
	webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
	speak(random.choice(RESPONSES))

def python_program():
	os.startfile('D:\\Laptrinhpython')
	speak(random.choice(RESPONSES))

def play_music():
	speak("What kind of music do you want me to play sir?")
	while True:
		you = hear_vie()
		if you == "":
			speak("What kind of music do you want me to play sir?")
		if "nhạc điện tử" in you:
			num = random.randint(0,14)
			music_dir = 'C:\\Users\\Phuc Nhat\\Music\\EDM'
			songs = os.listdir(music_dir)
			speak(random.choice(RESPONSES))
			os.startfile(os.path.join(music_dir,songs[num]))
			break
		if "Yugioh" in you:
			num = random.randint(0,7)
			music_dir = 'C:\\Users\\Phuc Nhat\\Music\\Yu-Gi-Oh'
			songs = os.listdir(music_dir)
			speak(random.choice(RESPONSES))
			os.startfile(os.path.join(music_dir,songs[num]))
			break
		if "remix" in you:
			num = random.randint(0,5)
			music_dir = 'C:\\Users\\Phuc Nhat\\Music\\remix'
			songs = os.listdir(music_dir)
			speak(random.choice(RESPONSES))
			os.startfile(os.path.join(music_dir,songs[num]))
			break
		else:
			num = random.randint(0,14)
			music_dir = 'C:\\Users\\Phuc Nhat\\Music\\EDM'
			songs = os.listdir(music_dir)
			speak(random.choice(RESPONSES))
			os.startfile(os.path.join(music_dir,songs[num]))
			break

def open_application():
	while True:
		you = hear()
		try:
			if you == "":
				speak("Which app do you want me to open sir?")
			if "open" in you or "run" in you:
				reg_ex = re.search('open (.+)' or 'run (.+)', you)
				text = reg_ex.group(1)
				speak(random.choice(RESPONSES))
				os.startfile("C:\\Users\\Phuc Nhat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\" + text + ".lnk")
				break
			else:	
				os.startfile("C:\\Users\\Phuc Nhat\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs" + you + ".lnk")
				speak(random.choice(RESPONSES))
				break
		except:
			speak("I’m afraid I can’t quite heard what you said! Please try again sir!")

def funtion():
	speak("I can perform various features such as Access to the internet, search Wikipedia, tell the current time and date, search Google, open a video from YouTube, open game, open Google Drive and play a music. How can I help you?")

def greeting():
	speak("I am Jarvis. Online and ready sir! Please tell me how I may help you?")

class JarvisAssistant(QThread):
	def __init__(self):
		super(JarvisAssistant, self).__init__()

	def run(self):
		self.brain()

	def brain(self):
		while True:
			you = hear()
			if you == "":
				speak("Is there anything you want me to help sir?")
			elif "internet" in you:
				speak("Can you tell me the website which you want to open sir?")
				website(you)
			elif "Wikipedia" in you:
				speak("What information do you want me to find sir?")
				tell_me_about()
			elif "date" in you:
				today()
			elif "time" in you:
				time()
			elif "search Google" in you:
				speak("What do you want me to search for sir?")
				search_google()
			elif "YouTube" in you:
				speak("What video do you want to search on Youtube sir?")
				search_ytb()
				break
			elif "game" in you:
				play_game()
			elif "folder" in you:
				open_folder()
			elif "program" in you:
				python_program()
			elif "Google Drive" in you:
				drive_google()
			elif "music" in you:
				play_music()
				break
			elif "application" in you:
				speak("Which app do you want to open sir?")
				open_application()
				break
			elif "hello" in you:
				greeting()
			elif "what you can do" in you:
				funtion()
			elif "stop" in you:
				speak(random.choice(RESPONSES))
				break
			elif "goodbye" in you:
				speak("Goodbye sir! Have a nice day!")
				break
			else:
				speak("Sorry, I'm afraid I can't meet your command sir!")

startExecution = JarvisAssistant()

class screen(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.SystemStart)

	def __del__(self):
		sys.stdout = sys.__stdout__

	def SystemStart(self):
		startExecution.start()

app = QApplication(sys.argv)
jarvis = screen()
jarvis.show()
sys.exit(app.exec_())
