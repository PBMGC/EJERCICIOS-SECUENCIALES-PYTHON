#9.	Desarrolle el programa que lea un número entero y determine la suma de sus cifras.
n= int ( input ( "Numero: " ))

c1= n // 1000
c2=( n % 1000 ) //100
c3= ( ( n%1000 ) %100 ) //10
c4= n % 10

print()
print(f" suma: {c1+c2+c3+c4} " )
