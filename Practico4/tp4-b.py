import cv2
import numpy as np
import sys
import subprocess      #Para enviar notificaciones en ubuntu



def sendmessage(message):
    if(sys.platform=="linux"):             #Solo si es linux lo envia
        subprocess.Popen(['notify-send', message])
    return







drawing =False
mode = True      # HARDCODED, DIBUJO

ix,iy =-1,-1                                  #Posicion no valida. #Variable global
tamano_rect=1
ancho=0
alto=0

vari=0      # Para mantener el rectangulo

def draw_circle(event,x,y,flags,param):
    global backup
    global img
    global ix,iy,drawing,mode
    global vari
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True                                      #Si hago click , actualiza la posicion y estoy listo para dibujar     
        ix,iy = x,y
        print("sigue")
    elif event == cv2.EVENT_MOUSEMOVE:
        print(x,y)
        if drawing is True:                                                 #Si drawing=1, significa que hice click y estoy moviendo el mouse
            
                #cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),1)            #Dibuja rectangulo toma las posicion donde hice click, hasta donde muevo
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

            print("El valor de ix",ix)
            print("El valor de iy",iy)


            print("El valor de x",x)
            print("El valor de y",y)
            print("ancho",ancho)
            print("alto",alto)
           
            print( (ix, x )[x<ix] , "hasta", ancho+(ix, x )[x<ix] )
            print( (iy, y )[y<iy] , "hasta",alto+(iy, y )[y<iy] )

            fila_aux=0
            columna_aux=0

            print(img.shape[0],"x",img.shape[1])
            print(backup.shape[0],"x",backup.shape[1])


            for fila in range ((iy, y )[y<iy],(iy, y )[y<iy]+alto-1):
                columna_aux=0
                for columna in range ((ix, x )[x<ix],ancho+(ix, x )[x<ix]):
                    
                    img[fila_aux][columna_aux]=backup[fila][columna]   
                    
                    print("fila col",fila,",",columna),
                    print("aux",fila_aux,",",columna_aux),

                    columna_aux=columna_aux+1
                
                fila_aux=fila_aux+1
            
    

img= cv2.imread("test.jpg")
#backup=cv2.imread("test.jpg")

backup = img.copy()
#print(img)


#img= np.zeros((512,512,3),np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)  #llama a la funcion

while(1):
    if vari==0:
        cv2.imshow('image',img)

    k=cv2.waitKey(1) & 0xFF
    if k == ord('m'):           #Cambio el modo. 
        mode = not mode
        img = np.zeros((512,512,3),np.uint8)

    elif k == 103:           #Cambio el modo. 
        cv2.imwrite("Resultado.png",img)
        sendmessage("Imagen Guardada")

    elif k == 114:           #Cambio el modo. 
        img=backup.copy()                                   #TENER CUIDADO CON ESTO PORQUE SI SIMPLEMENTE IGUALO HACE CUALQUIER COSA.
        sendmessage("Imagen Restaurada")

    elif (k==27 or k==113):
        sendmessage("Hasta pronto")
        break


   # print ("iniciales"+str(ix)+","+str(iy))
   # print ("finales"+str(x)+","+str(y))
    


cv2.destroyAllWindows()
