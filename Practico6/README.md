# Práctico 6 - Transformación de Similaridad

A. Agregar al método anterior un parámetro para permitir también el escalado de la imagen.

Parámetros:

* Angle: Ángulo
* tx: traslación en x
* ty: traslación en y
* s: escala

Recordar que la transformación de similaridad tiene la siguiente forma:

s.cos(angle)  s.sin(angle) tx
-s.sin(angle) s.cos(angle) ty

B. Usando como base el programa anterior, escriba un programa que permita seleccionar
un rectángulo de una imagen y

* con la letra “s” aplique una transformación de similaridad
a la imagen dentro del rectángulo y la guarde en el disco.