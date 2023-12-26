#creando una funcion de muestra la serie de fibonaci 

def fibonaci(num):
    a,b = 0,1
    fibonaci_lista = [0]
    for i in range(num):
        if b > num: return fibonaci_lista
        else:
            fibonaci_lista.append(b)
            a,b = b,a+b
            
resultado = fibonaci(33)
print(resultado)
    





