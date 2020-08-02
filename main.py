from pygame import *
from pygame import mixer
from tkinter import *
from mutagen.id3 import ID3
from tkinter.filedialog import askdirectory
import os


root = Tk()
root.title("Music Player")
root.geometry("400x300")
mixer.init()
mixer.music.load("music.mp3")

listofsongs = []
index = 0
realnames = []
def choosemusic():
    directory = askdirectory()
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)       # the whole path
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])

            listofsongs.append(files)
    mixer.init()
    mixer.music.load(listofsongs[0])
   # mixer.music.play()

def nextsong(event):
    global index
    try:
        if index + 1 > len(listofsongs):
            raise IndexError
        index += 1
        mixer.music.load(listofsongs[index])
        mixer.music.play()
    except IndexError:
        print("No more songs left !!!")


def prevsong(event):
    global index
    try:
        if index == 0:
            raise IndexError
        index -= 1
        mixer.music.load(listofsongs[index])
        mixer.music.play()
    except IndexError:
        print("This is the first song !!!")


def play():
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

Label(root,text = "Welcome !", font = "Lucidia 30 bold").pack()
btn1=Button(root , text = "Play" , command = play,font = "Helvetica").place(x = 20 , y = 200)



choosemusic()
listbox = Listbox(root)
listbox.pack()
for items in listofsongs:
    listbox.insert(0,items)
nextbutton = Button(root , text = "Next Song")
nextbutton.pack()
nextbutton.bind("<Button-1>" , nextsong) #button-1 means left click , button-2 the scroll , button-3 right click

previousbutton = Button(root , text = "Previous Song")
previousbutton.pack()
previousbutton.bind("<Button-1>" , prevsong)


Button(root , text = "Pause" , command = pause).place(x = 20 , y = 250)
Button(root , text = "Resume" , command = resume).place(x = 300 , y = 100)
Button(root , text = "Quit" , command = quit).place(x = 350 , y = 100)
try:
    if len(listofsongs) < index+1:
        raise IndexError
except IndexError:
    print("Index out of bonds")
root.mainloop()