#crando una funcion 3 parametros
#def frase(nombre,apellido,adjetuvo)
#    return f"hola {nombre} {apellido} son un {adjetivo}"

#utilizando keybord arguments
#frase_resultante = frase(adjetivo ="lucas ","apellido",="dalto")
      
#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo ="tonto"):
    return f'hola{nombre},{apellido},sos muy {adjetivo}'

frase_resultante = frase("nombre","dalto","inteligente")
print(frase_resultante)



