import os
import random

song_num = random.randint(0,5)
music_dir = 'C:\\Users\\Phuc Nhat\\Music\\remix'
songs = os.listdir(music_dir)
os.startfile(os.path.join(music_dir,songs[song_num]))