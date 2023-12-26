import re 

#detectamos un numero ABA y ocultandolo
texto = "hola pedro mi numero es +54 11 3453-2453 +54 11 1234-4252"

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

remplazo = re.sub(pattern,"(numero oculto)",texto)

print(remplazo)