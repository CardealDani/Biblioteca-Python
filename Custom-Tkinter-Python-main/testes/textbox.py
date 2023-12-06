import customtkinter as ctk

janela = ctk.CTk()

janela.title('Cadastro de Clientes')
janela.geometry("700x400+600+300")
janela.resizable(False, False)
janela.iconbitmap('ico.ico')

textbox = ctk.CTkTextbox(janela,width=300,height=350)
textbox.pack()
textbox.insert("0.0","Título do texto\n\n"+"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s\n\n"*20)

janela.mainloop()
