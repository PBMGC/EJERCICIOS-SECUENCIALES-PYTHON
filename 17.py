d= int ( input ( "donacion:" ) )
cs= (d*0.25)
ci= (d*0.35)
ei= (d*0.25)
anc= d-(cs+ci+ei)
print(f"Centro de Salud S/:{cs:.1f}\nComedor Infantil S/:{ci:.1f}\nEscuela Infantil S/:{ei:.1f}\nAsilo de Ancianos S/:{anc:.1f}")
