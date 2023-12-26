import pandas as pd

##usando la funcion read_csv para el archivo csc
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#obteniendo los datos de la columna nombre
nombre = df["nombre"]

#ordenando dataframe por la edad 
df_ordenado_ascendente = df.sort_values("edad")

#ordenando de forma decendente
df_ordenado_decendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenando = pd.concat([df,df2])

#accediendo a la primera 3 filas con head()
primeras_filas = df.head(3)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#ascediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadisticas del dataframe
df_info = df.describe()

#acediendo a la edad de la fila 2
elementos_especificos_loc = df.loc[2,"edad"]

#accediendo a la edad de la fila 2 con iloc
elementos_especificos_loc = df.iloc[2,2]

#acediendoo a todas las filas de una columna
apellido = df.iloc[:,1]

#accediendo a la fila 3 con iloc
fila_3 = df.loc[2,:]

#acediendo a la fila 3 con iloc 
fila_3 = df.loc[2,:]

#acideindo a las filas que la edad sea mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]

print(mayor_que_30)