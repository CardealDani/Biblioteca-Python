import customtkinter as ctk
app = ctk.CTk()


class App:

    def __init__(self):
        app.title('Cadastro de Clientes')
        width = int(app.winfo_screenwidth())
        height = int(app.winfo_screenheight())
        x = (5 * width) // 10
        y = (5 * height) // 10
        comeco_width = str(int(app.winfo_screenwidth()) // 4)
        comeco_height = str(int(app.winfo_screenheight()) // 4)
        app.geometry(f'{x}x{y}+{comeco_width}+{comeco_height}')
        app.resizable(False, False)


    def adicionar(self):
        """Mostra a Descrição"""

        print(f'Nome do restaurante: {self.resturante_nome}\nTipo de Cozinha: {self.tipo_cozinha}')

    def restaurante_aberto(self):
        """Mostra se ele está aberto"""
        print(f'{self.resturante_nome} está aberto!')


restaurantes = {'Fogo Campeiro': 'Rodízio de Carne',
                'Luciano': 'Churrascaria',
                'Restaurante Universitário': 'Almoço e Janta'}



if __name__ == "__main__":
    App()
    app.mainloop()