import wikipedia

wikipedia.set_lang("vi")
Liz_brain = wikipedia.summary("facebook", sentences=1)

print(Liz_brain)