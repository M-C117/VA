#Mario Gerardo Casas Miramontes 22310165

import cv2
import numpy as np

img_rgb = cv2.imread('Principal.jpg')
img_gray2 = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('Busqueda.jpg',0)
w, h = template.shape[::-1]  #El tamaño del parentezco
res = cv2.matchTemplate(img_gray2,template,cv2.TM_CCOEFF_NORMED) #Funcion para buscar similitudes entre las imagenes
threshold = 0.85 #Grado de parentezco
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):  #Genero bloques par marcar la zona de interes
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.imshow('Detected',img_rgb)
