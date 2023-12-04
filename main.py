import os
class Livro:
    def __init__(self, id, titulo, autor, tag):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.tag = tag
        self.estado = "Disponivel"
        self.emprestado_a = None
    def __str__(self):
        return f'ID {self.id}: {self.titulo} - {self.autor} - {self.tag} - {self.estado}'

class Usuario:
    def __init__(self, nome,id):
        self.nome = nome
        self.id = id
        self.livros = []
        self.historico = []

class Emprestimo:
    def __init__(self, livro, usuario, data_emprestimo):
        self.livro = livro
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None

class Biblioteca:
    def __init__(self):
       self.usuarios = []
       self.emprestimos = []
       self.livros = [
            Livro(0, "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia"),
            Livro(1, "Harry Potter", "J.K. Rowling", "Fantasia"),
            Livro(2, "Orgulho e Preconceito", "Jane Austen", "Romance"),
            Livro(3, "1984", "George Orwell", "Ficção Científica"),
            Livro(4, "Dom Quixote", "Miguel de Cervantes", "Romance"),
            Livro(5, "Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico"),
            Livro(6, "Crime e Castigo", "Fyodor Dostoevsky", "Ficção Psicológica"),
            Livro(7, "O Grande Gatsby", "F. Scott Fitzgerald", "Romance"),
            Livro(8, "A Revolução dos Bichos", "George Orwell", "Alegoria"),
            Livro(9, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fantasia"),
            Livro(10, "O Homem de Giz", "C. J. Tudor", "Drama"),
            Livro(11, "Harry Potter e A pedra filosofal", "J.K. Rowling", "Fantasia")
            
            ]


    def cadastrar_livro(self, titulo, autor, tag):
        novo_id = len(self.livros) + 1
        novo_livro = Livro(novo_id, titulo, autor, tag)
        self.livros.append(novo_livro)
        return novo_livro

    def cadastrar_usuario(self, nome):
        novo_usuario = Usuario(nome, len(self.usuarios))
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def realizar_emprestimo(self, id_livro, data_emprestimo, id_usuario):
       
            
        if self.livros[id_livro].estado == "Disponivel":
            self.livros[id_livro].estado = "Emprestado"
            novo_emprestimo = Emprestimo(self.livros[id_livro], self.usuarios[id_usuario], data_emprestimo)
            self.emprestimos.append(novo_emprestimo)
            print(f'Users: {self.usuarios[id_usuario]}')
            self.usuarios[id_usuario].livros.append(self.livros[id_livro])
            self.usuarios[id_usuario].historico.append(self.livros[id_livro])
            self.livros[id_livro].emprestado_a = self.usuarios[id_usuario]
            
            os.system('cls')
            print(f'Livro {self.livros[id_livro].id} - {self.livros[id_livro].titulo} emprestado')

        else:
            return "Livro não disponível para empréstimo"
        
    def verificarId(self, id_livro):
        return self.livros[id_livro].estado
    
    def realizar_devolucao(self, id_livro, data_devolucao, id_usuario):
        if self.livros[id_livro].estado == "Emprestado":
            self.livros[id_livro].estado = "Disponível"
            self.livros[id_livro].emprestado_a = None
            for emprestimo in self.emprestimos:
                if emprestimo.livro == self.livros[id_livro] and emprestimo.data_devolucao is None:
                    self.usuarios[id_usuario].livros.remove(self.livros[id_livro])
                    print(f'Livro {self.livros[id_livro].id} - {self.livros[id_livro].titulo} devolvido')
                    emprestimo.data_devolucao = data_devolucao
                    return emprestimo
        else:
            return "Livro não foi emprestado"

    def buscar_por_id(self, livro_id):
        busca = self._busca_binaria_livro(self.livros, livro_id)
        if busca:
            return print(f"Livro encontrado: {busca.titulo} (ID: {busca.id})")
        else:
            return print("Livro não encontrado")

    def _busca_binaria_livro(self, livros, livro_id):
        inicio = 0
        fim = len(livros) - 1

        while inicio <= fim:
            meio = (inicio + fim) // 2
            livro_atual = livros[meio]

            if livro_atual.id == livro_id:
                return livro_atual
            elif livro_atual.id < livro_id:
                inicio = meio + 1
            else:
                fim = meio - 1

        return None


    def buscar_por_titulo(self, titulo):
        titulos = [livro for livro in self.livros if titulo.lower() in livro.titulo.lower()]
        if titulos:
            print("Livros encontrados:")
            for t in titulos:
                print(t.__str__())
        else: print("Titulo nao encontrado!")


    def buscar_por_autor(self, autor):
        titulos = [livro for livro in self.livros if autor.lower() in livro.autor.lower()]
        if titulos:
            print("Livros encontrados:")
            for t in titulos:
                print(t.__str__())
                
        else: print("Autores nao encontrado!")

    def relatorio_emprestimos(self):
        relatorio = []
        for emprestimo in self.emprestimos:
            livro_info = f"{emprestimo.livro.titulo} (ID: {emprestimo.livro.id})"
            usuario_info = f"{emprestimo.usuario.nome} (ID: {emprestimo.usuario.id})"
            emprestimo_info = f"Empréstimo: {emprestimo.data_emprestimo}, Devolução: {emprestimo.data_devolucao}"
            relatorio.append(f"{livro_info} emprestado para {usuario_info}. {emprestimo_info}")
        return relatorio

    def mostrar_livros(self):
            print(" ")
            print('ID -TITULO - AUTOR - TAG - ESTADO')
            print(" ")             
            for l in self.livros:
                print(l.__str__())
    
    def len_livros(self):
        return len(self.livros)

# # Exemplo de Uso
biblioteca = Biblioteca()
# livro1 = biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
# livro2 = biblioteca.cadastrar_livro("Harry Potter", "J.K. Rowling", "Fantasia")
# livro3 = biblioteca.cadastrar_livro("Orgulho e Preconceito", "Jane Austen", "Romance")
# usuario1 = biblioteca.cadastrar_usuario("João")
# biblioteca.realizar_emprestimo(livro1, usuario1, "2023-01-01")
# biblioteca.realizar_emprestimo(livro2, usuario1, "2023-02-01")
# livro_encontrado = biblioteca.buscar_por_id(2)

# if livro_encontrado:
#     print(f"Livro encontrado: {livro_encontrado.titulo} (ID: {livro_encontrado.id})")
# else:
#     print("Livro não encontrado")

# livros = biblioteca.mostrar_livros()
# print('Livros na biblioteca:')
# print(" ")
# print('ID -TITULO - AUTOR - TAG - ESTADO')
# print(" ")

# for l in livros:
#     print(f'{l.id}: {l.titulo} - {l.autor} - {l.tag} - {l.estado}')