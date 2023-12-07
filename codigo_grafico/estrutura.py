
class Livro:
    def __init__(self, id, titulo, autor, tag):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.tag = tag
        self.estado = "Disponível"
        self.emprestado_a = None
        self.data_emprestimo = "Não foi emprestado"
        self.data_devolucao = "Não foi devolvido/emprestado"
    def __str__(self):
        return [self.id,self.titulo,self.autor,self.tag,self.estado]
    def retorno(self,emprestimo = False,historico = False):
        if emprestimo:
            return [self.id, self.titulo,self.autor,self.estado,self.data_emprestimo]
        elif historico:
            
            return [self.id, self.titulo,self.autor,self.estado,self.data_emprestimo,self.data_devolucao]
        else:
            return [self.id,self.titulo,self.autor,self.tag,self.estado]

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
        self.titulo = self.livro.titulo
        self.autor = self.livro.autor
        self.estado = self.livro.estado
        self.tag = self.livro.tag
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
    def __str__(self):
        return [self.id,self.titulo,self.autor, self.estado,self.data_emprestimo]

class Biblioteca:
    def __init__(self):
       self.usuarios = []
       self.emprestimos = []
       self.livros = [
            Livro(1, "Harry Potter", "J.K. Rowling", "Fantasia"),
            Livro(2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Fantasia"),
            Livro(3, "1984", "George Orwell", "Ficção Científica"),
            Livro(4, "Dom Quixote", "Miguel de Cervantes", "Romance"),
            Livro(5, "Crime e Castigo", "Fyodor Dostoevsky", "Ficção Psicológica"),
            Livro(6, "Cem Anos de Solidão", "Gabriel García Márquez", "Realismo Mágico"),
            Livro(7, "A Revolução dos Bichos", "George Orwell", "Alegoria"),
            Livro(8, "Orgulho e Preconceito", "Jane Austen", "Romance"),
            Livro(9, "O Homem de Giz", "C. J. Tudor", "Drama"),
            Livro(10, "A Menina que Roubava Livros", "Markus Zusak", "Romance Histórico"),
            Livro(11, "As Crônicas de Nárnia", "C.S. Lewis", "Fantasia"),
            Livro(12, "Harry Potter e A pedra filosofal", "J.K. Rowling", "Fantasia"),
            Livro(13, "Matar um Rouxinol", "Harper Lee", "Drama"),
            Livro(14, "A Moreninha", "Joaquim Manuel de Macedo", "Romance"),
            Livro(15, "O Iluminado", "Stephen King", "Horror"),
            Livro(16, "Memórias Póstumas de Brás Cubas", "Machado de Assis", "Sátira"),
            Livro(17, "A Guerra dos Tronos", "George R.R. Martin", "Fantasia Épica"),
            Livro(18, "O Hobbit", "J.R.R. Tolkien", "Fantasia"),
            Livro(19, "O Alquimista", "Paulo Coelho", "Ficção Inspiracional"),
            Livro(21, "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia"),
            Livro(22, "A Insustentável Leveza do Ser", "Milan Kundera", "Filosofia"),
            Livro(23, "O Retrato de Dorian Gray", "Oscar Wilde", "Gótico"),
            Livro(24, "O Grande Gatsby", "F. Scott Fitzgerald", "Romance"),
            Livro(25, "O Código Da Vinci", "Dan Brown", "Suspense"),
            Livro(26, "O Senhor das Moscas", "William Golding", "Alegoria"),
            Livro(27, "O Nome do Vento", "Patrick Rothfuss", "Fantasia"),
            Livro(28, "A Metamorfose", "Franz Kafka", "Absurdo"),
            Livro(29, "A Sangue Frio", "Truman Capote", "Não Ficção"),
            Livro(30, "O Silmarillion", "J.R.R. Tolkien", "Fantasia"),
            Livro(20, "A Arte da Guerra", "Sun Tzu", "Filosofia Militar"),
            Livro(31, "O Labirinto dos Espíritos", "Carlos Ruiz Zafón", "Mistério"),
            Livro(32, "O Apanhador no Campo de Centeio", "J.D. Salinger", "Ficção Adolescente"),
            Livro(33, "A Revolta de Atlas", "Ayn Rand", "Filosofia"),
            Livro(34, "A Estrada", "Cormac McCarthy", "Ficção Apocalíptica"),
            Livro(35, "O Senhor dos Anéis: As Duas Torres", "J.R.R. Tolkien", "Fantasia"),
            Livro(36, "Anna Karenina", "Liev Tolstói", "Romance"),
            Livro(37, "A Culpa é das Estrelas", "John Green", "Romance Adolescente"),
            Livro(38, "O Principezinho", "Antoine de Saint-Exupéry", "Fábula"),
            Livro(39, "Sapiens: Uma Breve História da Humanidade", "Yuval Noah Harari", "Não Ficção"),
            Livro(40, "O Sol é para Todos", "Harper Lee", "Drama"),
            Livro(41, "Os Miseráveis", "Victor Hugo", "Romance Histórico"),
            Livro(42, "A Princesa Prometida", "William Goldman", "Aventura"),
            Livro(43, "O Enigma do Quarto 622", "Joël Dicker", "Mistério"),
            Livro(44, "O Pequeno Livro das Grandes Virtudes", "William J. Bennett", "Filosofia"),
            Livro(45, "A Livraria 24 Horas do Mr. Penumbra", "Robin Sloan", "Mistério"),
            Livro(46, "O Cão dos Baskervilles", "Arthur Conan Doyle", "Mistério"),
            Livro(47, "O Jardim Secreto", "Frances Hodgson Burnett", "Literatura Infantil"),
            Livro(48, "A Cor Púrpura", "Alice Walker", "Ficção Feminina"),
            Livro(49, "A Ilha do Tesouro", "Robert Louis Stevenson", "Aventura"),
            Livro(50, "O Médico", "Noah Gordon", "Histórico"),
            Livro(51, "O Código éthico do Guerreiro", "Miyamoto Musashi", "Filosofia"),
            Livro(52, "A Conspiração Contra a América", "Philip Roth", "Ficção Alternativa"),
            Livro(53, "O Conto da Aia", "Margaret Atwood", "Ficção Especulativa"),
            Livro(54, "O Homem Invisível", "H.G. Wells", "Ficção Científica"),
            Livro(55, "A Máquina do Tempo", "H.G. Wells", "Ficção Científica"),
            Livro(56, "O Jogo do Anjo", "Carlos Ruiz Zafón", "Mistério"),
            Livro(57, "O Mundo Assombrado pelos Demônios", "Carl Sagan", "Divulgação Científica"),
            Livro(58, "Os Homens que Não Amavam as Mulheres", "Stieg Larsson", "Suspense"),
            Livro(59, "O Nome da Rosa", "Umberto Eco", "Mistério"),
            Livro(60, "O Estranho Caso do Dr. Jekyll e Mr. Hyde", "Robert Louis Stevenson", "Gótico"),
            Livro(61, "A Cabana", "William P. Young", "Ficção Inspiracional"),
            Livro(62, "O Médico e o Monstro", "Robert Louis Stevenson", "Gótico"),
            Livro(63, "O Corcunda de Notre-Dame", "Victor Hugo", "Romance Gótico"),
            Livro(64, "O Fim da Eternidade", "Isaac Asimov", "Ficção Científica"),
            Livro(65, "O Jogo da Amarelinha", "Julio Cortázar", "Ficção Experimental"),
            Livro(66, "A Peste", "Albert Camus", "Existencialismo"),
            Livro(67, "O Velho e o Mar", "Ernest Hemingway", "Aventura"),
            Livro(68, "Cemitério Maldito", "Stephen King", "Horror"),
            Livro(69, "O Médico doente", "Frederico Lourenço", "Ficção Filosófica"),
            Livro(70, "O Projeto Rosie", "Graeme Simsion", "Romance"),
            Livro(71, "O Despertar da Força", "Alan Dean Foster", "Ficção Científica"),
            Livro(72, "A Arte de Amar", "Erich Fromm", "Psicologia"),
            Livro(73, "O Lobo do Mar", "Jack London", "Aventura"),
            Livro(74, "O Último Homem", "Mary Shelley", "Ficção Apocalíptica"),
            Livro(75, "O Jardim das Delícias", "Ariano Suassuna", "Teatro"),
            Livro(76, "O Prisioneiro de Azkaban", "J.K. Rowling", "Fantasia"),
            Livro(77, "A Cidade e as Serras", "Eça de Queirós", "Realismo"),
            Livro(78, "O Homem Duplicado", "José Saramago", "Ficção Filosófica"),
            Livro(79, "A Trilogia da Fundação", "Isaac Asimov", "Ficção Científica"),
            Livro(80, "O Ladrão de Raios", "Rick Riordan", "Fantasia"),
            Livro(81, "A Casa dos Espíritos", "Isabel Allende", "Realismo Mágico"),
            Livro(82, "O Fantasma da Ópera", "Gaston Leroux", "Romance Gótico"),
            Livro(83, "A Vida como Ela É...", "Nelson Rodrigues", "Contos"),
            Livro(84, "O Último dos Moicanos", "James Fenimore Cooper", "Aventura"),
            Livro(85, "O Livro de Ouro", "Giovanni Papini", "Filosofia"),
            Livro(86, "O Coração das Trevas", "Joseph Conrad", "Ficção Psicológica"),
            Livro(87, "A Guerra do Fim do Mundo", "Mario Vargas Llosa", "Histórico"),
            Livro(88, "O Senhor dos Anéis: O Retorno do Rei", "J.R.R. Tolkien", "Fantasia"),
            Livro(89, "O Silêncio dos Inocentes", "Thomas Harris", "Suspense"),
            Livro(90, "O Morro dos Ventos Uivantes", "Emily Brontë", "Romance Gótico"),
            Livro(91, "A Elegância do Ouriço", "Muriel Barbery", "Filosofia"),
            Livro(92, "O Código Bro", "Herbert Schildt", "Computação"),
            Livro(93, "O Cemitério de Praga", "Umberto Eco", "Histórico"),
            Livro(94, "A Sombra do Vento", "Carlos Ruiz Zafón", "Mistério"),
            Livro(95, "O Lado Bom da Vida", "Matthew Quick", "Romance"),
            Livro(96, "O Hobbit: A Desolação de Smaug", "J.R.R. Tolkien", "Fantasia"),
            Livro(97, "O Poderoso Chefão", "Mario Puzo", "Crime"),
            Livro(98, "O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia"),
            Livro(99, "O Homem que Calculava", "Malba Tahan", "Matemática"),
            Livro(100, "O Leão, a Feiticeira e o Guarda-Roupa", "C.S. Lewis", "Fantasia"),
            
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
        print(f"ID emprestimo {id_livro}")
        print(f"ID emprestimo lista = {self.livros[id_livro].id}")
        novo_emprestimo = Emprestimo(self.livros[id_livro].id,self.livros[id_livro], self.usuarios[id_usuario], data_emprestimo)
        self.livros[id_livro].data_emprestimo = data_emprestimo
        self.emprestimos.append(novo_emprestimo)
        self.usuarios[id_usuario].livros.append(self.livros[id_livro])
        self.usuarios[id_usuario].historico.append(self.livros[id_livro])
        self.livros[id_livro].emprestado_a = self.usuarios[id_usuario]
        self.livros[id_livro].estado = "Emprestado"
        print("Livro Emprestado")
    
    def verificarEstadoLivro(self, id_livro):
        print(self.livros[id_livro].estado)
        if self.livros[id_livro].estado == "Disponível":
            return True
        else: return False
    
    def realizar_devolucao(self, id_livro_parametro, data_devolucao, id_usuario):
            id_emprestimo = self.binary_search(self.emprestimos,id_livro_parametro)
            id_livro=self.binary_search(self.livros,id_livro_parametro)
            self.livros[id_livro[1]].estado = "Disponível"
            
            self.livros[id_livro[1]].emprestado_a = None
            self.emprestimos[id_emprestimo[1]].data_devolucao = data_devolucao 
            self.livros[id_livro[1]].data_devolucao = data_devolucao           
            id_livro_usuario = self.binary_search(self.usuarios[id_usuario].livros, id_livro_parametro)
            
            self.usuarios[id_usuario].livros.pop(id_livro_usuario[1])
           
            
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

    def mostrar_livros(self,emprestimo = False, historico = False, usuario_id = None):
        if emprestimo:
            livros_ordenados= self.merge_sort(self.usuarios[usuario_id].livros)
        elif historico:
            livros_ordenados = self.merge_sort(self.usuarios[usuario_id].historico) 
            print(livros_ordenados)
        else: 
            livros_ordenados = self.merge_sort(self.livros) 
        return livros_ordenados
                
    
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
