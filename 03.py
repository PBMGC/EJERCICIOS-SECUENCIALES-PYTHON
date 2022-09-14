#Desarrolle el programa que determine la longitud total recorrida en metros y en yardas
k= int ( input (" kilometros : "))
p= int ( input (" pies :"))
m= int ( input (" millas :"))

me= k * 1000 + (p * 12 *2.54)/100 + m
y= m /1.09361
print()
print( f"Metros recorridos: {me:.2f} \nYardas recorridas: {y:.2f} ")
