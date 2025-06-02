#Mario Gerardo Casas Miramontes 22310165
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)#Cambiamos de BGR a HSV

    #Rango de deteccion del color rojo
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    #Mascara tomando los rangos de color
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #Aplicacion binaria
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #Matriz que permite la eliminacion de ruido
    kernel = np.ones((5,5), np.uint8)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #Elimina puntos blankos asilados
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #Rellena zonas negras
    tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel)
    #Resalta detalles brillantes
    blackhat = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel)
    #Oscurece zonas

    res = cv2.bitwise_and(frame, frame, mask=closing)
     
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Opening', opening)
    cv2.imshow('Closing', closing)
    cv2.imshow('Top Hat', tophat)
    cv2.imshow('Black Hat', blackhat)
    cv2.imshow('Resultado Final', res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:  # Tecla ESC para salir
        break

cv2.destroyAllWindows()
cap.release()
