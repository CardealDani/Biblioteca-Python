import os
from main import *


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
                return self.funcoesBibliotecario()
            elif escolha == '3':
                return print("Obrigado pela preferência, volte sempre!")
            else:
                print("""Valor inválido""")

    def funcoesUsuario(self, nome):
        usuario = biblioteca.cadastrar_usuario(nome)
        os.system('cls')

        while True:

            print(f"Logado como: {usuario.nome} - ID: {usuario.id}")

            print(f"""Seja bem vindo: {usuario.nome}!
            O que deseja fazer?

            1- Pegar livro
            2- Devolver livro
            3- Consultar livros
            4- Ver Historico
            5- Voltar ao menu principal""")
            escolha = input('Digite aqui o valor desejado: ')
            if escolha == '1':
                os.system('cls')
                print("Escolha das opções abaixo, o livro que quer pegar")
                biblioteca.mostrar_livros()
                id_livro = int(input("Digite aqui o ID escolhido: "))
                if id_livro > biblioteca.len_livros() or id_livro < 0 or id_livro == '':
                    print('ID inválido! Tente novamente\n')
                elif biblioteca.verificarId(id_livro) == "Emprestado":
                    os.system('cls')
                    print(
                        'Não foi possivel concluir o pedido. O livro ja esta emprestado a outra pessoa.')
                else:
                    data = input(
                        "Digite aqui a data de empréstimo em dd/mm/yyyy: ")
                    biblioteca.realizar_emprestimo(id_livro, data, usuario.id)
            elif escolha == '2':
                os.system('cls')
                print("Escolha um livro para devolver:")
                for u in usuario.livros:
                    print(
                        f'Id: {u.id} - Titulo: {u.titulo} - Estado: {u.estado}')
                id_escolha = int(input('Digite aqui o ID para devolver: '))
                data_devolucao = input(
                    "Digite aqui a data de devolução em dd/mm/yyyy: ")

                biblioteca.realizar_devolucao(
                    id_escolha, data_devolucao, usuario.id)

            elif escolha == '3':
                escolha_busca = self.menuBuscas()
                if escolha_busca == '1':
                    escolha_busca_id = int(input('Digite o ID do livro: '))
                    biblioteca.buscar_por_id(escolha_busca_id)
                    print(biblioteca.verificarId(escolha_busca_id))
                    if biblioteca.verificarId(escolha_busca_id) == "Disponivel":
                        print("""Livro disponível para empréstimo!
                        Se desejar pegar o livro, digite 1
                        Se desejar voltar ao menu de buscas, digite 2,
                        Se deseja voltar ao menu de usuario, digite 3,
                        Se deseja sair, digite 9""")
                        escolha_pegar_livro = input(
                            "Digite aqui sua escolha: ")
                        if escolha_pegar_livro == '1':
                            data = input(
                                "Digite aqui a data de empréstimo em dd/mm/yyyy: ")
                            biblioteca.realizar_emprestimo(
                                escolha_busca_id, data, usuario.id)
                        elif escolha_pegar_livro == '2':
                            continue
                        elif escolha_pegar_livro == '9':
                            return print("Obrigado pela preferência, volte sempre!")

                elif escolha_busca == '2':
                    os.system('cls')
                    escolha_busca_titulo = input('Digite o Título do livro: ')
                    biblioteca.buscar_por_titulo(escolha_busca_titulo)
                    print("""Se desejar pegar algum livro, digite 1
                        Se desejar voltar ao menu digite 2
                        Se deseja sair, digite 9""")
                    escolha_pegar_livro = input("Digite aqui sua escolha: ")
                    if escolha_pegar_livro == '1':
                        escolha_busca_id = int(input('Digite o ID do livro: '))
                        data = input(
                            "Digite aqui a data de empréstimo em dd/mm/yyyy: ")
                        biblioteca.realizar_emprestimo(
                            escolha_busca_id, data, usuario.id)
                    elif escolha_pegar_livro == '2':
                        continue
                    elif escolha_pegar_livro == '9':
                        return print("Obrigado pela preferência, volte sempre!")

                elif escolha_busca == '3':
                    os.system('cls')
                    escolha_busca_autor = input('Digite o Autor do livro: ')
                    biblioteca.buscar_por_autor(escolha_busca_autor)
                    print(" ")
                    print("""Se desejar pegar algum livro, digite 1
                    Se desejar voltar ao menu digite 2
                    Se deseja sair, digite 9""")
                    escolha_pegar_livro = input("Digite aqui sua escolha: ")
                    if escolha_pegar_livro == '1':
                        escolha_busca_id = int(input('Digite o ID do livro: '))
                        data = input(
                            "Digite aqui a data de empréstimo em dd/mm/yyyy: ")
                        biblioteca.realizar_emprestimo(
                            escolha_busca_id, data, usuario.id)
                    elif escolha_pegar_livro == '2':
                        continue
                    elif escolha_pegar_livro == '9':
                        return print("Obrigado pela preferência, volte sempre!")

                print("")

            elif escolha == '4':

                input('')
            elif escolha == '5':
                os.system('cls')
                biblioteca.mostrar_livros()

    def funcoesBibliotecario(self):
        print("opa")

    def menuBuscas(self):
        ...


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
            escolha_menu = input('Digite aqui o valor desejado: ')
            if escolha_menu == '1':
                os.system('cls')
                print("Escolha das opções abaixo, o livro que quer pegar")
                biblioteca.mostrar_livros()
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
            id_livro = input("Digite aqui o ID do livro: ")
            while id_livro != "v" and not id_livro.isnumeric():
                id_livro = input('Digite um valor válido: ')
            if id_livro == "v":
                os.system('cls')
                return
            else:
                print(id_livro)
                id_livro = int(id_livro)
        else:
            print(id_parametro)
            id_livro = int(id_parametro)
        if id_livro > biblioteca.len_livros() or id_livro < 0 or id_livro == '':
            print('ID inválido! Tente novamente\n')
        elif biblioteca.verificarId(id_livro) == "Emprestado":
            os.system('cls')
            print('Não foi possivel concluir o pedido. O livro ja esta emprestado.')
        else:
            data = input("Digite aqui a data de empréstimo em dd/mm/yyyy:")
            biblioteca.realizar_emprestimo(id_livro, data, self.usuario.id)

    def devolverLivro(self):
        os.system('cls')
        print("Escolha um livro para devolver:")
        for u in self.usuario.livros:
            print(
                f'Id: {u.id} - Titulo: {u.titulo} - Estado: {u.estado}')
            id_escolha = int(input('Digite aqui o ID para devolver: '))
            data_devolucao = input(
                "Digite aqui a data de devolução em dd/mm/yyyy: ")

            biblioteca.realizar_devolucao(
                id_escolha, data_devolucao, self.usuario.id)

    def menuConsultarLivro(self):
        os.system('cls')
        print("Consulta de Livros")
        print("")
        print("""1- Buscar livro por ID
2- Buscar livro por Titulo
3- Buscar livro por Autor
4- Buscar livro por Gênero
5- Ver todos os livros""")
        escolha_busca = input("Digite aqui sua escolha: ")

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

            ver_livro = input(
                "Deseja ver os livros?\n1 - Sim\n2 - Não\n\nDigite aqui sua escolha: ")
            if ver_livro == '1':
                print("")
                self.pegarLivroBusca(mostrar_livros=True)
            elif ver_livro == '2':
                self.menu()
            else:
                print("Valor inválido, tente novamente!\n")

    def buscarPorId(self):
        os.system('cls')
        escolha_busca_id = int(input('Digite o ID do livro: '))
        print("")
        biblioteca.buscar_por_id(escolha_busca_id)
        if biblioteca.verificarId(escolha_busca_id) == "Disponivel":
            print("")
            print("O livro está Disponível, deseja pegar emprestado?\n1- Sim\n2- Não\n\n")

            escolha = input("Digite aqui a sua escolha: ")
            print(" ")
            if escolha == '1':
                self.pegarLivroBusca(id_livro=escolha_busca_id)
            elif escolha == '2':
                os.system('cls')
                self.pegarLivroBusca()
            else:
                print("Valor inválido, tente novamente!\n")
        else:
            print("O livro não está disponível para entrega")
            print("")
            self.pegarLivroBusca()
    
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
            escolha_pegar_livro = input("Digite aqui sua escolha: ")
            if escolha_pegar_livro == '1':
                print("""Digite o ID do livro.
Se não souber o id do livro, digite 'm' para mostrar os livros.
Se deseja voltar ao menu, digite 'v'""")
                input_id = input("Digite aqui: ")
                if input_id == 'm':
                    biblioteca.mostrar_livros()
                    print(" ")
                    self.pegarLivro()
                elif input_id == 'v':
                    return
                else:
                    self.pegarLivro(id_parametro=input_id)
            elif escolha_pegar_livro == '2':
                self.menuConsultarLivro()
            elif escolha_pegar_livro == '9':
                return


sistema = Sistema()
sistema.run()
