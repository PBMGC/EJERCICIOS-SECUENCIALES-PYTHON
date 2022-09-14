#11.-Dado dos números enteros de 3 cifras, desarrolle el programa que muestre la cifra primera y tercera cifras intercambiadas entre ambos números
n= int( input ("ingrese el primer numero: " ) )
n2= int( input("ingrese el segundo numero: ") )

c1= n // 100
c2= ( n % 100 ) //10
c3= n % 10
s1= n2 // 100
s2= ( n2 % 100 ) //10
s3= n2 % 10

print( "Primer numero:", str(s3)+str(c2)+str(s1) )
print( "Segundo numero:",str(c3)+str(s2)+str(c1) )