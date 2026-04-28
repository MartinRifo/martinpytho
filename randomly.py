# uso y explicacion de random
# import random
# num=random.randint(1,10)
# print(num)

# for i in range (num):
#     print("hola vicente")

#     for i in range (10)
#     print(f"(num)x(i)=(num*1)")

# 3 personas juegan golf
# cada persona tiene la posibilidad de golpear 
# y la distancia varia entre 60 y 190 metros
# mostrar al final, el golpe mas fuerte

# import random
# personas=["persona1","persona2","persona3"]
# golpes={}

# for persona in personas:
#     golpe=random.randint(60,190)
#     golpes[persona]=golpe

# golpe_mas_fuerte=max(golpes.values())
# persona_golpe_mas_fuerte=[persona for persona, distancia in golpes.items() if distancia==golpe_mas_fuerte][0]

# print(f"El golpe más fuerte fue de {golpe_mas_fuerte} metros y lo logró {persona_golpe_mas_fuerte}")


# import random


# dad0=random.randint(1,6)
# dad1=random.randint(1,6)


# #si los dados dan el mismo numero, el jugador
# # se va a la carcel
# if dad0==dad1:
#     print("Vas a la carcel")


#Ludo
#1 jugador juega y lanza dos dados
#por cada unidad en el dado avanza una posicion en el tablero
# cuando llegue a 50, gana
# mostrar cuantos turnos le toma
#llegar a la meta
# import random
# posicion=0
# turnos=0
# while posicion<50:
#     dado1=random.randint(1,6)
#     dado2=random.randint(1,6)
#     posicion+=dado1+dado2
#     turnos+=1

# print(f"El jugador necesitó {turnos} turnos para llegar a la meta.")



#crea un numero random del 1 al 100
#pide al usuario que adivine el numero
#si el usuario pone un numero mayor al generado
# debe decir "la pasaste" en caso contrario
# " el numero a adivinar es mayor"
# solo hay 5 posibilidades de adivinar.
# import random
# numero_aleatorio=random.randint(1,100)
# intentos=5
# print("Adivina el número entre 1 y 100. Tienes 5 intentos.")
# for intento in range(intentos):
#     adivinanza=int(input(f"Intento {intento+1}: "))
#     if adivinanza>numero_aleatorio:
#         print("La pasaste")
#     elif adivinanza<numero_aleatorio:
#         print("El número a adivinar es mayor")
#     else:
#         print("¡Felicidades! Has adivinado el número.")
#         break









