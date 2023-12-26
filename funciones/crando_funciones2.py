#creando funciones que nos retornen multiples valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_enteros =str(num)
    num = int(num_enteros[0])
    c1 = num -2
    c2 = num 
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña    

#desenpaquetando la  funcion
password,primer_numero = crear_contraseña_random(289)

#mostrando los resultados obtenidos y 
print(f"tu contraseña nueva es:{password}")
print(f"el numero utilizado para crar tu contraseña fue:{primer_numero}")


