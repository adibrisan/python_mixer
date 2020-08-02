from pygame import mixer
from tkinter import *

root = Tk()
root.title("Music Player")
root.geometry("400x300")
mixer.init()
mixer.music.load("music.mp3")
def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

Label(root,text = "Welcome !", font = "Lucidia 30 bold").pack()
Button(root , text = "Play" , command = play).place(x = 20 , y = 200)
Button(root , text = "Pause" , command = pause).place(x = 20 , y = 250)
Button(root , text = "Resume" , command = resume).place(x = 300 , y = 100)
Button(root , text = "Quit" , command = quit).place(x = 350 , y = 100)

root.mainloop()