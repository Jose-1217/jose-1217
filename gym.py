# acceso al gym

edad = int(input("ingresa tu edad: "))
    
if edad < 13: 
   print("no puede entrar ")
       
elif edad > 13 and edad <17:
    print("clase juvenil: si puede entar ")

elif edad > 18 and edad <59: 
    print("clase general: si puede entar ")

elif edad > 60: 
    print("clase senior: si puede entar ")

else:
    print("edad no valida ")
    
 
