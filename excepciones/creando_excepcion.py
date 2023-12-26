#crando mi propia excepcion personalizada
class miexcepcion(Exception):
    def __init__(self,err):
        print(f"impresionante, cometiste el siguiente error: {err}")
        
#lanzando mi propia excepcion
#raise miexcepcion("ajajjajaja persona poco culta")

#manejandola
try:
    raise miexcepcion("jajajaj persona como culta")
except:
    print("como vas a cometer ese error")