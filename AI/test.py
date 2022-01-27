import speech_recognition

jarvis_ear = speech_recognition.Recognizer()

def hear():
    with speech_recognition.Microphone() as mic:
        audio = jarvis_ear.listen(mic, phrase_time_limit=3)
    try:
        you = jarvis_ear.recognize_google(audio)
        print("you:", you)
    except:
        you = ""
        print("you:", you)

hear()