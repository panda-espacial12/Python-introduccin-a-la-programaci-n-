import re 
 
texto = '''hola mestro esta es la cadena 1 como estas mi capitan
 esta es la linea 2 de texto
 y esta es la final (linea 3 ) definiticamente mi capitan'''
 
 #haciendo una busqueda simple
 #resultado = re.findall("esta,texto")
 
 #/d -> busca digitos numericos del 0 - 9
 #resultado = re.findall(r"/d),texto
 
 #/D busca TODO menos digutos numericos 0 - 9
 #resultado = re.findall(r"D",texto)
 
 #/w busca caracteres alfa numericos a-z A-Z 0-9
 #resultado = re.findall(r"w",texto)
 
 #armando una cadena que busque un numero seguido de un punto y un espacion
 #resultado = re.findall(f/d/./s ,texto)
 
 #buscando el principio de una linea 
 #^ -> busca el comienzo de una linea 
#resultado = re.findall(f'^',texto,flags=re.M)

 #buscando el final de una linea 
#resultado = re.findall(f'capitan$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda (3 numeros esta vez)
#resultado = re.findall(r'/d{3}',texto)

#{n,m} -> al menos n como maximo m
#resultado = re.findall(r'/d{2,4}',texto)

# | -> busca una cosa o la otra 
resultado = re.findall(r'/d{2,4}|hola',texto)
 
print(resultado)