from tkinter import *

import customtkinter

# criar o aplicativo Tk
menu_inicial = Tk()

# da um titulo para o app
menu_inicial.title('Cadastro de Clientes')

width = int(menu_inicial.winfo_screenwidth())
height = int(menu_inicial.winfo_screenheight())
x = (5 * width) // 10
y = (5 * height) // 10

comeco_width = str(int(menu_inicial.winfo_screenwidth()) // 4)
comeco_height = str(int(menu_inicial.winfo_screenheight()) // 4)



# ajusta a dimensão do aplicativo: geometry(x,y,começoX, começoY)
menu_inicial.geometry(f'{x}x{y}+{comeco_width}+{comeco_height}')

# indica se o app vai ser redimensinável, sendo resizable(xRedimensionavel:bool, yRedimensionavel:bool)
menu_inicial.resizable(False, False)
menu_inicial.iconbitmap('ico.ico')


# menu_inicial['bg'] = 'black'


# da a dimensão mínima
# menu_inicial.minsize(widht=500,height=250)
# inicia o app com a tela toda aberta
# menu_inicial.state('zoomed')
# da o loop no app

menu_inicial.mainloop()
