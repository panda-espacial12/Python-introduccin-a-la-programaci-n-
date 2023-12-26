frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "dalto"
numeros = [12,8,10]
#evitando que se coma una manzana con la sentencia for in
for fruta in frutas:
    if fruta == "granada":
      continue
    print(f"me voy a comer una {fruta}")

#evitar que el bucle no se ejecute tampoco(el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta == "pera":
       break
else:
    print("bulce terminado") 
        
#recorer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)




