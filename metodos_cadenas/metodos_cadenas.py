cadena1 ="hola,que,tal"
cadena2 ="Bienvenido"
cadena3 ="1234567890"


resultado1 = cadena1.lower()#lo pone en minuscula
resultado2 = cadena1.upper()#lo póne en mayuscula
resultado3 = cadena1.capitalize()#pone la primer letra en mayuscula

#busca una cadena en otra cadena si no existe devuelve -1 
busqueda_find =cadena1.find("e")

#busca una cadena en otra cadena si no existe devuelve una exepcion
busqueda_index =cadena3.index("8")

#si es numerico devuelve true si no false
si_Es_numerico =cadena3.isnumeric()

#si es numerico devuelve false 
si_Es_isalpha =cadena3.isalpha()

#busca una cadena en otra cadena y devuelve la cantidad de coincidencia
contar_coincidencia = cadena1.count("a")

#cuantos carateres tiene una cadena
cuantos_carateres =len(cadena1)

#verifica si una cadena enpieza con otra cadena 
enpieza_con = cadena1.startswith("a")

#remplaza una cadena por otra 
cadena_nueva =cadena1.replace("la","sol")

#separar cadenas por cadenas
separar_cadena = cadena1.split(",")

print(separar_cadena[2])