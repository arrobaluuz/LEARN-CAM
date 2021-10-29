import cv2

cap = cv2.VideoCapture(0)

leido, frame = cap.read()

if leido == True:
	cv2.imwrite("foto.jpeg", frame)
	print("Foto tomada correctamente")
else:
	print("Error al acceder a la cámara")

cap.release()
