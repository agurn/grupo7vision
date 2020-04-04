#PRACTICO 1

#Crear una función adivinar que permita adivinar un número generado en forma aleatoria
# El número debe estar entre 0 y 100
# Este número se genera adentro de la función
# Además debe recibir un parámetro que sea la cantidad de intentos y en caso de que esta cantidad de intentos sea superada el programa
#debe terminar con un mensaje

#Si el usuario adivina antes de superar el número de intentos máximo, se debe imprimir un mensaje con el número de intentos en los que adivinó
# Después de crear la función, llamarla en el mismo archivo

# Ejecutar el script desde la consola  python nombre_programa.py

def aleatorio():
    
    import random
    random = random.randint(0, 100)
    print(str(random))
    cont = 1
    intentos =int(input('Ingrese cantidad de intentos\n'))


    while True:
        numero_elegido=int( input("¿Cual cree que es el numero? Intento N° "+str(cont)+"\n"))
        
        
        if (cont == intentos):
            print ("Se te acabaron los intentos, el numero era:"+random)
            return 0
        else:
            cont=cont + 1
            if (numero_elegido == random):
                print("Adivino el numero\n")
                return 0
            elif (numero_elegido<random):
                print("Más arriba")
            else:
                print("Más abajo")
        



aleatorio()