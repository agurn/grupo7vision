import numpy as np
import cv2
import sys




if(len(sys.argv)> 1):
    filename = sys.argv[1]                          #Toma como argumento aquel acompañado en el comando
else :
    print('No pasó el nombre del video ej python guarda.py video.mp4')      #Sino tengo argumento lo cierra
    sys.exit(0)

cap = cv2.VideoCapture(filename)



codec = cv2.VideoWriter_fourcc(*'DIVX')  #Elijo para que la salida sea AVI , codec elijo.

print("La resolucion del video es:"+str(int(cap.get(3)))+"x"+str(int(cap.get(4))))
print("Los fps del video son:" +str(cap.get(cv2.CAP_PROP_FPS)))


#out = cv2.VideoWriter('Salida.avi',codec, 30, (int(cap.get(3)),int(cap.get(4))),False)

out = cv2.VideoWriter('Salida.avi',codec, cap.get(cv2.CAP_PROP_FPS) , (int(cap.get(3)),int(cap.get(4))),False) 

#


#Basicamente le digo que utilice el Formato AVI, y toma las dimensiones del video, es decir que no esta hardcodeado.
#Que seria una mala practica de programacion ya que el usuario no puede modificar el codigo. Tendria que  estar
# modificando cada 2x3 el codigo . En cambio aca reconoce las dimensiones del video.    

while(cap.isOpened()): # si puedo leer
    ret, frame = cap.read()       #devuelve 1 si puede leer el fotograma
    if ret == True: 
        
        #Convierte el frame original a escala de gris
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Escribe el frame en el video.avi
        out.write(output)
        
        # muestra el original
       # cv2.imshow('frame',frame)
        
        cv2.imshow('frame',output)   #muestra la salida en gris

        # Press Esc on keyboard to stop recording
        if cv2.waitKey(1) == 27:
            break
    
    # Break the loop
    else:
        break

# When everything is done, release the video capture and video write objects
cap.release()
out.release()
 
# Closes all the frames
cv2.destroyAllWindows()