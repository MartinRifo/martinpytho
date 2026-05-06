#explicacion y uso de for:

# for i in range/¡(6)
# print ("hola")

# num=int(input("ingrese un numero: "))

# for i in range(num):
#    print(i+1,"repeticion")





   #pedir un numero al usuario y mostrar su tabla de multiplicar

# num=int(input("ingrese un numero"))

# for i in range(12):
#     print(num, "x" , i+1, "=", num*(i+1))
    

# titulo= "clima de hoy"
# diadelmes=17
# mes=4
# tem=25.7
# llueve=True

#     print(titulo, "temperatura", tem,diadelmes,"7",mes)

# if llueve==True

# else ("no sacar paraguas")

# preguntar cuantas notas son y sacar el promedio
# num=int(input("ingrese un numero: "))  
# suma=0
# for i in range (num):
#     nota=float(input("ingrese la nota: "))
#     suma=suma+nota
#     prom= suma/num
#     print("el promedio es: ", prom)

#     if prom>=4:
#         print("aprobado")
#     else:
#         print("reprobado")

#sumatoria
# num=int(input("ingrese un numero")
#         total=0
#         for i in range(num):
#             total=total*i+1
#             print("la sumatoria es: ",total)
# contador de vocales y consonantes
# vocales=0
# conso=o
# print("ingrese su nombre: ")
# nombre=input()
# if i== "a" or i== "e" or i== "i" or i== "o" or i== "u":
#         print("es una vocal")

# for i in  (nombre):
#     print(i)
#     vocales=vocales+1
# elif i == "":
# else:
#     conso=conso+1
    

# print("la cantidad de vocales es: ",vocales)
# print("la cantidad de consonantes es: ",conso)

# n= "carolina"
# name="alonso robles"
# print(name[0])
# print(len(name))
# print(n.strip())
# print(name.upper())
# print(name.lower())
# print(name.replace("Robles , parra"))
# print (name.split())

# ejercicios
#pedir a la clave al usuario y verificar que sea shazam independiente de su case

# clave=input("ingrese su clave")
# if clave.() == "SHAZAM":
#    print("clave correcta")
# else: 
#    print("clave incorrecta")

# code="shazam"

# code=inout("ingrese su clave")
# if clave==code.upper ():
#    print("clave correcta")
# else 
#    print ("clave incorrecta")


# pin=int (input("ingrese su pin"))
# if len (str(pin))==4:
#    print("pin creado")
# else:
#    print ("pin erroneo")



# definir 2 candidatos. Preguntar la cantidad de votantes
# pregunar a cada votante por quien votara mostrando las alternativas. Contar los votos y mostrar resultados.
#Definir el ganador y considerar un empate

# print("ingrese el nombre del candidato 1: ")
# candidato1=input()
# print("ingrese el nombre del candidato 2")
# candidato2=input()
# print("ingrese la cantidad de votantes: ")
# votantes=int(input())
# votos_candidato1=0
# votos_candidato2=0
# for i in range(votantes):
#     print("votante", i+1, "por quien votara? (1 para", candidato1, "2 para", candidato2, ")")
#     voto=int(input())
#     if voto==1:
#         votos_candidato1=votos_candidato1+1
#     elif voto==2:
#         votos_candidato2=votos_candidato2+1
#     else:
#         print("voto invalido")

# if votos_candidato1>votos_candidato2:
#     print("el ganador es", candidato1)
# elif votos_candidato2>votos_candidato1:
#     print("el ganador es", candidato2)
# else:
#     print("es un empate")




# num=int (input("ingrese un numero"))
# for i in range(num):
#     print ("repeticion", i +1)

#definir 2 candidatos, preguntar la cantidad de votantes
#preguntar a cada votante por quien votara
# # mostrando las alaternativas.Contar los votos y mostrar resultados
#definir el ganador y considerar un empate

# c1= "candidato1"
# c2= "candidato2"
# c1=0
# c2=0
# cantv=int(input("ingrese la cantidad de votantes: "))
# for i in range (cantv):
#     print("votante", i+1, "por quien votara? (1 para", c1, "2 para", c2, ")")
#     voto=int(input())
#     if voto==1:
#         c1=c1+1
#     elif voto==2:
#         c2=c2+1
#     else:
#         print("voto invalido")
# if c1>c2:
#     print("el ganador es", c1)
# elif c2>c1:
#     print("el ganador es", c2)
# else:
#     print("es un empate")
