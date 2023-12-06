import customtkinter as ctk

janela = ctk.CTk()

janela.title('Cadastro de Clientes')
janela.geometry("700x400")
janela.resizable(False, False)


def processo(escolha):
    if escolha == 'Outro':
        print("Escolha outro processo")
        dial = ctk.CTkInputDialog(title='Outro Processo',text='Escolha outro processo')
        print(f'Outro processo = {dial.get_input()}')

    else:
        print(f'Processo {escolha} escolhido')

string_var = ctk.StringVar(value='Tipo do Processo')
string_cliente = ctk.StringVar(value='Digite o nome do Cliente')

ctk.CTkLabel(janela,text="Menu de Opções", font=("arial bold",20)).pack(pady=20,padx =5)
ctk.CTkLabel(janela,text="Escolha o seu Processo: ", font=("arial bold",20)).pack()


menu = ctk.CTkOptionMenu(janela,
                         values=['Trabalhista','Cível','Criminal','Outro'],
                         command=processo,
                         variable=string_var,
                         corner_radius=20,
                         )
menu.pack(pady=10)


janela.mainloop()


