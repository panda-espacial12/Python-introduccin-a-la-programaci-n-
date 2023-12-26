with open("archivos\\texto3_escribir.txt","a",encoding="UTF-8") as archivo:
     #usando bucles para agregar lineas
     archivo.write("\n")
     for i in range(5):
         archivo.write(f"-linea {i+1} agregando \n")
     

