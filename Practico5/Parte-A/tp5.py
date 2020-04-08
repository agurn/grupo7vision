

import numpy as np 
import cv2
import sys
import math

# Recibir imagen
if(len(sys.argv)> 1):
    filename = sys.argv[1]  #Toma como argumento aquel acompanado en el comando
else :
    print('El nombre no corresponde con un archivo de imagen existente en la carpeta')  #Sino tengo argumento lo cierra
    sys.exit(0)


img = cv2.imread(filename,0)
img2 = cv2.imread(filename)
rows,cols= img.shape

red= np.zeros((img.shape[0],img.shape[1],1),np.uint8)

   
b,g,r = cv2.split(img2)
 
#cv2.imshow("Blue",b)
#cv2.imshow("Green",g)
#cv2.imshow("Red",r)
cv2.imshow('img2',img2)

# Transformacion Euclideana

print("\nIngrese los parametros:\n")

angle=float(sys.argv[2])
a=math.radians(angle)

tx=float(sys.argv[3])
x=tx

ty=float(sys.argv[4])
y=ty

#La Transformacion euclidea
# se reliza en 2 parte separadas, 
# cada una representando una
#parte de la transformacion:
# rotacion y traslacion

#ROTACION
M_1 = cv2.getRotationMatrix2D((cols/2,rows/2),angle,1)      #Le paso el punto central y el angulo 

# la funcion cv2.getRotationMatrix2D crea la matriz
# M_1  que corresponde a la rotacion

#TRASLACION
M_2 = np.float32([[1,0,x],[0,1,y]])

print(M_2)

# la funcion np.float32 crea la matriz
# M_2  que corresponde a la traslacion


dst_b = cv2.warpAffine(b,M_1,(cols,rows)) 
dst_g = cv2.warpAffine(g,M_1,(cols,rows)) 
dst_r = cv2.warpAffine(r,M_1,(cols,rows)) 

dst_2b= cv2.warpAffine(dst_b,M_2,(cols,rows)) 
dst_2g= cv2.warpAffine(dst_g,M_2,(cols,rows)) 
dst_2r= cv2.warpAffine(dst_r,M_2,(cols,rows)) 

#cv2.warpAffine realiza la transformacion
# el primer elemento es el objetivo de la transofrmacion

# el segundo es la matriz, en este caso se suman las dos
# matrices para realizar tanto la rotacion 
# como la traslacion

# el tercer argumento dela funcion cv2.warpAffine
# define tamano de imagen de salida

img = cv2.merge((dst_2b,dst_2g,dst_2r))


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()