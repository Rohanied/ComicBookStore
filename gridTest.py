from tkinter import *
from PIL import ImageTk, Image
from tkinter.scrolledtext import ScrolledText

def ShowImage(imageName):

    base = Toplevel()
    image = Image.open(imageName)
    photo = ImageTk.PhotoImage(image)
    img_label = Label(base, image=photo)
    img_label.pack()
