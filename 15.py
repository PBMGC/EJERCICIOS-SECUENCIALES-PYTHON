#Desarrolle el programa que determine el capital total en dólares y que porcentaje de dicho capital aporta cada uno
j=int ( input("cuanto aporto Juan: " ) )
r=int ( input("cuanto aporto Rosa: " ) )
d=int ( input("cuanto aporto Daniel: " ) )

dol= d/3
t= dol+j+r

porc1= ( j*100/t ) 
porc2= ( r*100/t ) 
porc3= ( dol*100/t )

print( f"el capital total es de: {t:.2f}" )
print( f"la inversion de Juan:{porc1:.2f} %" ) 
print( f"la inversion de Rosa: {porc2:.2f}%" )
print( f"la inversion de Daniel:{porc3:.2f}%" ) 