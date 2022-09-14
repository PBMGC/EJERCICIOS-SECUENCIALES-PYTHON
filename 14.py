n1= int ( input ("Numero 1: " ) )
n2= int ( input ("Numero 2: " ) )
n3= int ( input ("Numero 3: " ) )
n4= int ( input ("Numero 4: " ) )
n5= int ( input ("Numero 5: " ) )

lista= list((n1,n2,n3,n4,n5))
lista.sort()
promedio = (n1 + n2 + n3 + n4 +n5 - lista[0] - lista[1]) / 3

print( f"Promedio : {promedio:.2f}" )
print( f"Numero Maximo : {lista[4]}" )
print( f"Numero Minimo : {lista[0]}" )