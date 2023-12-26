#crenado funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #intercanbiando a enteris y sumarlos
        try:
            resultado = int(a) + int(b)
            #si lanzo una excepcion pedirle que reingrese los datos 
        except ValueError as e:
            print("ingresa un numero")
            print(f"error: {e}")
            #si todo salio bien terminamos el bucle
        else:
            break
        #finally se ejecuta siempre
        finally:
            print("manejo de excepciones finalizadas")
            
    #mostrabdi ek resultadi
    return resultado
        
print(sumar_dos())