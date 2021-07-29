from pytube import YouTube
from tkinter import *

# Create a display window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("@Phy Youtube Video Downloader")
Label(root, text='Youtube Video Downloader', font='arial 20 bold', bg='Red').pack()

# Create Field to enter link
link = StringVar()
Label(root, text='Paste Link Here', font='verdana 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


# Create a function to start downloading
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Downloaded', font='verdana 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='verdana 15 bold', bg='Blue', padx=2, command=downloader).place(x=180,
                                                                                                   y=150)
root.mainloop()
