from tkinter import *
from PIL import Image, ImageTk
import cv2
import sys
import time


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

def foto():
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    if ret:
        cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".png", img)


def reset():
    print("hola")

url = "http://192.168.0.6:4747/video"
cap = cv2.VideoCapture(url)

if cap.isOpened():
    print("Camara Iniciada")
else:
    sys.exit("camara desconectada")

root = Tk()
root.protocol("WM_DELETE_WINDOW", onClossing)
root.config(bg="gray")
root.title("Traductor")

label = Label(root)
label.grid(column=0, row=1)

label1 = Label(root)
label1.grid(column=1, row=1)

button1 = Button(root, text="Tomar Foto", command=foto)
button1.grid(column=0, row=2, pady=20)

button2 = Button(root, text="Reiniciar", command=reset)
button2.grid(column=1, row=2, padx=20)

button2 = Button(root, text="Salir", command=quit)
button2.grid(column=1, row=4, padx=5, pady=20)

root.after(1,callback)

root.mainloop()
