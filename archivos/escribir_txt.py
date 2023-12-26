with open("archivos\\texto3_escribir.txt","w",encoding="UTF-8") as archivo:
     #sobrescribiendo el archivo 
     #archivo.write("jajajajaj te la recontra teclee")

     #agregando 2 lineas con writelines
     archivo.writelines([ "- hola meastro como andas\n" ,"- misericordia"])

     #agregando otras 2 lineas 
     archivo.writelines([ "- no se porque dijiste eso \n","- yo tanpoco"])

     

