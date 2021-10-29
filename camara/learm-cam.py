import cv2
import uuid

cap = cv2.VideoCapture(0)
flag = cap.isOpened()

while(flag):
    ret, frame = cap.read()
    cv2.imshow("Learn-Cam",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord (' '): #Presione la tecla espacio para ingresar a la siguiente operación de guardado de imágenes
        cv2.imwrite("./images/" + str(uuid.uuid4()) + ".jpg", frame)
        print(cap.get(3))
        print(cap.get(4))
    elif k == ord ('q') or k == ord('Q'): #Presione la tecla q, el programa sale
        break

cap.release()
cv2.destroyAllWindows()