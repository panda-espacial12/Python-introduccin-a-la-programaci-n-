numeros = [1,2,3,4,5,6,7,87,9,0,10]

#creando una funcion llamada lambda para multiplicar por dos
multiplicar_por_dos = lambda x : x*2

#crando funcion que diga su es par o no 
def es_par(num):
    if(num%2==1):
        return True

#usando filter con una funcion comun 
numeros_pares = filter(es_par,numeros)

#creando lo mismo pero con lambda
numeros_pares =filter(lambda numero:numero%2 == 0,numeros)
print(list(numeros_pares))
