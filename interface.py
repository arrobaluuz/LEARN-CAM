from tkinter import *
from PIL import ImageTk
import sys
import time

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from PIL import Image
import cv2

longitud, altura = 100 , 100
modelo = './modelo/modelo.h5'
pesos='./modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos)

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    im = Image.open('./LSM/mango-lsm.png')
    im.show()

  elif answer == 1:
    im = Image.open('./LSM/manzana-lsm.png')
    im.show()
  elif answer == 2:
    im = Image.open('./LSM/pera-lsm.png')
    im.show()
  elif answer == 3:
    im = Image.open('./LSM/platano-lsm.png')
    im.show()
  return answer

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
    if ret:
        cv2.imwrite("./camara/photos/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".png", frame)
        predict("./camara/photos/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".png")

def reset():
    print("hola")

url = "http://192.168.1.74:4747/video"
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
