import cv2
import numpy as np
import uuid

cap = cv2.VideoCapture(0)
flag = cap.isOpened()

while(flag):
    ret, frame = cap.read()
    cv2.imshow("Learn-Cam",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord (' '): #Presione la tecla espacio para ingresar a la siguiente operación de guardado de imágenes
        namePhoto = str(uuid.uuid4())
        cv2.imwrite("./photos/" + namePhoto + ".jpg", frame)
        print(cap.get(3))
        print(cap.get(4))
        cv2.imshow("./photos/" + namePhoto + ".jpg", frame)
    elif k == ord ('q') or k == ord('Q'): #Presione la tecla q, el programa sale
        break

cap.release()
cv2.destroyAllWindows()

original = cv2.imread("../Frutas/naranja1.jpg")
image_to_compare = cv2.imread("./photos/" + namePhoto + ".jpg")

# 1) Verificamos si las dos imagenes son iguales
if original.shape == image_to_compare.shape:
    print('Las imagenes tiene el mismo tamaño y canal')
    difference = cv2.subtract(original, image_to_compare)
    b, g, r = cv2.split(difference)
    print(cv2.countNonZero(b))
    if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0):
        print('Las imagenes son completamente iguales')
    else: 
        print('Las imagenes no son iguales')

# 2) Check para la similitud de las dos imagenes
shift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = shift.detectAndCompute(original, None)
kp_2, desc_2 = shift.detectAndCompute(image_to_compare, None)

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

result = cv2.drawMatches(original, kp_1, image_to_compare, kp_2, good_points, None)
cv2.imshow("Result", cv2.resize(result, None, fx = 0.4, fy=0.4))
cv2.imwrite("./feature_matching/Feature_matching.jpg", result)

cv2.imshow("Fotografia", original)
cv2.imshow("Imagen Analizada", image_to_compare)
cv2.waitKey(0)
cv2.destroyAllWindows()