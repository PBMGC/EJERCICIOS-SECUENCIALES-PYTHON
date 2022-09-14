h=int( input ( "horas trabajadas:" ) )
t=float( input ( "tarifa basica:" ) )
sb=h*t
b=sb*0.20
sbr=b+sb
d=sbr*0.10
sn=sbr - d
print(f"Sueldo Base S/:{sb:.1f}\nSueldo Bruto S/:{sbr:.1f}\nDescuento S/:{d:.1f}\nSueldo neto es S/:{sn:.1f}")