import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog,messagebox

def createwidgets():
    link_label = Label(root,text="Youtube url : ",bg="green")
    link_label.grid(row=1,column=0,pady=5,padx=5)
    root.link_text = Entry(root,width=60,textvariable=video_link)
    root.link_text.grid(row=1,column=1,pady=5,padx=5)
    destination_label = Label(root,text="Destination : ",bg="purple")
    destination_label.grid(row=2,column=0,pady=5,padx=5)
    root.destination_text=Entry(root,width=45,textvariable=download_path)
    root.destination_text.grid(row=2,column=1,pady=3,padx=3)
    browse_but = Button(root,text="Browse",command=browse , width=10,bg="blue")
    browse_but.grid(row=2,column=2,pady=1,padx=1)
    download_but = Button(root,text="Download Video",command=download,width=25,bg="#05E8E0")
    download_but.grid(row=3,column=1,pady=3,padx=3)

def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory path")
    download_path.set(download_dir)
def download():
    url=video_link.get()
    folder = download_path.get()
    getvideo = YouTube(url)
    get_stream = getvideo.streams.first()
    get_stream.download(folder)
    messagebox.showinfo("successfully downloaded")

root=tk.Tk()
root.iconbitmap("yt.ico")
root.geometry("600x120")
root.resizable(False,False)
root.title("YouTube Video Downloader")
root.config(background="#000000")
video_link=StringVar()
download_path = StringVar()
createwidgets()

root.mainloop()