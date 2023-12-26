numerosecreto =10
print (
    """
      ┌─────────────┐
      │  Bienvenido │  
      │  a mi Juego!│ 
      └─────────────┘
       """)
num =int(input("ingrese el numero: "))
while num!=numerosecreto:
    print("!ja ja !estas atrapado en mi ciclo!")
    num = int(input("ingresa el numero:"))
    if num==numerosecreto:
        print("bien echo,muggle!eres el numero 1")
        print("el numero era:",numerosecreto)