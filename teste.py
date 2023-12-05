import os
from main import *


class Sistema:
    def __init__(self):
        self.estado = True

    def run(self):
        while self.estado == True:
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
                    return self.funcoesUsuario(nome)
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
                os.system('cls')
                for u in usuario.historico:
                    print(
                        f'Id: {u.id} - Titulo: {u.titulo} - Estado: {u.estado}')
                input('')
            elif escolha == '5':
                os.system('cls')
                biblioteca.mostrar_livros()

    def funcoesBibliotecario(self):
        print("opa")

    def menuBuscas(self):
        os.system('cls')
        print("Consulta de Livros")
        print("")
        print("""1 - Buscar livro por ID
2- Buscar livro por Titulo
3- Buscar livro por Autor
4- Buscar livro por Gênero
5- Ver todos os livros""")
        escolha_busca = input("Digite aqui sua escolha: ")
        return escolha_busca


sistema = Sistema()
sistema.run()
