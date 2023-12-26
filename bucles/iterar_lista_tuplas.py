animales = ["gato","perro","loro","cocodrilo"]
numeros =[52,16,14,72]

#recoriendo la lista
for animal in animales:
    print(f'ahora las variables son igual a {animales}')

#recoriendo la lista y multiplicando el valor por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)
    
for numero,animal in zip(numeros,animales):
    print(f"recoriendo la lista 1: {animal}")
    print(f"recoriendo la lista 2: {numero}")
   
   #forma no optima de recorer una lista con su indice
for num in range(len(numeros)):
   print(numeros[num])
   
   #forma correcta de recorer una lista
   for num in enumerate(numeros):
       indice = num[0]
       valor = num[1]
       print(f'el indice es:  {indice} y el valor es {valor}')
   
   #usando el else
   for numero in numeros:
       print(f"ejecutando el ultimo bucle, valor actual {numeros}")
else:
      print("el bucle termino")   
      
#todo lo anterior funciona exactamente igual para tuplas
   
   
   