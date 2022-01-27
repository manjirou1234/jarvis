from PIL import ImageGrab
from PIL import Image

screenshot = ImageGrab.grab()
name = "test"
save_path = "C:\\Users\\Phuc Nhat\\Pictures\\Screenshots\\" + name + ".jpg"
screenshot.save(save_path)

image = "C:\\Users\\Phuc Nhat\\Pictures\\Screenshots\\" + name + ".jpg"
img = Image.open(image)
img.show()