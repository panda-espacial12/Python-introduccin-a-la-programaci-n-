lista =["lucas dalto","peter",True,1.85]

#es una lista que NO se puede modificar luego de definirlo
tupla =["lucas dalto","peter", True,1.85]

#esto  es valido
lista[3]= "maquinola"

#esto no es valido
#tupla[3]="maquinola"

indice =int(input("ingrese un indice del 0 al 3: "))
#while indice !=0:
  #  print("debe cargar un indice valido")
 #   indice =int(input("ingrese un indice del 0 al 3: "))
#if indice == 0:  
print(lista[indice])