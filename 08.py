#8.	Desarrolle el programa que determine de un cilindro el área base 
import math
r= int( input( "ingrese el radio(r): " ))
h= int( input( "ingrese la altura(h): " ))
a= math.pi* r ** 2
al= 2 * math.pi * r * h
at= 2 * a * al
print( f"El area es de la base es de:{a:.2f},\nEl area lateral es:{al:.2f},\nEl area total es:{at:.2f}" )
