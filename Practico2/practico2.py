# pip install opencv-python

import cv2
img= cv2.imread("hoja.png",0)
print(type(img))
print(str(img.shape[0])+"x"+str(img.shape[1]))

for fila in range (img.shape[0]):

    for columna in range (img.shape[1]):
        if img[fila][columna]!=255:
            img[fila][columna]=0
        

cv2.imwrite("Resultado.png",img)