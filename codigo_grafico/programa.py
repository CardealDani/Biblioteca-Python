from tkinter import ttk
from tkinter.ttk import Treeview
import customtkinter as ctk
from tkinter import *
from tkcalendar import *
from babel import numbers
import datetime
from estrutura import *

janela = ctk.CTk()
janela.geometry("900x600")
janela.title("Biblioteca CC")
janela.resizable(False, False)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela.resizable(False,False)




class App:
    def __init__(self):
        self.img_bg = PhotoImage(master=janela, file="imgs/back.png")

    def run(self):
        self.menuApp()
        janela.mainloop()

    def menuApp(self):
        label_img_bg = ctk.CTkLabel(janela, image=self.img_bg, text="")
        label_img_bg.place(x=0, y=0)
        botao_usuario = ctk.CTkButton(janela, width=250, height=60, text="Logar como Usuário",
                                       font=self.my_font(), bg_color="#206781", fg_color="#206781", command=self.usuarioDigitarNome)
        botao_usuario.place(x=325, y=290)
        botao_bibliotecario = ctk.CTkButton(janela, width=250, height=60, text="Cadastrar Livro",
                                            font=self.my_font(), bg_color="#206781", fg_color="#206781",command=self.botaoCadastrarLivro)
        botao_bibliotecario.place(x=325, y=370)

    def usuarioDigitarNome(self):
        frame = ctk.CTkFrame(janela, 900, 700).place(x=0, y=0)
        label_img_bg = ctk.CTkLabel(master=janela, image=self.img_bg, text="")
        label_img_bg.place(x=0, y=0)
        botao_nome = ctk.CTkEntry(janela, width=250, height=60, font=self.my_font(20), placeholder_text="Digite aqui o seu nome", bg_color="#206781",fg_color="#206781")
        botao_nome.place(x=325, y=320)
        botao_entrarUsuario = ctk.CTkButton(janela, width=160, height=40, text="Entrar", font=self.my_font(),
                                             bg_color="#1aac77", fg_color="#1aac77", command=lambda: self.btnEntrarUsuario(botao_nome.get()))
        botao_entrarUsuario.place(x=370, y=400)
        
        botao = ctk.CTkButton(janela,40,30,bg_color="#e1f4fb",fg_color="#e1f4fb",text_color="#000000",hover_color="#e1f4fb",text="🢠",font=self.my_font(50), command=self.menuApp)
        botao.place(x=40,y=330)

    def btnEntrarUsuario(self, usuario):
        if usuario.strip() == "":
            self.modal("Digite um nome válido", font=15, bg_top="#f05e5f", bg_bot="#d1b7b7", command_button=self.usuarioDigitarNome)
        else:
            usuario_menu = UsuarioMenu(usuario)
            usuario_menu.menu()

    def botaoCadastrarLivro(self):
        cadastrador = UsuarioMenu("Cadastrador")
        cadastrador.cadastrarLivro()
    
    def my_font(sx_p, size_param=25):
        return ctk.CTkFont(family="Helvetica", size=size_param)

    def modal(self, mensagem, bg_top="#206781", font=25, command_button=None,text_button = "OK!",w = 250, x_p=325,bg_bot="#9bb0a7"):
        frame = ctk.CTkFrame(janela, width=w, height=120).place(x=325, y=320)
        ctk.CTkLabel(master=janela,text=mensagem, bg_color=bg_top, width=250, height=60,
                      font=self.my_font(font)).place(x=x_p, y=320)
        botao_confirma = ctk.CTkButton(janela, width=250, height=60, text=text_button, bg_color=bg_bot, font=self.my_font(15),
                                       command=command_button)
        botao_confirma.place(x=325, y=380)

    def modalCalendario(self, id_livro,emprestimo = False):
        # Criação de uma janela de diálogo modal
        dialog = Toplevel(janela)

        hoje = datetime.date.today()
        ano = hoje.year
        mes = hoje.month
        dia = hoje.day

        cal = Calendar(dialog, selectmode="day", year=ano, month=mes, day=dia)
        cal.pack(pady=20)
        btn_cal = Button(dialog, text="Confirmar", command=lambda: self.fecharJanela(dialog, cal.get_date(),id_livro,emprestimo))
        btn_cal.pack()
        # Aguarda o término da janela de diálogo
        dialog.wait_window()

    def fecharJanela(self, dialog, data,id_livro,emprestimo = False):
        print(id_livro)

        dialog.destroy()
        if not emprestimo:
            
            biblioteca.realizar_emprestimo(id_livro,data,self.usuario.id)
            self.funcaoVerLivros(headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO"],widths=[40,165,165,165,165])
            label = ctk.CTkLabel(janela,text=f"Livro (ID - {biblioteca.livros[id_livro].id}) Emprestado!",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=350,y=60)
            
        else:
            biblioteca.realizar_devolucao(id_livro,data,self.usuario.id) 
            self.funcaoVerLivros(emprestimo=True,headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO"],widths=[40,165,165,165,165])
            id_emprestimo = biblioteca.binary_search(biblioteca.emprestimos,id_livro)
            label = ctk.CTkLabel(janela,text=f"Livro (ID -{biblioteca.emprestimos[id_emprestimo[1]].id}) Devolvido!",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=350,y=60)
            

class UsuarioMenu(App):
    def __init__(self, usuario):
        self.usuario = biblioteca.cadastrar_usuario(usuario)
        self.img_bg_menu_usuario = PhotoImage(master=janela, file="imgs/back_menu_usuario.png")
        self.img_voltar_lib = PhotoImage(master=janela,file="imgs/img_voltar_lib.png")
        super().__init__()

    def menu(self):
        self.informacoesMenu()

        img_botao_buscar_livro = PhotoImage(master=janela,file="imgs/img_botao_buscar_livro.png")
        botao_buscar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_buscar_livro, text="", hover=False, command=lambda:self.funcaoVerLivros(headings=["ID","TÍTULO","AUTOR","GÊNERO","ESTADO"], widths=[40,165,165,165,165]))
        botao_buscar_livro.place(x=130,y=250)

        img_botao_devolver_livro = PhotoImage(master=janela,file="imgs/img_botao_devolver_livro.png")
        botao_pegar_livro = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_devolver_livro, text="", hover=False, command= lambda: self.funcaoVerLivros(emprestimo=True, headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO"],widths=[40,165,165,165,165]))
        botao_pegar_livro.place(x=350,y=250)
        
        
        
        img_botao_ver_historico = PhotoImage(master=janela,file="imgs/img_botao_ver_historico.png")
        botao_ver_historico = ctk.CTkButton(master=janela,width=200,height=200,border_color="#000000", border_spacing=0, bg_color="#e1f4fb", fg_color="#e1f4fb", image=img_botao_ver_historico, text="", hover=False, command=lambda:self.funcaoVerLivros(historico=True,headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO","DATA_DEVOLUCAO"],widths=[40,132,132,132,132,132]))
        botao_ver_historico.place(x=570,y=250) 
    
    def funcaoVerLivros(self,emprestimo=False,historico = False,headings = [], widths = []):
        self.informacoesMenu()
        self.botaoVoltarMenu(comando=self.menu)
        frame_tabela = ttk.Frame(janela, width=600, height=350)
        frame_tabela.place(x=100, y=150)

        scroll_tabela = ttk.Scrollbar(frame_tabela)
        scroll_tabela.pack(side="right", fill="y")
        cols = headings
        tabela_livros = Treeview(frame_tabela, show="headings", yscrollcommand=scroll_tabela.set, columns=cols, height=18, selectmode="browse")
        for coluna in range(len(cols)):
            tabela_livros.column(cols[coluna],width=widths[coluna])
            tabela_livros.heading(cols[coluna], text=cols[coluna], anchor="w")


        tabela_livros.pack(fill="both", expand=True)
        scroll_tabela.config(command=tabela_livros.yview)
        
        if emprestimo:
            lista_livros = biblioteca.mostrar_livros(emprestimo=True,usuario_id=self.usuario.id)

        elif historico:
            lista_livros = biblioteca.mostrar_livros(historico = True, usuario_id= self.usuario.id)
        else: 
            lista_livros = biblioteca.mostrar_livros()


        for col_id, _ in enumerate(cols):
            tabela_livros.tag_configure(f"col_{col_id}", background="#a0d2e4")
            tabela_livros.tag_configure(f"col_{col_id}_alt", background="#81bcb9")
        

        for i, livro in enumerate(lista_livros):
            cor_tag = f"col_0_alt" if i % 2 == 0 else "col_0"
            valores_livro = livro.retorno(emprestimo=emprestimo, historico=historico)

            # Inserir valores na tabela e aplicar a tag
            tabela_livros.insert('', END, values=valores_livro, tags=f"linha_{i} {cor_tag}")
                # for v in range(len(valor)):
                #     print(v)
                #     print(valor)
                # # for v in valor:
                #     print(v)
                #     # tabela_livros.insert('', END, values=valor,  tags=f"linha_{i} {cor_tag}")

        tipo_busca = StringVar(janela,"Filtro")
        botao_filtro_busca = ctk.CTkOptionMenu(janela,values=headings,  variable=tipo_busca,width=100,height=30,)
        botao_filtro_busca.place(x=100,y=120)
         
        search_entry = ctk.CTkEntry(janela,placeholder_text="Escolha o filtro e busque aqui",placeholder_text_color="#ffffff", width=590,height=30, font=self.my_font(15))
        search_entry.place(x=200,y=120)
        
        botao_search_entry = ctk.CTkButton(janela,50,30,text="➜",command=lambda: self.funcaoFiltroBusca(tipo_busca,search_entry,tabela_livros,lista_livros,headings,widths,emprestimo,historico))
        botao_search_entry.place(x=770,y=120)
        if emprestimo:
            tabela_livros.bind('<ButtonRelease-1>', lambda event: self.on_click(event, tabela_livros, lista_livros, devolver=True))
        else:
            tabela_livros.bind('<ButtonRelease-1>', lambda event: self.on_click(event, tabela_livros, lista_livros))
        
    def funcaoFiltroBusca(self, tipo,value_input,tabela_livros,lista_livros,headings,width,emprestimo,historico):
        tipo = tipo.get()
        valor_input = value_input.get()
        livros_filtrados = []
        if tipo != "Filtro":
            if valor_input != "":
                # Limpa a tabela
                for record in tabela_livros.get_children():
                    tabela_livros.delete(record)

                # Obtém a lista original de livros

                # Filtra os livros com base no tipo de busca e valor inserido
                
                for livro in lista_livros:
                    if tipo == "ID" and str(livro.id) == valor_input:
                        livros_filtrados.append(livro)
                    elif tipo == "TÍTULO" and valor_input.lower() in livro.titulo.lower():
                        livros_filtrados.append(livro)
                    elif tipo == "AUTOR" and valor_input.lower() in livro.autor.lower():
                        livros_filtrados.append(livro)
                    elif tipo == "GÊNERO" and valor_input.lower() in livro.tag.lower():
                        livros_filtrados.append(livro)
                    elif tipo == "DATA_EMPRESTIMO" and valor_input.lower() in livro.tag.lower():
                        livros_filtrados.append(livro)

                # Preenche a tabela com os livros filtrados
                for i, livro in enumerate(livros_filtrados):
                    cor_tag = f"col_0_alt" if i % 2 == 0 else "col_0"
                    valores_livro = livro.__str__()
                    tabela_livros.insert('', END, values=valores_livro, tags=f"linha_{i} {cor_tag}")
            else:
                if emprestimo:
                    self.funcaoVerLivros(emprestimo=True, headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO"],widths=[40,165,165,165,165])
                elif historico:
                    self.funcaoVerLivros(historico=historico,headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO","DATA_DEVOLUCAO"],widths=[40,132,132,132,132,132])
                else:
                    self.funcaoVerHistorico(headings=["ID","TÍTULO","AUTOR","GÊNERO","ESTADO"], widths=[40,165,165,165,165])
                    
        else:
            if emprestimo:
                    self.funcaoVerLivros(emprestimo=True, headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO"],widths=[40,165,165,165,165])
            elif historico:
                self.funcaoVerLivros(historico=historico,headings=["ID","TÍTULO","AUTOR","ESTADO","DATA_EMPRESTIMO","DATA_DEVOLUCAO"],widths=[40,132,132,132,132,132])
            else:
                self.funcaoVerHistorico(headings=["ID","TÍTULO","AUTOR","GÊNERO","ESTADO"], widths=[40,165,165,165,165])
            
            
    def cadastrarLivro(self):
        self.informacoesMenu()
        self.botaoVoltarMenu(comando=self.menuApp)
        ctk.CTkLabel(janela,text="ID").place()
        
        label_id = ctk.CTkLabel(janela,text="ID",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=230,y=174)
        id_livro = ctk.CTkEntry(janela, width=350,height=50, font=self.my_font(20),text_color="#000000",corner_radius=3,fg_color="#60c6cb")
        id_livro.place(x=275,y=164)
        
        label_titulo = ctk.CTkLabel(janela,text="Título",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=200,y=280)
        titulo = ctk.CTkEntry(janela, width=350,height=50, font=self.my_font(20),text_color="#000000",corner_radius=3,fg_color="#60c6cb")
        titulo.place(x=275,y=270)
        
        label_autor = ctk.CTkLabel(janela,text="Autor",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=200,y=398)
        autor = ctk.CTkEntry(janela, width=350,height=50, font=self.my_font(20),text_color="#000000",corner_radius=3,fg_color="#60c6cb")
        autor.place(x=275,y=378)

        label_autor = ctk.CTkLabel(janela,text="Gênero",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=180,y=495)
        genero = ctk.CTkEntry(janela, width=350,height=50, font=self.my_font(20),text_color="#000000",corner_radius=3,fg_color="#60c6cb")
        genero.place(x=275,y=485)

        ctk.CTkButton(janela,text="Cadastrar",width=200,height=50, font=self.my_font(20),command=lambda:self.getData(id_livro,titulo,autor,genero)).place(x=665,y=325) 
            
        
    def getData(self,id_livro,titulo,autor,genero):
        id_livro= id_livro.get()
        titulo = titulo.get()
        autor = autor.get()
        genero= genero.get()
        
        if id_livro != "" and titulo != "" and autor != "" and genero != "" :
            if not biblioteca.emptyId(id_livro):
                biblioteca.cadastrar_livro(int(id_livro),titulo,autor,genero)
                self.cadastrarLivro()
                label = ctk.CTkLabel(janela,text="Livro Cadastrado com Sucesso!",font=self.my_font(),text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=350,y=60)
            else:
                label = ctk.CTkLabel(janela,text="ID já utlizado!",font=self.my_font(),text_color="#ff0000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=350,y=60)
        else: 
            label = ctk.CTkLabel(janela,text="Digite os valores!",font=self.my_font(),text_color="#ff0000",bg_color="#e1f4fb",fg_color="#e1f4fb").place(x=350,y=60)
        
        
           
    def on_click(self, event, tabela_livros, lista_livros,devolver=False):
        # Obtém a linha clicada
        item = tabela_livros.identify('item', event.x, event.y)
        id_livro = tabela_livros.item(item)["values"][0]
        if item:
            id_para_emprestimo = id_livro
            id_livro = biblioteca.emptyId(id_livro)
            if not devolver:
                if  lista_livros[id_livro[1]].estado== "Disponível":
                    botao_pegarlivro= ctk.CTkButton(janela,200,40,text="Pegar Livro",command=lambda: self.modalCalendario(id_livro[1]))
                    botao_pegarlivro.place(x=350,y=540)         
                else: 
                    botao_pegarlivro= ctk.CTkLabel(janela,200,40,text="Livro indisponível")
                    botao_pegarlivro.place(x=350,y=540)
            else: 
                    botao_pegarlivro= ctk.CTkButton(janela,200,40,text="Devolver Livro",command=lambda: self.modalCalendario(id_para_emprestimo,emprestimo=True))
                    botao_pegarlivro.place(x=350,y=540)  
                

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

    def funcaoVerHistorico():
        ...
        
    def methodId(self,id_livro):
        if not id_livro.isnumeric():
            print(id_livro)
            print(type(id_livro))
            self.modal("Digite um ID válido!",command_button= self.funcaoVerLivros)

            
        return int(id_livro )

    def informacoesMenu(self):
        label_img_bg = ctk.CTkLabel(master=janela, image=self.img_bg_menu_usuario, text="")
        label_img_bg.place(x=0, y=0)
        botao_voltar = ctk.CTkButton(master=janela,width=200,height=100,hover=False,bg_color="#60c6cb", fg_color="#60c6cb",text="",image=self.img_voltar_lib,command= self.run)
        botao_voltar.place(x=0,y=0)
        label_nome = ctk.CTkLabel(master=janela,text_color="#000000",bg_color="#e1f4fb",fg_color="#e1f4fb",text=f"Logado como: {self.usuario.nome} - {self.usuario.id}", font=self.my_font(15))
        label_nome.place(x=10,y=568)
    def botaoVoltarMenu(self,comando):
        botao = ctk.CTkButton(janela,40,30,bg_color="#e1f4fb",fg_color="#e1f4fb",text_color="#000000",hover_color="#e1f4fb",text="🢠",font=self.my_font(50), command=comando)
        botao.place(x=10,y=330)
        
    def criarInput(self, mensagem, w,h,font,eixo_x,eixo_y,text_color="#000000",bg="#206781", fg= None ):
        campo = ctk.CTkEntry(janela, width=w, height=h, font=self.my_font(font), placeholder_text=mensagem, bg_color=bg,fg_color=fg,placeholder_text_color=text_color)
        campo.place(x=eixo_x, y=eixo_y)
        if not campo.get().isnumeric():
            print(campo.get())
            self.modal("Digite um ID válido!",command_button=lambda:self.methodId(mensagem,w,h,font,eixo_x,eixo_y,text_color,bg,fg))
        return campo 



app = App()
app.run()