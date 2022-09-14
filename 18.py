ar=int( input ("cuantos productos esta llevando: ") )
pr=float( input ( "precio del producto: " ) )

can= pr * ar
d1= can- (can * 0.15)
d2= d1- (d1 * 0.15)
td= (can * 0.15) + (d1*0.15)

print()
print( f"Importe sin descuento:{can:.1f}\nDescuento S/:{td:.1f}\nImporte total:{d2:.1f}" )