import numpy as np #
import cv2
import sys
import math

def transformacion(rows,cols):
    # Transformacion Euclideana
    print("\nIngrese los parametros:\n")

    angle=float(input("\nÁngulo:\t"))

    tx=float(input("Traslacción en X:\t"))

    ty=float(input("Traslacción en Y:\t"))

    #La Transformación euclidea
    # se reliza en 2 parte separadas, 
    # cada una representando una
    #parte de la transformacion:
    # rotación y traslación

    #ROTACIÓN
    M_1 = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1) 
    # la función cv2.getRotationMatrix2D crea la matriz
    # M_1  que corresponde a la rotación

    #TRASLACIÓN
    M_2 = np.float32([[1,0,tx],[0,1,ty]])
    # la función np.float32 crea la matriz
    # M_2  que corresponde a la traslación

    dst_1 = cv2.warpAffine(img,M_1,(cols,rows)) #ROTACIÓN
    dst_2= cv2.warpAffine(dst_1,M_2,(cols,rows)) #TRASLACIÓN
    # cv2.warpAffine realiza la transformación
    # el primer elemento es el objetivo de la transofrmacion
    # el segundo es la matriz, en este caso se suman las dos
    # matrices para realizar tanto la rotación 
    # como la traslación
    # el tercer argumento dela función cv2.warpAffine
    # define tamaño de imagen de salida
    return (dst_2)


#CODIGO PRINCIPAL 
# Recibir imagen
if(len(sys.argv)> 1):
    filename = sys.argv[1]  #Toma como argumento aquel acompañado en el comando
else :
    print('El nombre no corresponde con un archivo de imagen existente en la carpeta')  #Sino tengo argumento lo cierra
    sys.exit(0)

img = cv2.imread(filename)
rows,cols= img.shape[0:2]

res=transformacion(rows,cols)


cv2.imshow('img',res)

key = cv2.waitKey(); 

if key is '0': cv2.destroyAllWindows()

elif key is'e': cv2.destroyAllWindows()
