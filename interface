from tkinter import *
from PIL import Image, ImageTk
import cv2
import sys
import numpy as np
import uuid

def onClossing():
    root.quit()
    cap.release()
    print("Camara desconectada")
    root.destroy()
def callback():
    ret, frame = cap.read()
    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img.thumbnail((400,400))
        tkimage = ImageTk.PhotoImage(img)
        label.configure(image=tkimage)
        label.image = tkimage
        root.after(1,callback)
    else:
        onClossing()

url = "http://192.168.0.6:4747/video"
cap = cv2.VideoCapture(0)


if cap.isOpened():
    print("Camara Iniciada")
else:
    sys.exit("camara desconectada")

def foto():
    print("foto")
def reset():
    print("hola")

root = Tk()
root.protocol("WM_DELETE_WINDOW", onClossing)
root.config(bg="gray")
root.title("Traductor")

label = Label(root)
label.grid(column=0, row=1)
label1 = Label(root)
label1.grid(column=1, row=1)

button1 = Button(root, text="Tomar Foto", command=foto)
button1.grid(column=0, row=2)
button2 = Button(root, text="Reutilizar", command=reset)
button2.grid(column=1, row=2, padx=20)

root.after(1,callback)

root.mainloop()
