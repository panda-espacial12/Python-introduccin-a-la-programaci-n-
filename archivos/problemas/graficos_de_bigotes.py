import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos\\problemas\\bigotes.csv')

#creando el grafico 
sns.boxenplot(x="categoria",y="valor",data=df)

plt.show()



