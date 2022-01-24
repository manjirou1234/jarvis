import speech_recognition

Liz_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Liz: Tôi đang lắng nghe")
	audio = Liz_ear.listen(mic, timeout=3, phrase_time_limit=3)

try:
	you = Liz_ear.recognize_google(audio, language='vi-VN')
except:
	you = ""

print("you: " + you)
