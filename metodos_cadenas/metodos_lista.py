#creando una lista con list
lista = list([34,45,77])

#devuelve la cantidad de elementos de la list
cantidad_de_elementos = len(lista)

#agregando elementos con append 
lista.append("Gotham")
lista.append(56)

#agregando un indice a la lista en un orden especifico
lista.insert(1,1)

#agrega varios elementos a la lista
lista.extend([66,2023])

#elimina un elemento de la lista por su indice
lista.pop(3) #-1 para eliminar el ultimo de la lista -2 para eliminar el ante ultimo de la lista

#remuve un elemento de la lista por su valor
lista.remove("Gotham")

#ordena la lista de forma acendente(si usamos el parametro reverse=True lo ordena en reves)
lista.sort()

#invierte los elementos de la lista
#lista.reverse()

#verifica si el elmento se encuentra en la lista 
se_encuentra_en =lista.index(56)

#elimina todos los elementos de la lista 
#lista.clear()
print("""esta es mi lista:
      """)
print(lista)
print("""
      ¿en -que orden esta el  56 en esta lista?:
      """)
print(se_encuentra_en)

