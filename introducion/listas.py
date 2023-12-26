print("Eliga su Pais De Origen")
print(
    """
    1-Argentina
    2-Colombia
      """)

eleccion =int(input("ingrese la opcion de la lista: "))

lista =("dulce de leche","mate","futbol")

if eleccion ==1: 
    print("""
          a usted le gusta 
          
          """)
    print(lista[0])
    print(lista[1])
    print(lista[2])
if eleccion ==2:
     lista=("cafe","tamales","Patatas rellenas")
     print("""
          a usted le gusta 
          
          """)
     print(lista[0]) 
     print(lista[1])
     print(lista[2])
else:
 print("ingrese una opcion valida")
eleccion =int(input("ingrese la opcion de la lista: "))

