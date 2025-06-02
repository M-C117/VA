#Mario Gerardo Casas Miramontes 22310165
import cv2
import numpy as np

# Cargar imagen en escala de grises
img = cv2.imread('imagen.jpg', cv2.IMREAD_GRAYSCALE)

# Suavizar para reducir el ruido
blur1 = cv2.GaussianBlur(img, (3, 3), 0) #Metodo para suavizar la imagen

# Laplaciano
laplacian = cv2.Laplacian(blur1, cv2.CV_64F) #Se encarga de aplicar el metodo Laplacian , evitando la saturacion de metodos negativos
laplacian = cv2.convertScaleAbs(laplacian) #Usa los valores de blanco y negro para la imagen
# Sobel en X y Y
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # dx=1, dy=0 y se encarga de los bordes verticales
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # dx=0, dy=1 y se encarga de los bordes horizontales
# Convertir a uint8
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
# Aplicar suavizado
blur2 = cv2.GaussianBlur(img, (5, 5), 1.4) #Suavizamos la imagen
# Canny
edges = cv2.Canny(blur2, threshold1=50, threshold2=150) 
#Este es el metodo mas complejo porque hace un calculo de gradiente en donde si supera el valor del Thershold
#Si se encuentra encima del 150 se dibuja, pero si es menor que 50 es ruido y se elimina.

# Mostrar resultados
cv2.imshow("Canny", edges)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Laplaciano", laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()
