#
archivo = open ("archivos\\texto.txt" ,encoding="UTF-8")


#leer archivo completo 
#arcgivo = archivo_sin_leer.read()

#leer linea por linea
#archivo = archivo_sin_leer.readlines()

#leer una sola linea 
linea = archivo.readline()

#cerrar el archivo 
archivo.close()

print(linea)

