#creando una funcion que nos devuelva los numeros primos
#entre 0 y el argumento que pasamos

#creamos una funcion que verifique si un numero es primo
def es_primo(num):
    #verificamos que el numero pasado no pueda dividirse
    #por nungun numero entre 2 y ese sismo numero -1
    for i in range(2,num-1):
        #si es divisible por alguno retornamos false y termina el bucle
        if num%i==0: return False
   #si termina el bucle significa que no fue divisible entonces es primo
    return True

def primos_hasta(num):
    primos = []
    for i in range(3,num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos 
resultado = primos_hasta(98)
print(resultado)


