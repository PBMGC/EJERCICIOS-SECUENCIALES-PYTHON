#5.	Desarrolle el programa que, dada la capacidad de un disco duro en gigabytes, lo convierta a megabytes, kilobytes y bytes
print( "**"*5+"ingrese la capacidad del disco duro"+"**"*5 )
x= int( input ("                         ") )
print()

mb= x*1024
kb= mb*1024
b= kb*1024

print( "la capacidad en megabytes son:",mb,"\nla capacidad en kylobites son:",kb,"\nla capacidad en bytes son:",b )
print()
