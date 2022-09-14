#Desarrolle el programa que calcule el área total y el volumen de un cilindro
import math
r=int( input( "ingrese el radio(r): " ))
h=int( input( "ingrese la altura(h): " ))

ar= 2 * math.pi * r *(r+h)
vol= math.pi * r**2 *h

print()
print( f"la area es:{ar:.2f}\nel volumen es:{vol:.2f}" )
