#importamos un modulo y asignamos el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde este modulo impotamos dos funciones 
from modulo_saludar import saludar,saludar_raro
#creamos las variables saludar 
saludo = saludar("lucas")
saludar_raro = saludar_raro("fran")



#saludo = m_saludar.saludar("lucas")
print(saludo)
print(saludar_raro)

#para ver todas las propuiedades de los metodos de el namepace
#print(dir(namespace))