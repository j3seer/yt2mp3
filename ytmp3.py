import tkinter as tk
from tkinter import *
import tkinter.messagebox
import pytube
import os

root = Tk()

def popup(title,info):
    tk.messagebox.showinfo(title,info)

def download_video(url):
    try:
        itag = 137
        video = pytube.YouTube(url.get())
        popup("In progress..","Downloading "+url.get()+"...")
        stream = video.streams.filter(only_audio=True).first() 
        filename = stream.default_filename
        stream.download()
        base, ext = os.path.splitext(filename)
        new_file = base + '.mp3'
        os.rename(filename, new_file)
        popup("Done","Finished downloading!")
    except:
        popup("ERROR","There was an error somewhere..")



root.title("yt to mp3")
root.geometry("800x100")

l = Label(root, text = "Submit URL")
l.config(font=("Arial", 14))

url = Entry(root,width=50,font=("Arial",15))

download = Button(root,width=50,text="Downloading MP3",command=lambda:download_video(url),font=("Arial",15))

l.pack()
url.pack()
download.pack()



root.mainloop()
                                  

