#contadores
vainilla = 0 
chocolate = 0 
fresa = 0

for i in range (0,5,1):
   eleccion = input("elige un sabor: ")
   
   if (eleccion == "vainilla"):
      vainilla +=1
    
   elif (eleccion == "chocolate"):
      chocolate +=1

   elif (eleccion == "fresa"):
       fresa +=1

print("cantidad de vainilla: ",vainilla)
print("cantidad de chocolate: ",chocolate)
print("cantidad de fresa: ",fresa)
