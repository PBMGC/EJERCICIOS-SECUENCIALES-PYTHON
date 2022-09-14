#7.	Desarrolle el programa que determine el área y el perímetro de un rectángulo
b= int( input( "ingrese la base:" ))
h= int( input( "ingrese la altura:" ))

area= b * h
perimetro= 2 * ( b+h )

print( f"El area es:{area:.2f}\nEl perimetro es de:{perimetro:.2f}" )
