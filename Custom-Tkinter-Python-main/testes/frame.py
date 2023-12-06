import customtkinter as ctk

janela = ctk.CTk()

janela.title('Cadastro de Clientes')
janela.geometry("700x400+600+300")
janela.resizable(False, False)


frame1 = ctk.CTkFrame(janela, 200, 330, fg_color="teal",bg_color='red',border_width=10,corner_radius=30).place(
    x=10, y=60)
frame2 = ctk.CTkFrame(janela, 200, 330,fg_color="green").place(x=230, y=60)
frame3 = ctk.CTkFrame(janela, 200, 330,fg_color="#2b0536").place(x=450, y=60)


janela.mainloop()
