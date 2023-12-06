
from metodos import *
import customtkinter as ctk
from tkinter import *
janela = ctk.CTk()
janela.geometry("900x700")
janela.title("Biblioteca CC")
janela.resizable(False, False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela.resizable(False,False)

class App:
    def __init__(self):
        self.img_bg = PhotoImage(master=janela, file="grafico/imgs/back.png")

    def run(self):
        self.menuApp()
        janela.mainloop()

    def menuApp(self):
        label_img_bg = ctk.CTkLabel(janela, image=self.img_bg, text="")
        label_img_bg.place(x=0, y=0)
        botao_usuario = ctk.CTkButton(janela, width=250, height=60, text="Logar como Usuário",
                                       font=self.my_font(), bg_color="#206781", fg_color="#206781", command=self.usuarioDigitarNome)
        botao_usuario.place(x=325, y=290)
        botao_bibliotecario = ctk.CTkButton(janela, width=290, height=60, text="Logar como Bibliotecário",
                                            font=self.my_font(), bg_color="#206781", fg_color="#206781")
        botao_bibliotecario.place(x=305, y=370)

    def usuarioDigitarNome(self):
        frame = ctk.CTkFrame(janela, 900, 700).place(x=0, y=0)
        label_img_bg = ctk.CTkLabel(master=janela, image=self.img_bg, text="")
        label_img_bg.place(x=0, y=0)
        botao_nome = ctk.CTkEntry(janela, width=250, height=60, font=self.my_font(20), placeholder_text="Digite aqui o seu nome", bg_color="#206781",fg_color="#206781")
        botao_nome.place(x=325, y=320)
        botao_entrarUsuario = ctk.CTkButton(janela, width=160, height=40, text="Entrar", font=self.my_font(),
                                             bg_color="#1aac77", fg_color="#1aac77", command=lambda: self.btnEntrarUsuario(botao_nome.get()))
        botao_entrarUsuario.place(x=370, y=400)

    def btnEntrarUsuario(self, usuario):
        if usuario.strip() == "":
            self.modal("Digite um nome válido", font=15, bg_top="#f05e5f", bg_bot="#d1b7b7", command_button=self.usuarioDigitarNome)
        else:
            usuario_menu = UsuarioMenu(usuario)
            usuario_menu.menu()

    def my_font(self, size_param=25):
        return ctk.CTkFont(family="Helvetica", size=size_param)

    def modal(self, mensagem, bg_top="#206781", bg_bot="#9bb0a7", font=25, command_button=None):
        frame = ctk.CTkFrame(janela, width=250, height=120).place(x=325, y=320)
        ctk.CTkLabel(master=janela, text=mensagem, bg_color=bg_top, width=250, height=60,
                      font=self.my_font(font)).place(x=325, y=320)
        botao_confirma = ctk.CTkButton(janela, width=250, height=60, text="OK!", font=self.my_font(15),
                                       command=command_button)
        botao_confirma.place(x=325, y=380)


class UsuarioMenu(App):
    def __init__(self, usuario):
        self.usuario = biblioteca.cadastrar_usuario(usuario)
        self.img_bg_menu_usuario = PhotoImage(master=janela, file="grafico/imgs/back_menu_usuario.png")
        self.img_voltar_lib = PhotoImage(master=janela,file="grafico/imgs/img_voltar_lib.png")
        super().__init__()

    def menu(self):
        label_img_bg = ctk.CTkLabel(master=janela, image=self.img_bg_menu_usuario, text="")
        label_img_bg.place(x=0, y=0)
        botao_voltar = ctk.CTkButton(master=janela,width=200,height=100,hover=False,bg_color="#60c6cb", fg_color="#60c6cb",text="",image=self.img_voltar_lib,command= self.run)
        botao_voltar.place(x=0,y=0)
        label_nome = ctk.CTkLabel(master=janela,text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb",text=f"Logado como: {self.usuario.nome} - {self.usuario.id}", font=self.my_font(10))
        label_nome.place(x=10,y=678)
#         Pegar livro
# 2- Devolver livro
# 3- Consultar livro
# 4- Ver Historico
        img_botao_pegar_livro = PhotoImage(master=janela,file="grafico/imgs/img_botao_pegar_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_pegar_livro, text="", hover=False)
        botao_pegar_livro.place(x=223,y=142)
        
        img_botao_devolver_livro = PhotoImage(master=janela,file="grafico/imgs/img_botao_pegar_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_pegar_livro, text="", hover=False)
        botao_pegar_livro.place(x=223,y=142)
        
        img_botao_consultar_livro = PhotoImage(master=janela,file="grafico/imgs/img_botao_pegar_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_pegar_livro, text="", hover=False)
        botao_pegar_livro.place(x=223,y=142)
        
        img_botao_ver_historico = PhotoImage(master=janela,file="grafico/imgs/img_botao_pegar_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_pegar_livro, text="", hover=False)
        botao_pegar_livro.place(x=223,y=142) 



app = App()
app.run()