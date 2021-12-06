#programación detección de frutas
import cv2
import numpy as np
import uuid

#capturar imagen desde webcm
cap = cv2.VideoCapture(0)
flag = cap.isOpened()

while(flag):
    ret, frame = cap.read()
    cv2.imshow("Learn-Cam",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord (' '): #Presione la tecla espacio para ingresar a la siguiente operación de guardado de imágenes
        namePhoto = str(uuid.uuid4())
        cv2.imwrite("./camara/photos/" + namePhoto + ".jpg", frame)
        print(cap.get(3))
        print(cap.get(4))
        cv2.imshow("./camara/photos/" + namePhoto + ".jpg", frame)
    elif k == ord ('q') or k == ord('Q'): #Presione la tecla q, el programa sale
        break

cap.release()
cv2.destroyAllWindows()

#imagenes a utilizar
image_camera = cv2.imread("./camara/photos/" + namePhoto + ".jpg")
pera_original = cv2.imread('./Frutas/pera.jpg')
img_pera_lsm = cv2.imread('./Frutas/pera-lsm.png',255)

#------------------------TRATAMIENTO DE IMÁGENES-----------------------------------
#escala de grises
img_camera_gray= cv2.cvtColor(image_camera,cv2.COLOR_BGR2GRAY)
img_pera_gray = cv2.cvtColor(pera_original,cv2.COLOR_BGR2GRAY)

#reescalamiento
res_cam=cv2.resize(img_camera_gray,(550,530),interpolation=cv2.INTER_CUBIC)
res1=cv2.resize(img_pera_gray,(550,530),interpolation=cv2.INTER_CUBIC)
res1lsm=cv2.resize(img_pera_lsm,(550,530),interpolation=cv2.INTER_CUBIC)

#filtro por gausiano 
blur1 = cv2.GaussianBlur(res1,(5,5),0)
blur_cam= cv2.GaussianBlur(res_cam,(5,5),0)

#método por umbral 
_,bin1 =cv2.threshold(blur1,240,255,cv2.THRESH_BINARY)
_,bin_cam =cv2.threshold(blur_cam,210,255,cv2.THRESH_BINARY)

# Check para la similitud de las dos imágenes
shift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = shift.detectAndCompute(bin1, None)
kp_2, desc_2 = shift.detectAndCompute(bin_cam, None)

print("Keypoints 1st image", str(len(kp_1)))
print("Keypoints 2st image", str(len(kp_2)))

index_params = dict(algorithm=0, trees=5)
search_params = dict()

flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(desc_1, desc_2, k=2)

good_points = []
for m, n in matches:
    if m.distance < 0.6*n.distance:
        good_points.append(m)

number_keypoints = 0
if (len(kp_1) <= len(kp_2)):
    number_keypoints = len(kp_1)
else:
    number_keypoints = len(kp_2)

print("GOOD matches",len(good_points))
print("Que tan bueno es el match", len(good_points) / number_keypoints * 100, "%")

result = cv2.drawMatches(bin1, kp_1, bin_cam, kp_2, good_points, None)
cv2.imshow("Result", cv2.resize(result, None, fx = 0.4, fy=0.4))
cv2.imwrite("./feature_matching/Feature_matching.jpg", result)


# mostrar imagen en lsm
#cv2.imshow('imagen lsm',res1lsm)

cv2.waitKey(0)
cv2.destroyAllWindows