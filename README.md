# Youtube-Video-Downloader

The Youtube video downloader is a project that aims at downloading any type of video from Youtube in a fast, simple and easy way.
The user has to paste the Youtube Video link and click download button to download the video.
To implement this project we use basic concept of **python**,**tkinter** and **pytube library**

**Tkinter** is a standard GUI library for building GUI applications

**Pytube** is used for downloading videos from youtube.

To install the required modules run pip installer on the command line

* *pip install tkinter*

* *pip install pytube*

## Steps to build Youtube Video Donloader in Python
* Import Libraries.
* Create Display Window.
* Create field to Enter Link.
* Create Function to start downloading.

##  Import Libraries

```
from tkinter import *
from pytube import Youtube
```
#### Create Display Window
```
root = Tk() 
root.geometry('500x300')
root.resizable(0, 0) 
root.title("Youtube Video Downloader")
Label(root, text='Youtube Video Downloader', font='arial 20 bold', bg='Red').pack()
```
**Tk()** used to intialize tkinter to create window

**geometry()** used to set windows width and height

**resizable** sets the fixs size of window

**title()** used to give title of the window

**root** is the name of the window

**label()** widget used to display text that users can't edit

**pack** is an organized widget in block

## Create Field to Enter Link
```
link = StringVar()
Label(root, text='Paste Link Here', font='verdana 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)
```
**Link()**  is a variable that stores youtube video link that user enters

**Entry()**  is widget for creating an input text field

**Width** sets the width of entry widget

**TextVariable** is used to retrieve the value of current text variable to the entry widget

**Place()**  places the widget at specidic position

## Create a function to start Downloading

```
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='Downloaded', font='verdana 15').place(x=180, y=210)


Button(root, text='DOWNLOAD', font='verdana 15 bold', bg='Blue', padx=2, command=downloader).place(x=180,
                                                                                                   y=150)
root.mainloop()
```
*  url variable gets youtube link using **get()** function and **str()** will convert link in string datatype

**Button()** widget displays the download button on the window

**text** which we display on the label

**font**specific size and style in which the text is written

**bg** sets the background color

**command** is used to call the function

**SUMMARY**
With this simple project we have successfully developed youtube video downloader using python.We have used the popular tkinter library.Tkinter is a standard GUI library for python that provides a fast and easy way to build GUI applications.
We have also used pytube.pytube is a lightweight, Pythonic, dependency-free, library (and command-line utility) for downloading YouTube Videos.








