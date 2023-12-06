import customtkinter as ctk
from tkinter import *
from planilha import inserirDados
janela = ctk.CTk()


def config_menu():
    janela.title('Cadastro de Clientes')
    width = int(janela.winfo_screenwidth())
    height = int(janela.winfo_screenheight())
    x = (5 * width) // 10
    y = (5 * height) // 10
    comeco_width = str(int(janela.winfo_screenwidth()) // 4)
    comeco_height = str(int(janela.winfo_screenheight()) // 4)
    janela.geometry(f'{x}x{y}+{comeco_width}+{comeco_height}')
    janela.resizable(False, False)
    # janela.iconbitmap('ico.ico')

config_menu()

def cadastrar():
    dia = data.get()
    nome_cliente = cliente.get()
    tipo_processo = processo.get()
    valor = valor_input.get()
    entrada = entrada_input.get()
    pagamento = pagamento_input.get()
    parcela = parcela_input.get()
    obs = obs_input.get()
    
    
    data.delete(0, END)
    cliente.delete(0,END)
    valor_input.delete(0,END)
    entrada_input.delete(0,END)
    parcela_input.delete(0,END)
    obs_input.delete(0,END)
    inserirDados(dia, nome_cliente,tipo_processo,valor,entrada,pagamento,parcela,obs)


ctk.CTkLabel(janela, text='Cadastro de Clientes',
             font=("arial bold", 20)).pack(pady=10)




data = ctk.CTkEntry(janela,width=200,placeholder_text='Data',corner_radius=10)
data.pack()

cliente = ctk.CTkEntry(janela, width=300, placeholder_text='Cliente',corner_radius=10)
cliente.pack(pady=20)

text_var = ctk.StringVar(value='Tipo do processo')

processo = ctk.CTkOptionMenu(janela,values=['Trabalhista', 'Cível','Criminal'],variable=text_var,corner_radius=10,width=300)
processo.pack()

valor_input = ctk.CTkEntry(janela,width=200,placeholder_text='Valor',corner_radius=10)
valor_input.pack(pady=10)

entrada_input = ctk.CTkEntry(janela,width=200,placeholder_text='Entrada',corner_radius=10)
entrada_input.pack(pady=10)

pagamento_input = ctk.CTkOptionMenu(janela,values=['À vista','Crédito','Débito'],corner_radius=10)
pagamento_input.pack(pady=10)

parcela_input = ctk.CTkEntry(janela,width=200,placeholder_text='Parcela',corner_radius=10)
parcela_input.pack(pady=10)

obs_input = ctk.CTkEntry(janela,width=200,placeholder_text='Observação',corner_radius=10)
obs_input.pack(pady=10)

botao= ctk.CTkButton(janela,text='Cadastrar',command=cadastrar)
botao.pack(pady=30)


janela.mainloop()
