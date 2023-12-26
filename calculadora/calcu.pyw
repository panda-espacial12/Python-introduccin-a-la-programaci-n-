from tkinter import *
ventana = Tk()
ventana.title("Calculadora")
#entrada
e_texto = Entry(ventana, font= ("calibri 20"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx =5, pady =5)
i = 0
#funciones 
def click_boton(valor):
    global i
    e_texto.insert(i,valor)
    i += 1

def borrar(): 
    e_texto.delete(0, END)
    i = 0

def operacion():
   ecuacion = e_texto.get()
   resultado = eval(ecuacion)
   e_texto.delete(0, END)
   e_texto.insert(0,resultado)
   i = 0
   #botones
boton1 = Button(ventana, text="1", width =5, height =2,command = lambda: click_boton(1))
boton2 = Button(ventana, text="2", width =5, height =2,command = lambda: click_boton(2))
boton3 = Button(ventana, text="3", width =5, height =2,command = lambda: click_boton(3))
boton4 = Button(ventana, text="4", width =5, height =2,command = lambda: click_boton(4))
boton5 = Button(ventana, text="5", width =5, height =2,command = lambda: click_boton(5))
boton6 = Button(ventana, text="6", width =5, height =2,command = lambda: click_boton(6))
boton7 = Button(ventana, text="7", width =5, height =2,command = lambda: click_boton(7))
boton8 = Button(ventana, text="8", width =5, height =2,command = lambda: click_boton(8))
boton9 = Button(ventana, text="9", width =5, height =2,command = lambda: click_boton(9))
boton0 = Button(ventana, text="0", width =13, height =2,command = lambda: click_boton(0))

boton_parentesis1 = Button(ventana, text="(", width =5, height =2,command = lambda: click_boton("("))
boton_parentesis2= Button(ventana, text=")", width =5, height =2,command = lambda: click_boton(")"))
boton_punto = Button(ventana, text=".", width =5, height =2,command = lambda: click_boton("."))


boton_delete = Button(ventana, text="AC", width =5, height =2,command = lambda: borrar())
boton_suma = Button(ventana, text="+", width =5, height =2,command = lambda: click_boton("+"))
boton_resta = Button(ventana, text="-", width =5, height =2,command = lambda: click_boton("-"))
boton_division = Button(ventana, text="/", width =5, height =2,command = lambda: click_boton("/"))
boton_multi = Button(ventana, text="x", width =5, height =2,command = lambda: click_boton("*"))
boton_igual = Button(ventana, text="=", width =5, height =2,command = lambda: operacion())

#botones fila 1
boton_delete.grid(row = 1, column = 0,  padx =5, pady =5)
boton_parentesis1.grid(row = 1, column = 1,  padx =5, pady =5)
boton_parentesis2.grid(row = 1, column = 2,  padx =5, pady =5)
boton_division.grid(row = 1, column = 3,  padx =5, pady =5)

#botone fila2 [7 8 9 x]  
boton7.grid(row = 2, column = 0,  padx =5, pady =5)
boton8.grid(row = 2, column = 1,  padx =5, pady =5)
boton9.grid(row = 2, column = 2,  padx =5, pady =5)
boton_multi.grid(row = 2, column = 3,  padx =5, pady =5)

#botone fila3 [4 5 6 +]
boton4.grid(row = 3, column = 0,  padx =5, pady =5)
boton5.grid(row = 3, column = 1,  padx =5, pady =5)
boton6.grid(row = 3, column = 2,  padx =5, pady =5)
boton_suma.grid(row = 3, column = 3,  padx =5, pady =5)

#botone fila4 [1 2 3 -]
boton1.grid(row = 4, column = 0,  padx =5, pady =5)
boton2.grid(row = 4, column = 1,  padx =5, pady =5)
boton3.grid(row = 4, column = 2,  padx =5, pady =5)
boton_resta.grid(row = 4, column = 3,  padx =5, pady =5)

#botone fila5 [0 . =]
boton0.grid(row = 5, column = 0, columnspan =2,  padx =5, pady =5)
boton_punto.grid(row = 5, column = 2,  padx =5, pady =5)
boton_igual.grid(row = 5, column = 3,  padx =5, pady =5)

ventana.mainloop()


