#
#numeros = [3,3]
#def pepe():
 #   print("hola mundo")
  #  suma=sum(numeros)
   # print(suma)
    
#pepe()
#print("hola mundo")
#pepe()

#creeando una funcion que tenga parametros 

def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
         adjetivo ="titan"
    else:
         adjetivo ="amor"
    
    
    
    print(f"hola {nombre}, mi {adjetivo} ¿como andas")
saludar("camila","mujer")
saludar("dalto","hombre")

#creando funciones que nos retornen valores

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_enteros =str(num)
    num = int(num_enteros[0])
    c1 = num -2
    c2 = num 
    c3 = num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña    
    
password = crear_contraseña_random(5) 
frase = f"tu contraseña Nueva es:{password}"
print(frase)  
