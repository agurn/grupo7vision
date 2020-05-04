import numpy as np #
import cv2
import sys
import math

drawing =False
mode = True      # HARDCODED, DIBUJO

ix,iy =-1,-1     #Posicion no valida. #Variable global
tamaño_rect=1
ancho=0
alto=0
vari=0

def draw(event,x,y,flags,param):
    global backup
    global img
    global ix,iy,drawing,mode
    global vari
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True                 #Si hago click , actualiza la posicion y estoy listo para dibujar     
        ix,iy = x,y
        print("sigue")
    elif event == cv2.EVENT_MOUSEMOVE:
        print(x,y)
        if drawing is True:             #Si drawing=1, significa que hice click y estoy moviendo el mouse
            
                copy = img.copy()
                cv2.rectangle(copy,(ix,iy),(x,y),(0,255,0),2)      #Para evitar efecto.
                cv2.imshow("image", copy)
                vari=1
                
            
    elif event == cv2.EVENT_LBUTTONUP:                            
        drawing=False
        vari=0
        if mode is True:
            
         cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        ancho=abs(ix-x)
        alto=abs(iy-y)
        print(str(ancho)+"x"+str(alto)) 
            
        img=np.zeros((alto,ancho,3),np.uint8)

        fila_aux=0
        columna_aux=0

        for fila in range ((iy, y )[y<iy],(iy, y )[y<iy]+alto-1):
            columna_aux=0
            for columna in range ((ix, x )[x<ix],ancho+(ix, x )[x<ix]):
                    
                img[fila_aux][columna_aux]=backup[fila][columna]   
                columna_aux=columna_aux+1 
            fila_aux=fila_aux+1

def transformacion(rows,cols,angle,x,y):
    # Transformacion Euclideana
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

print("\nIngrese los parametros:\n")

angle=float(input("\nÁngulo:\t"))
tx=float(input("Traslacción en X:\t"))
ty=float(input("Traslacción en Y:\t"))

img = cv2.imread(filename)

backup = img.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)  #llama a la funcion


while(1):
    if vari==0:
        cv2.imshow('image',img)

    k=cv2.waitKey(1) & 0xFF
    if k == ord('m'):           #Cambio el modo. 
        mode = not mode
        res = np.zeros((512,512,3),np.uint8)
    elif k == 101:           #Cambio el modo. 
        rows,cols= img.shape[0:2]
        res=transformacion(rows,cols,angle,tx,ty)
        cv2.imwrite("Resultado.png",res)
        break

cv2.destroyAllWindows()