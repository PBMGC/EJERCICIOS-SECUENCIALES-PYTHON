#2.	Desarrolle el programa que permite convertir una cantidad dada en metros a su equivalente en centímetros, pulgadas, pies y yardas.
m= int( input (" ingrese los metros a convertir: " ) )
cm= m*100
p= cm/2.54
pi= p/12
y= pi/3
print()
print( f"los centimetros son:{cm:.2f}\nlas pulgadas son:{p:.2f}\nlos pies son:{pi:.2f}\nlas yardas son:{y:.2f}" )
