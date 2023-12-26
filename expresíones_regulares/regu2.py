import re 

#la cadena en la que se buscara los patrones
text = "a fecha es 23/06/2021 y el telefono es +1-555-555-555"

#el patron a buscar es 
pattern = r"/d{2}/d{2}/d{4}"

#el texto con el que se remplazara el patron
replacement = "fecha oculta"

#remplazar todas las apariciones en el cadena de texto
new_text = re.sub(pattern, replacement, text)

#imprimir el resultado 
print("texto modificado:", new_text)