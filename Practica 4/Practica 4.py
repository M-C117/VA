#Mario Gerardo Casas Miramontes 22310165
import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR) #Asignamos lo que es la imagen que usaremos
cv2.line(img,(0,0),(200,300),(255,255,255),5)#Creamos la linea asignando en donde se dibujara, el origen, el color y el grosor
cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
cv2.circle(img,(44,63), 63, (0,255,0), -1)
pts = np.array([[10,50],[20,30],[70,20]], np.int32) #Generamos los puntos entre los cuales se generar un poligono
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)#Se crea el poligono el cual tomara los puntos y los unira
font = cv2.FONT_HERSHEY_SIMPLEX #Usamos esta funcion para añadir la fuente en la que se hara el texto
x, y, w, h = 10, 50, 200, 150 #Declaramos X, Y, Ancho y altura
cv2.putText(img,'22310165!',(10,50), font, 1, (200,255,155), 4, cv2.LINE_AA)#Con esta funcion podemos insertar el texto en una imagen en  donde decimos donde sera, el texto, la fuente y las caracteristicas que queramos poner como color, grosor, etc
roi = img[y:y+h, x:x+w]#Seccionamos la imagen para generar la region de interes
cv2.imshow('ROI', roi)#Mostramos la region de interes
cv2.imshow('image',img)#Mostramos la imagen con los dibujos
cv2.waitKey(0)
cv2.destroyAllWindows()
