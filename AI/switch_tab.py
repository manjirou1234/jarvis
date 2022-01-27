import pyautogui
import speech_recognition

jarvis_ear = speech_recognition.Recognizer()

def hear():
	with speech_recognition.Microphone() as mic:
		audio = jarvis_ear.listen(mic, phrase_time_limit=1)
	try:
		you = jarvis_ear.recognize_google(audio)
		return you
	except:
		you = ""
		return you

def switch_window():
	while True:
		pyautogui.keyDown("alt")
		pyautogui.press("tab")
		command = hear()
		if "stop" in command:
			pyautogui.keyUp("alt")
			break

switch_window()