import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from PIL import Image
import cv2
import uuid

longitud, altura = 100 , 100
modelo = './modelo/modelo.h5'
pesos= './modelo/pesos.h5'
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

#tomar foto desde webcam
cap = cv2.VideoCapture(0)
flag = cap.isOpened()
while(flag):
    ret, frame = cap.read()
    cv2.imshow("Learn-Cam",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord (' '): #Presione la tecla espacio para ingresar a la siguiente operación de guardado de imágenes
        namePhoto = str(uuid.uuid4())
        cv2.imwrite("./camara/photos/" + namePhoto + ".jpg", frame)
        cv2.imshow("./camara/photos/" + namePhoto + ".jpg", frame)
    elif k == ord ('q') or k == ord('Q'): #Presione la tecla q, el programa sale
        break
cap.release()
cv2.destroyAllWindows()
#hacer la predicción
predict("./camara/photos/" + namePhoto + ".jpg")
