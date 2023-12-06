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
    def __init__(self, id_livro,livro, usuario, data_emprestimo):
        self.id = id_livro
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
            Livro(9, "Orgulho e Preconceito", "Jane Austen", "Romance"),
            Livro(3, "1984", "George Orwell", "Ficção Científica"),
            Livro(4, "Dom Quixote", "Miguel de Cervantes", "Romance"),
            Livro(53, "Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico"),
            Livro(6, "Crime e Castigo", "Fyodor Dostoevsky", "Ficção Psicológica"),
            Livro(74, "O Grande Gatsby", "F. Scott Fitzgerald", "Romance"),
            Livro(85, "A Revolução dos Bichos", "George Orwell", "Alegoria"),
            Livro(2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fantasia"),
            Livro(10, "O Homem de Giz", "C. J. Tudor", "Drama"),
            Livro(13, "Harry Potter e A pedra filosofal", "J.K. Rowling", "Fantasia")
            ]

    def mostrar_por_id(self, livro_id):
        return self.livros[livro_id]

    def binary_search(self, livros, id_livro):
        '''
        Verifica se id_livro  estÃ¡ presente em livros (livros precisa estar ordenado)
        :param livros: lista ordenada de valores
        :param id_livro: valor a ser procurado na lista
        :return: True e o Ã­ndice da lista onde id_livro se encontra, False e -1, caso contrÃ¡rio
        '''
        livros = self.merge_sort(livros)
        low = 0
        high = len(livros) - 1

        # print(livros[0].i)
        
        # Enquanto o livros nÃ£o tiver sido percorrido por completo
        while low <= high:
            # encontra o meio do livros
            mid = (high + low) // 2
            # se o valor foi maior que o valor que estÃ¡ no meio do livros
            # ignora toda a parte anterior ao meio do livros            
            if livros[mid].id < id_livro:
                low = mid + 1
            # se o valor for menor, faz o contrÃ¡rio
            elif livros[mid].id > id_livro:
                high = mid - 1
            # caso contrÃ¡rio, o elemento estÃ¡ exatamente no meio
            else:
                return True, mid
        # elemento nÃ£o estÃ¡ no livros
        return False
    
    def cadastrar_livro(self, id_livro, titulo, autor, tag):
        novo_id = id_livro
        novo_livro = Livro(novo_id, titulo, autor, tag)
        self.livros.append(novo_livro)
        return True
    
    def editarLivro(self, id_livro_atual, novo_id=None, novo_titulo=None, novo_autor=None, novo_genero=None):
        if novo_id != None:
            self.livros[id_livro_atual].id = novo_id
            novo_id = self.binary_search(self.livros,novo_id)
            return novo_id
        elif novo_titulo != None:
            self.livros[id_livro_atual].titulo = novo_titulo
        elif novo_autor != None:
            self.livros[id_livro_atual].autor = novo_autor
        elif novo_genero != None:
            self.livros[id_livro_atual].tag = novo_genero

    def excluirLivro(self, id_livro):
        self.livros.pop(id_livro)
        
    def emptyId(self, id_livro, emprestimo = False):
        if emprestimo:
            busca = self.binary_search(self.emprestimos, int(id_livro))
        else: busca = self.binary_search(self.livros, int(id_livro))
        return busca

    def cadastrar_usuario(self, nome):
        novo_usuario = Usuario(nome, len(self.usuarios))
        self.usuarios.append(novo_usuario)
        return novo_usuario

    def realizar_emprestimo(self, id_livro, data_emprestimo, id_usuario):
       

        self.livros[id_livro].estado = "Emprestado"
        novo_emprestimo = Emprestimo(id_livro,self.livros[id_livro], self.usuarios[id_usuario], data_emprestimo)
        self.emprestimos.append(novo_emprestimo)
        self.usuarios[id_usuario].livros.append(self.livros[id_livro])
        self.usuarios[id_usuario].historico.append(self.livros[id_livro])
        self.livros[id_livro].emprestado_a = self.usuarios[id_usuario]
        os.system('cls')
        print(f'Livro {self.livros[id_livro]} - {self.livros[id_livro].titulo} - foi emprestado para você!\nBoas leituras :D')

    def verificarEstadoLivro(self, id_livro):
        # novo_id = self.binary_search(self.livros, id_livro)
        return self.livros[id_livro].estado
        
    
    def realizar_devolucao(self, id_livro,id_emprestimo, data_devolucao, id_usuario):
            self.livros[id_livro].estado = "Disponível"
            self.livros[id_livro].emprestado_a = None
            self.emprestimos[id_emprestimo].data_devolucao = data_devolucao
            self.usuarios[id_usuario].livros.remove(self.livros[id_livro])
            return f"Livro {self.livros[id_livro].id} - {self.livros[id_livro].titulo} devolvido"
 
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

    def buscar_por_genero(self, genero):
        titulos = [livro for livro in self.livros if genero.lower() in livro.tag.lower()]
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
            livros_ordenados= self.merge_sort(self.livros) 
            for l in livros_ordenados:
                print(l.__str__())
                
    
    def merge_sort(self, arranjo):
        if len(arranjo) > 1:
            mid = len(arranjo) // 2
            left = arranjo[0:mid]
            right = arranjo[mid:]

            # Chamada recursiva em cada metade
            self.merge_sort(left)
            self.merge_sort(right)

            # a partir daqui vamos fazer o "merge" das sublistas
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i].id <= right[j].id:
                    arranjo[k] = left[i]
                    i += 1
                else:
                    arranjo[k] = right[j]
                    j += 1
                k += 1

            # valores restantes
            while i < len(left):
                arranjo[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arranjo[k] = right[j]
                j += 1
                k += 1
            
            return arranjo
        else: return arranjo
    
    def len_livros(self):
        return len(self.livros)

biblioteca = Biblioteca()
