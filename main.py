from pygame import mixer
from tkinter import *

root = Tk()
root.title("Music Player")
root.geometry("400x300")
mixer.init()
mixer.music.load("filename.mp3")


root.mainloop()