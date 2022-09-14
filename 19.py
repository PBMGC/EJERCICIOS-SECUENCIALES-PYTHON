ven=int( input ( "ingrese el total vendido:" ) )

co= ven * 0.09
sb= co + 500
desc=sb*0.11
sn=sb-desc

print(f"Comision:{co:.1f}\nSueldo Bruto:{sb:.1f}\nDescuento:{desc:.1f}\nSueldo Neto:{sn:.1f}")