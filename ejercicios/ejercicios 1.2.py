frase = input("decime una frase y te calculo cuanto tardarias en decirla: ")

palabras_separadas = frase.split(" ")
cantidad_De_palabras= len(palabras_separadas)

if cantidad_De_palabras >120:
    print("para flaco no te pido un testamento")

print(f'digiste {cantidad_De_palabras} palabras y tardaste {cantidad_De_palabras/2} segundos en decirlo' )

print(f"dalto lo diria en {cantidad_De_palabras*100 //(2*1.3)//100} segundo en decirlo")


