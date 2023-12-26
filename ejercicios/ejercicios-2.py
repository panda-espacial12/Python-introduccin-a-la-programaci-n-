#funcion para obtener al asistente y al profesor segun la edad
def obtener_compañero(cantidad_de_compañeros):
    #creando la lista con los compañero
    compañeros = []
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre= input("igresa el nombre del compañero: ")
        edad = int(input("igresa la edad del conpañero: "))
        compañero = (nombre,edad)
        #agregando la informacion a la lista
        compañeros.append(compañero)
        #ordenando de menor a mayor segun la edad
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    return asistente,profesor      
 #compañero [x] devulve una tupla con (nombre,edad)y despues acedemos al nombre
 #para definir al asistente yal profesor
asistente,profesor = obtener_compañero(4)

print(f"el profesor es: {profesor} y su asistente es {asistente}")