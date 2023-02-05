from tkinter import * 
from ADT_Racional import Racional


root = Tk()

def sumar():
    var2.set('Sexo') 

root.config(bd = 30)
root.config(cursor='heart')

var1 = StringVar()
var2 = StringVar()

titulo1 = Label(root, text='Expresión racional: (Con notación RPN)')
titulo1.pack()
entrada1 = Entry(root, justify='center', textvariable=var1)
entrada1.pack()

titulo2 = Label(root, text='Resultado: ')
titulo2.pack()
entrada2 = Entry(root, justify='center', textvariable=var2)
entrada2.pack()

btn = Button(root, text='Resultado', command=sumar)
btn.pack()

root.mainloop()