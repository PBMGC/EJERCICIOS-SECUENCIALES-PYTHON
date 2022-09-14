import math

a=int( input ("ingrese el primer valor:" ) )
b=int( input ("ingrese el segundo valor: ") )
c=int( input ("ingrese el tercer valor: ") )

formula= ( (math.pow(b,2)) + (-1*4*a*c) )**1/2
p1=(( -1*b ) + formula )/2*a
p2=( ( -1*b ) - formula )/2*a

print(f"Las claves son:{p1:.2f} y {p2:.2f}")