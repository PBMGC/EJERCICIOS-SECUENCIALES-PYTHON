c=int(input("cantidad a convertir:"))
conver_200=c//200
conver_100=c//100
converespe_100=(c%200)//100
conver_50=c//50
converesp_50=(c%100)//50
conver_20=c//20
converesp_20=(c%50)//20
conver_10=c//10
converesp_10=(c%20)//10
conver_5=c//5
converesp_5=(c%10)//5
conver_2=c//2
converesp_2=(c%5)//2
conver_1=c//1
converesp_1=round(c%2)//1
print( "billetes de 200:", conver_200 , "billetes de 100: ", conver_100 , " billetes de 50: " , conver_50 ,"billetes de 20: ", conver_20 ," billetes de 10: ", conver_10 , " monedas de 5: " , conver_5 , "monedas de 2: ", conver_2 , "monedas de 1: " ,conver_1,sep="    " )
print()
print( "billetes de 200: ", conver_200 , "billetes de 100: ", converespe_100 , " billetes de 50: ", converesp_50 ,"billetes de 20: ", converesp_20 , " billetes de 10: ", converesp_10 ," monedas de 5: ", converesp_5 , "monedas de 2: ", converesp_2 , "monedas de 1: " , converesp_1,sep="    ")