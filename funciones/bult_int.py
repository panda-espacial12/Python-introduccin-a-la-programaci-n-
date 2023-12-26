numeros = [4,7,1,42,15]

#encontrando el numero mayor
mayor = max(numeros)
print(mayor)

#encontrando el numero menor
menor = min(numeros)
print(menor)

#redondeando a 6 decimales
numero = round(12.345678,3)

print(numero)

#retorna false -> 0, vacio, false, none / true -> dustinto a 0, cadena, datos no vacios
resultado_bool =bool([13,123])

print(resultado_bool)

#retorna true si todos los valores son verdaderos
resultado_all = all([0,"true",[344,23]])
print(resultado_all)

#suma todos los valores de un iterable
suma = sum(numeros)
print(suma)
