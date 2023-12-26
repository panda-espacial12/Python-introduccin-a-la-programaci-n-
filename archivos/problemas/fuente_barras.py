import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos\\problemas\\cofla_ingresos.csv')
#creando el grafico 
sns.barplot(x="fuente",y="ingresos",data=df)

#opteniendo el total de ingresos
total_ingresos = df["ingresos"].sum()

#mostrando el grafico total
print(f"el total de ingresos es de: ${total_ingresos} usd")


plt.show()