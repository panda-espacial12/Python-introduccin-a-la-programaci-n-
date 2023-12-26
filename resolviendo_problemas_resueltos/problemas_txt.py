#2 listas, una con nombre otra con apellido
nombres  =["lucas","matias","camila","pedro","roberto"]
apellidos =["dalto","zing","dalto","robetrix","tarado"]

#registrar esra infromacion en un TXT de forma optima

with open("resolviendo_problemas_resueltos\\nombres_y_apellidos.txtnombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"nombre: {n}\napellidos: {a}\n--------\n") for n,a in zip(3s,apellidos)]