import re
email = "corrreo27@example.com"

    # Expresión regular para validar direcciones de correo electrónico
patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    
    # Utilizamos re.match para verificar si el email cumple con el patrón
resultado = re.match(patron, email)
         
# Ejemplo de uso:
if resultado:
    print("El correo electrónico es válido.")
else:
    print("El correo electrónico no es válido.")
