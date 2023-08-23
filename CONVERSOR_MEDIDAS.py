#Declarar variales
conversion = float()
metro = 0.01
yarda = 0.0109361
vara = 0.0083333
pulgada = 0.393701
pie = 0.0328084

#Solicita al usuario ingresar la longitud en centimetros
print("Ingrese longitud en centimetros:  ")
cms = float(input())
#Solicita al usuario ingresas la unidad de medida a convertir
print("Ingrese la unidad de medida, que desee convertir, 1. Metro, 2. Yarda, 3. Vara, 4. Pulgada, 5. Pie:    ")
medida = input()

#Este procedimiento realiza la conversión, con operador lógico IF.
if medida == "1":
    conversion = cms * metro
    print("La longitud en metros es:  ",conversion)
elif medida == "2":
   conversion = cms * yarda
   print("La longitud en yardas es:  ",conversion)
elif medida == "3":
   conversion = cms * vara
   print("La longitud en Varas es:  ",conversion)
elif medida == "4":
   conversion = cms * pulgada
   print("La longitud en Pulgadas es:  ",conversion)
elif medida == "5":
   conversion = cms * pie
   print("La longitud en Pies es:  ",conversion)
else:
   print("La unidad de medida no existe. Elija una opcion de la 1 a la 5")

input("Presione Enter para salir...")
