import os
import time
from biblioteca import *


class Sistema:
    def run(self):
        while True:
            os.system('cls')
            print("""Boas vindas ao sistema de bibliotecas.
Escolha uma das opções abaixo para logar:

1- Logar como Usuário
2- Logar como Bibliotecário
3- Sair
                """)
            escolha = input('Digite aqui o valor desejado: ')
            if escolha == '1':
                os.system('cls')
                nome = input("Digite aqui seu nome: ")
                if nome != '':
                    usuario = UsuarioMenu(nome)
                    usuario.menu()
                else:
                    print('Nome inválido')
                    continue
            elif escolha == '2':
                os.system('cls')
                bibliotecario = BibliotecarioMenu()
                bibliotecario.menu()
            elif escolha == '3':
                return print("Obrigado pela preferência, volte sempre!")
            else:
                print("""Valor inválido""")



class UsuarioMenu:
    def __init__(self, nome):
        self.usuario = biblioteca.cadastrar_usuario(nome)

    def menu(self):
        os.system('cls')
        print(f"Logado como: {self.usuario.nome} - ID: {self.usuario.id}")
        print(f"Seja bem vindo: {self.usuario.nome}!")
        while True:
            print("""O que deseja fazer?
1- Pegar livro
2- Devolver livro
3- Consultar livro
4- Ver Historico
5- Voltar ao menu principal\n""")
            escolha_menu = self.methodInput('Digite aqui o valor desejado: ')
            if escolha_menu == '1':
                os.system('cls')
                print("Escolha das opções abaixo, o livro que quer pegar")
                biblioteca.mostrar_livros()
                print("")
                self.pegarLivro()
            elif escolha_menu == '2':
                self.devolverLivro()
            elif escolha_menu == '3':
                self.menuConsultarLivro()
            elif escolha_menu == '4':
                self.verHistorico()
            elif escolha_menu == '5':
                return

    def pegarLivro(self, id_parametro=None):
        if id_parametro == None:
            id_livro = int(self.methodInput(mensagem="Digite aqui o ID do livro: "))
            if id_livro == "$":
                return
            aux = biblioteca.emptyId(id_livro)
            
            if not aux:
                print("Não existe nenhum livro com esse ID")
            else:
                id_livro = aux[1]
        else:
            id_livro = int(id_parametro)
        if id_livro > biblioteca.len_livros() or id_livro < 0:
            print('ID inválido! Tente novamente\n')
        elif biblioteca.verificarEstadoLivro(int(id_livro)) =="Emprestado":
            # os.system('cls')
            print('Não foi possivel concluir o pedido. O livro ja esta emprestado.')
        else:
            data = input("Digite aqui a data de empréstimo em dd/mm/yyyy: ")
            biblioteca.realizar_emprestimo(id_livro, data, self.usuario.id)

    def devolverLivro(self):
        os.system('cls')
        print("Escolha um livro para devolver:")
        for u in self.usuario.livros:
            print(f'Id: {u.id} - Titulo: {u.titulo} - Estado: {u.estado}')
        id_escolha =int(self.methodInput(mensagem="Digite aqui o ID do livro para devolver:"))
        if id_escolha == "$":
            return
        id_emprestimo = biblioteca.emptyId(int(id_escolha),emprestimo=True)
        if id_emprestimo:
            data_devolucao = input("Digite aqui a data de devolução em dd/mm/yyyy: ")
            result = biblioteca.realizar_devolucao(id_escolha,id_emprestimo[1], data_devolucao, self.usuario.id)
            print(result)
        else: print("Nenhum livro emprestado com esse ID")
        
    def menuConsultarLivro(self):
        os.system('cls')
        print("Consulta de Livros")
        print("")
        print("""1- Buscar livro por ID
2- Buscar livro por Titulo
3- Buscar livro por Autor
4- Buscar livro por Gênero
5- Ver todos os livros
9- Retornar""")
        escolha_busca =self.methodInput(mensagem="Digite aqui sua escolha: ")
        if escolha_busca == "9":
            os.system('cls')
            return 
        if escolha_busca == '1':
            self.buscarPorId()
        elif escolha_busca == '2':
            self.buscarPorTitulo()
        elif escolha_busca == '3':
            self.buscarPorAutor()
        elif escolha_busca == '4':
            self.buscarPorGenero()
        elif escolha_busca == '5':
            self.buscarTodos()

    def verHistorico(self):
        os.system('cls')
        if self.usuario.historico:
            for u in self.usuario.historico:
                print(
                    f'Id: {u.id} - Titulo: {u.titulo} - Estado: {u.estado}')
        else:
            print("Sem movimento por aqui! :)")

            ver_livro = self.methodInput(
                "Deseja ver os livros?\n1 - Sim\n2 - Não\n\nDigite aqui sua escolha: ")
            if ver_livro == "$":
                return
            
            if ver_livro == '1':
                print("")
                self.pegarLivroBusca(mostrar_livros=True)
            elif ver_livro == '2':
                self.menu()

    def buscarPorId(self):
        os.system('cls')
        escolha_busca_id = int(self.methodInput(mensagem="Digite aqui o ID do livro: "))
        if escolha_busca_id == "$":
            return
        print("")
        id_atual = biblioteca.emptyId(escolha_busca_id)
        if id_atual:
            print(biblioteca.mostrar_por_id(id_atual[1]))
            if biblioteca.verificarEstadoLivro(id_atual[1]) == "Disponível":
                print("")
                print("O livro está Disponível, deseja pegar emprestado?\n1- Sim\n2- Não\n\n")

                escolha = self.methodInput("Digite aqui a sua escolha: ")
                if escolha == "$":
                    return
                            
                print(" ")
                if escolha == '1':
                    self.pegarLivroBusca(id_livro=id_atual[1])
                elif escolha == '2':
                    os.system('cls')
                    self.pegarLivroBusca()
            else:
                print("O livro não está disponível para emprestimo")
                print("")
                self.pegarLivroBusca()
        else:
            print("Não existe nenhum livro em nossa biblioteca com esse ID")
            
    def buscarPorTitulo(self):
        os.system('cls')
        escolha_busca_titulo = input('Digite o Título do livro: ')
        print("")

        biblioteca.buscar_por_titulo(escolha_busca_titulo)
        print("")
        self.pegarLivroBusca()

    def buscarPorAutor(self):
        os.system('cls')
        escolha_busca_autor = input('Digite o Autor do livro: ')
        print("")
        biblioteca.buscar_por_autor(escolha_busca_autor)
        print(" ")
        self.pegarLivroBusca()

    def buscarPorGenero(self):
        os.system('cls')
        escolha_busca_genero = input('Digite o Gênero do livro: ')
        print(" ")
        biblioteca.buscar_por_genero(escolha_busca_genero)
        print(" ")
        self.pegarLivroBusca()     
    
    def buscarTodos(self):
        os.system('cls')
        biblioteca.mostrar_livros()
        print(" ")
        self.pegarLivroBusca()
    
    def pegarLivroBusca(self, id_livro=None, mostrar_livros=False):
        if mostrar_livros:
            biblioteca.mostrar_livros()
            print("")
            self.pegarLivro()
        elif id_livro != None:
            self.pegarLivro(id_parametro=id_livro)
        elif id_livro == None:
            print("""Se desejar pegar algum livro, digite 1
Se desejar voltar ao menu digite 2
Se deseja sair, digite 9\n""")
            escolha_pegar_livro = self.methodInput("Digite aqui sua escolha: ")
            if escolha_pegar_livro == '1':
                print("""Digite o ID do livro.
Se não souber o id do livro, digite 'm' para mostrar os livros.""")
                input_id = self.methodInput("Digite aqui: ", True)
                if input_id == 'm':
                    biblioteca.mostrar_livros()
                    print(" ")
                    self.pegarLivro()
                else:
                    self.pegarLivro(id_parametro=input_id)
            elif escolha_pegar_livro == '2':
                self.menuConsultarLivro()
            elif escolha_pegar_livro == '9':
                return

    def methodInput(self, mensagem, campoTexto = False):
        campo = input(mensagem)
        while not campo.isnumeric():
            if campoTexto and campo == "m":
                return campo
            campo = input('Digite um valor válido: ')
           
        return campo 


