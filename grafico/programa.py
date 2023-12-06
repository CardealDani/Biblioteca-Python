
from tkinter import ttk
from tkinter.ttk import Treeview
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
        self.informacoesMenu()

        img_botao_pegar_livro = PhotoImage(master=janela,file="grafico/imgs/img_botao_pegar_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_pegar_livro, text="", hover=False, command=self.funcaoPegarLivro)
        botao_pegar_livro.place(x=223,y=142)
        
        img_botao_devolver_livro = PhotoImage(master=janela,file="grafico/imgs/img_botao_devolver_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_devolver_livro, text="", hover=False, command=self.funcaoDevolverLivro)
        botao_pegar_livro.place(x=477,y=142)
        
        img_botao_buscar_livro = PhotoImage(master=janela,file="grafico/imgs/img_botao_buscar_livro.png")
        botao_buscar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_buscar_livro, text="", hover=False, command=self.funcaoBuscarLivro)
        botao_buscar_livro.place(x=223,y=370)
        
        img_botao_ver_historico = PhotoImage(master=janela,file="grafico/imgs/img_botao_ver_historico.png")
        botao_ver_historico = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_ver_historico, text="", hover=False, command=self.funcaoVerHistorico)
        botao_ver_historico.place(x=477,y=370) 
    
    def funcaoPegarLivro(self):
        self.informacoesMenu()
        frame_tabela = ttk.Frame(janela, width=600, height=350)
        frame_tabela.place(x=100, y=150)

        scroll_tabela = ttk.Scrollbar(frame_tabela)
        scroll_tabela.pack(side="right", fill="y")
        cols = ["ID", "TÍTULO", "AUTOR", "GÊNERO", "ESTADO"]

        tabela_livros = Treeview(frame_tabela, show="headings", yscrollcommand=scroll_tabela.set, columns=cols, height=18, selectmode="browse")
        tabela_livros.column("ID", width=60)
        tabela_livros.column("TÍTULO", width=140)
        tabela_livros.column("AUTOR", width=140)
        tabela_livros.column("GÊNERO", width=140)
        tabela_livros.column("ESTADO", width=140)


        for c in cols:
            tabela_livros.heading(c, text=c, anchor="w")
            tabela_livros.column(c, anchor="w", width=140)

        tabela_livros.pack(fill="both", expand=True)
        scroll_tabela.config(command=tabela_livros.yview)
        
        
        lista_livros = biblioteca.mostrar_livros()

        for col_id, _ in enumerate(cols):
            tabela_livros.tag_configure(f"col_{col_id}", background="#a0d2e4")
            tabela_livros.tag_configure(f"col_{col_id}_alt", background="#81bcb9")

        for i, livro in enumerate(lista_livros):
            cor_tag = f"col_0_alt" if i % 2 == 0 else "col_0"
            valores_livro = livro.__str__()
            
            tabela_livros.insert('', END, values=valores_livro, tags=f"linha_{i} {cor_tag}")
        
        # id_livro = ctk.CTkEntry(janela, width=690, height=30, font=self.my_font(15), placeholder_text="Digite um ID")
        # id_livro.place(x=100,y=120)
        # botao_id_livro = ctk.CTkButton(janela,30,30,text="➜",command=lambda: self.methodId(id_livro.get()))
        # botao_id_livro.place(x=790,y=120)
        
        tabela_livros.bind('<ButtonRelease-1>', lambda event: self.on_click(event, tabela_livros, lista_livros))
        
    def on_click(self, event, tabela, lista_livros):
        # Obtém a linha clicada
        item = tabela.identify('item', event.x, event.y)
        print(item)

        if item:
            # Obtém o índice da linha clicada
            i = self.pegar_indice_linha(item)-1
            id_livro = lista_livros[i].id
            id_livro = biblioteca.binary_search(lista_livros,id_livro)
            print(biblioteca.verificarEstadoLivro(lista_livros[id_livro[1]].id))
            if biblioteca.verificarEstadoLivro(lista_livros[id_livro[1]].id):
                print("oi")
                botao_pegarlivro= ctk.CTkButton(janela,200,50,text="Pegar Livro",command=lambda: self.pegarLivroPorID(id_livro[1]))
                botao_pegarlivro.place(x=350,y=550)            
            

            
    def pegarLivroPorID(self,id_livro):
        data = input("teste: ")
        biblioteca.realizar_emprestimo(id_livro,data,self.usuario.id)
        self.funcaoPegarLivro()
        
    def pegar_indice_linha(self,item):
    # Verifique se a identificação começa com "I00" antes de tentar converter
        if item.startswith("I"):
            try:
                # Extrai a parte hexadecimal e converte para inteiro
                indice_hex = item[1:]
                indice_decimal = int(indice_hex, 16)
                return indice_decimal
            except ValueError:
                # Tratamento de erro se a conversão falhar
                return None
        else:
            # Retorna None se a identificação não começar com "I00"
            return None

    def funcaoDevolverLivro(self):
        ...
    def funcaoBuscarLivro():
        ...   
    def funcaoVerHistorico():
        ...
        
    def methodId(self,id_livro):
        if not id_livro.isnumeric():
            print(id_livro)
            print(type(id_livro))
            self.modal("Digite um ID válido!",command_button= self.funcaoPegarLivro)

            
        return int(id_livro )

    def informacoesMenu(self):
        label_img_bg = ctk.CTkLabel(master=janela, image=self.img_bg_menu_usuario, text="")
        label_img_bg.place(x=0, y=0)
        botao_voltar = ctk.CTkButton(master=janela,width=200,height=100,hover=False,bg_color="#60c6cb", fg_color="#60c6cb",text="",image=self.img_voltar_lib,command= self.run)
        botao_voltar.place(x=0,y=0)
        label_nome = ctk.CTkLabel(master=janela,text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb",text=f"Logado como: {self.usuario.nome} - {self.usuario.id}", font=self.my_font(10))
        label_nome.place(x=10,y=678)
    
    def criarInput(self, mensagem, w,h,font,eixo_x,eixo_y,text_color="#000000",bg="#206781", fg= None ):
        campo = ctk.CTkEntry(janela, width=w, height=h, font=self.my_font(font), placeholder_text=mensagem, bg_color=bg,fg_color=fg,placeholder_text_color=text_color)
        campo.place(x=eixo_x, y=eixo_y)
        if not campo.get().isnumeric():
            print(campo.get())
            self.modal("Digite um ID válido!",command_button=lambda:self.methodId(mensagem,w,h,font,eixo_x,eixo_y,text_color,bg,fg))
        return campo 
app = App()
app.run()