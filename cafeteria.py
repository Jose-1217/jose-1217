# compra
cafe = 4000
te = 3500
jugo = 5000

elige = input("que bedida quieres: ")
cantidad = int(input("cuanas quieres: "))

if (elige == "cafe" ):
  total = cafe * cantidad

elif (elige == "te" ):
   total = te * cantidad

elif (elige == "jugo" ):
  total = jugo * cantidad

else :
   print("no hay esa bebida ") 

print("debes pagar:", total)
