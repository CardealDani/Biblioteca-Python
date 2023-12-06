import customtkinter as ctk

janela = ctk.CTk()

janela.title('Cadastro de Clientes')
janela.geometry("700x400+600+300")
janela.resizable(False, False)
janela.iconbitmap('ico.ico')

tabview = ctk.CTkTabview(janela,width=400,corner_radius=20,border_width=1,border_color="red",fg_color="teal",
                         segmented_button_fg_color="cyan",segmented_button_selected_color="#E03A61",
                         segmented_button_selected_hover_color="#E03A61",segmented_button_unselected_hover_color='#2b0536',segmented_button_unselected_color="#2b0536")
tabview.pack()
tabview.add("Nomes")
tabview.add("Idades")
tabview.add("Genero")
tabview.tab("Nomes").grid_columnconfigure(0,weight=1)

text = ctk.CTkLabel(tabview.tab("Nomes"),text="Daniel Cardeal\nElias Cardeal\nCíntia Cordeiro")
text.pack()

janela.mainloop()
