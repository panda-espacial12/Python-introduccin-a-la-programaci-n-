import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('archivos\\problemas\\agua.csv')
print(df)

sns.lineplot(x="fecha",y="cantidad",data=df)
plt.plot("2-sep",9,"o")
plt.show()