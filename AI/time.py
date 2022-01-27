from datetime import datetime

now = datetime.now()
Liz_brain = now.strftime("%H hours %M minutes and %S seconds")

print(Liz_brain)