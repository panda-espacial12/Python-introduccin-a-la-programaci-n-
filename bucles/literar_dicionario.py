dicionario = {
    "nombre": "lucas",
    "apellido": "dalto",
    "subs": 1000000
}
#recoriendo dicionario para obtener la clave
for datos in dicionario:
    key = datos[0]
    print(f"la clave es: {key}")

#recoriendo dicionario para obtener la clave y los valores
for datos in dicionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es: {value}")



