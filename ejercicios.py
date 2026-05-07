# Calcular el araccel a pagar segun grupo familiar y comuna en la que reside
# A continuacion , los descuentos por cumuna:
# La Florida 20%, La pintana 30%, Puente Alto 25%, San Joaquin 15%
# Grupo familiar: 1=>2%, 2 a 4=>3%, 5 o mas=>4%
# Preguntar al usuario en que comuna vive
# Preguntar al usuario con cuantas personas vive
# El arancel actual es de 200.000 por semestre
# Basados en las respuestas del usuario  y en 
# la informacion dada, calcular su descuento

# arancel=200000
# descuento=0
# print("ingrese su comuna: ")
# comuna=input()
# print ("ingrese la cantidad de personas con las que vive: ")
# personas=int(input()) 
# match comuna:
#     case "La Florida":
#         descuento+=0.20
#     case "La pintana":
#         descuento+=0.30
#     case "Puente Alto":
#         descuento+=0.25
#     case "San Joaquin":
#         descuento+=0.15
#     case _:
#         print("comuna no valida")
# if personas==1:
#     descuento+=0.02
# elif personas>=2 and personas<=4:
#     descuento+=0.03
# elif personas>=5:
#     descuento+=0.04
# else:
#     print("cantidad de personas no valida")
# total=arancel-(arancel*descuento)
# print("el total a pagar es: ", total)


