# Mario Gerardo Casas Miramontes 22310165
import numpy as np
import cv2

img = cv2.imread('IMG1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Detección de esquinas
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = corners.astype(int)

# Dibujar círculos
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, 255, -1) 


cv2.imshow('Corners', img)