class BibliotecarioMenu:
    def menu(self):
        os.system('cls')
        print(f"Logado como bibliotecario!\n")
        print(f"Seja bem vindo!\n")
        while True:
            print("""O que deseja fazer?\n
1- Cadastrar livro
2- Editar livro
3- Excluir livro
4- Ver livros
5- Ver Relatório de empréstimo
6- Voltar ao menu principal\n""")
            escolha_menu = self.methodInput('Digite aqui o valor desejado: ')
            if escolha_menu == '1':
                os.system('cls')
                self.cadastrarLivro()
            elif escolha_menu == '2':
                self.editarLivro()
            elif escolha_menu == '3':
                self.excluirLivro()
            elif escolha_menu == '4':
                self.verLivros()
            elif escolha_menu == '5':
                self.verRelatorioEmprestimo()
            elif escolha_menu == "6": 
                return
            
    def cadastrarLivro(self):
        # biblioteca.mostrar_livros()
        # print("")
        # print("Esses são os livros já cadastrados ^ \n")
        id_livro = int(self.methodInput("Digite um ID para o livro: "))
        while biblioteca.emptyId(id_livro):
            id_livro = self.methodInput("ID já existente!\n Tente outro ID do livro: ")
            
        titulo = input("Digite um Título para o Livro: ")
        autor = input("Digite um Autor para o Livro: ")
        genero = input("Digite um Gênero para o Livro: ")
        confirma = self.methodInput("Confirmar cadastro?\n1- Sim\n2- Não\nR:")
        if confirma == "1":
            if biblioteca.cadastrar_livro(id_livro,titulo,autor,genero):
                os.system('cls')
                print("Livro cadastrado com sucesso!\n\n")
                time.sleep(0.7)
                return
        else: 
            print("Cadastro cancelado!")
            time.sleep(0.7)
            return
            
    def editarLivro(self):
        os.system('cls')
        id_livro = int(self.methodInput("Digite aqui o ID do livro que deseja editar: "))
        verificarLivro = biblioteca.emptyId(id_livro)
        if verificarLivro:
            id_livro = verificarLivro[1]
            escolha_editar = None
            while escolha_editar != "9":
                
                print(biblioteca.mostrar_por_id(id_livro))
                print("\nEscolha o que deseja editar:\n1- ID\n2- Título\n3- Autor\n4- Gênero\n9- Voltar ao menu\n")
                escolha_editar = self.methodInput("R:")
                
                if escolha_editar == "1":
                    os.system('cls')
                    novo_id = int(self.methodInput("Digite o novo ID: "))
                    result = biblioteca.emptyId(novo_id)
                    print(novo_id)
                    if result:
                        print("\nID já em uso. Tente outro ID\n")
                    else:
                        aux = biblioteca.editarLivro(id_livro,novo_id=novo_id)
                        id_livro = aux[1]
                        print("ID editado com sucesso!\n")
                elif escolha_editar == "2":
                    os.system('cls')
                    novo_titulo = input("Digite o novo Título: ")
                    biblioteca.editarLivro(id_livro,novo_titulo=novo_titulo)
                    print("Título editado com sucesso!")
                elif escolha_editar == "3":
                    os.system('cls')
                    novo_autor = input("Digite o novo Autor: ")
                    biblioteca.editarLivro(id_livro,novo_autor=novo_autor)
                    print("Autor editado com sucesso!")
                elif escolha_editar == "4":
                    os.system('cls')
                    novo_genero = input("Digite o novo Gênero: ")
                    biblioteca.editarLivro(id_livro,novo_genero=novo_genero)
                    print("Gênero editado com sucesso!")
            return os.system('cls')
        
    def excluirLivro(self):
        os.system('cls')
        print(biblioteca.mostrar_livros())
        print("")
        id_livro = int(self.methodInput("Digite aqui o ID do livro que deseja excluir: "))
        
        verificarLivro = biblioteca.emptyId(id_livro)
        id_livro = verificarLivro[1]
        if verificarLivro:
            confirma = self.methodInput("Confirmar exclusão?\n1- Sim\n2- Não\nR:")
            if confirma == "1":
                biblioteca.excluirLivro(id_livro)
                print("Excluído com sucesso!")
            else: print("Exclusão cancelada!")
    def verLivros(self):
        os.system('cls')
        print(biblioteca.mostrar_livros())
    def verRelatorioEmprestimo(self):
        os.system('cls')
        for r in biblioteca.relatorio_emprestimos():
            print(r)
            
            
    def methodInput(self, mensagem, campoTexto = False):
        campo = input(mensagem)
        while not campo.isnumeric():
            if campoTexto and campo == "m":
                return campo
            campo = input('Digite um valor válido: ')
           
        return campo 

        

sistema = Sistema()
sistema.run()
