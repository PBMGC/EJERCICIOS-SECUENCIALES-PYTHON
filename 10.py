#10.	Dado un número natural de cuatro cifras, desarrolle el programa que permite obtener el número al revés.
n= int( input ("ingrese el numero: " ) )

c1= n // 1000
c2=( n % 1000 ) //100
c3= ( ( n%1000 ) %100 ) //10
c4= n % 10

print( "revez:",str(c4)+str(c3)+str(c2)+str(c1) )
