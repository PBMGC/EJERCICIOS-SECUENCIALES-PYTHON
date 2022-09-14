#13.Desarrolle el programa que permita calcular la hipotenusa de un triángulo
import math

c1= int( input( "cateto opuesto:" ) )
c2= int( input( "cateto abyacente: ") )
hipo=( math.hypot(c1,c2) )

print()
print( f"Hipotenusa:{hipo:.2f}")
