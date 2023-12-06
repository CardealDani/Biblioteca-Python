from tkinter import *

app = Tk()

app.title('Entry')
app.geometry('500x300')
app.configure(background="#dde")

def funcao():
    print('opa')


barraMenu = Menu(app)
menuContatos = Menu(barraMenu,tearoff=0)
menuContatos.add_command(label='Novo',command=funcao)
menuContatos.add_command(label='Pesquisar',command=funcao)
menuContatos.add_command(label='Deletar',command=funcao)
menuContatos.add_separator()
menuContatos.add_command(label='Fechar',command=app.quit)
barraMenu.add_cascade(label='Contatos',menu=menuContatos)

menuManutencao=Menu(barraMenu,tearoff=0)
menuManutencao.add_command(label='Banco de Dados',command=funcao)
barraMenu.add_cascade(label='Manutenção',menu=menuManutencao)


app.config(menu=barraMenu)

 
app.mainloop()
