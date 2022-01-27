from gtts import gTTS
import os
import time
from datetime import date
from datetime import datetime
import webbrowser
import speech_recognition
import wikipedia
import playsound

now = datetime.now()
Liz_ear = speech_recognition.Recognizer()
wikipedia.set_lang("vi")
Liz_brain = ""

while True:
	def speak(Liz_brain):
		print("Liz: ", Liz_brain)
		tts = gTTS(Liz_brain, lang = "vi", slow=False)
		tts.save("output.mp3")
		playsound.playsound("output.mp3", True)
		os.remove("output.mp3")

	with speech_recognition.Microphone() as mic:
		print("Liz: Trợ lý ảo Liz xin được nghe lệnh")
		audio = Liz_ear.listen(mic, timeout=3, phrase_time_limit=3)

	try:
		you = Liz_ear.recognize_google(audio, language='vi-VN')
	except:
		you = ""		

	if you == "":
		speak("Tôi chưa nghe rõ. Xin hãy lặp lại mệnh lệnh")
		time.sleep(3) 
	elif "ngày" in you:
		speak("Hôm nay là ngày %d tháng %d năm %d" % (now.day, now.month, now.year))
		time.sleep(4)
	elif "giờ" in you:
		speak("Bây giờ là %d giờ %d phút và %d giây" % (now.hour, now.minute, now.second))
		time.sleep(4)
	elif "thông tin" in you:
		speak("Bạn muốn tìm thông tin về cái gì ạ?")
		time.sleep(3)
		while True:
			with speech_recognition.Microphone() as mic:
				audio = Liz_ear.listen(mic, timeout=3, phrase_time_limit=3)
			try:
				you = Liz_ear.recognize_google(audio, language='vi-VN')
			except:
				you = ""

			speak(wikipedia.summary(you, sentences=3))
			time.sleep(20)
			break
		break
	elif "hóa học" in you:
		os.startfile('C:\\Users\\Phuc Nhat\\Documents\\Hóa - Tùng Tùng')
		speak("tới giờ học hóa thôi nào!")
		time.sleep(3)
		break
	elif "lập trình" in you:
		os.startfile('D:\\Laptrinhpython\\AI')
		speak("chào mừng ngài quay trở lại với công việc của mình!")
		time.sleep(4)
		break
	elif "nhạc không lời" in you:
		webbrowser.open("https://www.youtube.com/watch?v=Ljd1hSnslic", new=1)
		speak("nhạc nhẹ cho ngài nghe đây")
		time.sleep(3)
		break
	elif "xem phim" in you:
		webbrowser.open("https://www.youtube.com/", new=1)
		speak("youtube sẽ phục vụ ngài")
		time.sleep(3)
		break
	elif "mạng xã hội" in you:
		webbrowser.open("https://www.facebook.com/", new=1)
		speak("Facebook đã được mở")
		time.sleep(2)
		break
	elif "bộ nhớ đám mây" in you:
		webbrowser.open("https://drive.google.com/drive/u/1/my-drive", new=1)
		speak("google drive đã được mở")
		time.sleep(3)
		break
	elif "tài liệu trên mạng" in you:
		webbrowser.open("https://github.com/pathakabhi24/Hacking-related-books/find/master")
		speak("Tài liệu trên mạng đã có")
		time.sleep(3)
		break
	elif "nhạc hay" in you:
		webbrowser.open("https://www.youtube.com/watch?v=YBH1fSahMw4&list=RDMMYBH1fSahMw4&index=1")
		speak("kho nhạc mà ngài yêu thích đã được bật")
		time.sleep(3)
		break
	elif "tạm biệt" in you:
		speak("xin chào tạm biệt ngài. Hẹn gặp lại")
		time.sleep(4)
		break
	else:
		speak("lệnh này tôi xin phép không thể đáp ứng")
		time.sleep(3)


