#1.	Desarrolle el programa que determine el porcentaje de varones y de mujeres que hay en un salón de clases
import os 
os.system("cls")

v= int (input (" varones: "))
m= int (input (" mujeres: "))

total= v + m
pv= v*100/total
pm= m*100/total

print( f"varones:{pv:.2f}%" )
print( f"mujeres:{pm:.2f}%" )




