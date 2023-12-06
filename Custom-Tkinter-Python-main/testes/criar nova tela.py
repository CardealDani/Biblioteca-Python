import customtkinter as ctk

janela = ctk.CTk()

janela._set_appearance_mode("dark")

janela.title('Cadastro de Clientes')

janela.geometry("600x600")
janela.resizable(False, False)



# #fecha janela
# .iconify()
# #abre janela
# .deiconify()

def nova_tela():
    janela.iconify()
    nova_janela = ctk.CTkToplevel(janela)
    nova_janela.geometry(f"300x300")


btn = ctk.CTkButton(janela, text="Abrir nova janela", command=nova_tela).place(x=300, y=100)

janela.mainloop()
