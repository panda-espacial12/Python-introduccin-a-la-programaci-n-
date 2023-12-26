#las listas no pueden ser mexclas de claves y usamos frozenset para meter conjuntos
dicionario ={frozenset(["dalto","rancio"]):"jajaj"}

#creando diocionario con fromkeys() valor por defecto
dicionario =dict.fromkeys(["dalto","apellido"])

#creando diocionario con fromkeys() canbiando el valor por defecrto a "no se"
dicionario = dict.fromkeys(["dalto","apellido"],"no se")

print(dicionario)

