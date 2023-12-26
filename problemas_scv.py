#canbiar el tipo de dato de una columan 
import pandas as pd
df = pd.read_csv("archivos//datos.csv")

#convertir a sting los datos de una columna
df["edad"] = df["edad"].astype(str)

#mostar el tipo de dato del primer elemento de la columna edad 
# print(type(df["edad"][0]))

df["apellido"].replace("medina","maestro",inplace=True)
# print(df["apellido"])
print("lista original")
print(df)

#eliminando filas con datos faltantes
df = df.dropna()
print("lista modificada")
print(df)

#eliminar filas repetidas
df = df.drop_duplicates()
print("lista sin duplicados")
print(df)

#creando archivo scv (limpios)
df.to_csv("archivos//datos_limpios.csv") 
