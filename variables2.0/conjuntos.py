#creando conjuntos con set()
conjunto = set(["dato1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 ={conjunto1, "dato1"}

#print(conjunto2)

#teoria de conjunto
conjun1 = {1,3,5,7}
conjun2 = {1,5,7}

#verificando si es un subconjunto
#resultado = conjunto2.issubset(conjunto1)
#resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
#resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1

#verifica si hay un numeri en comun
resultado = conjunto2.isdisjoint(conjunto)


print(resultado)



