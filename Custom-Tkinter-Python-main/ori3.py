import gspread
import locale
from tkinter import *
from tkinter import ttk
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
CODE = "1X9PTWhz0ceadTCQzKDzNuIYiQQLuKJI_Rwp5tJPQ5Ss"
gc = gspread.service_account(filename='key.json')
sheet = gc.open_by_key(CODE)
caminho = 'Financeiro'
excel = sheet.worksheet(caminho)


janela = Tk()


class App:
    def __init__(self, dados):
        self.dados = dados
        janela.title('Cadastro de Clientes')
        width = int(janela.winfo_screenwidth())
        height = int(janela.winfo_screenheight())
        x = (5 * width) // 10
        y = (5 * height) // 10
        comeco_width = str(int(janela.winfo_screenwidth()) // 4)
        comeco_height = str(int(janela.winfo_screenheight()) // 4)
        janela.geometry(f'{x}x{y}+{comeco_width}+{comeco_height}')
        janela.resizable(False, False)
        janela.iconbitmap('ico.ico')
        return None
    
    def consultarDados(self):
        tv = ttk.Treeview(janela,columns=("data", "cliente", "processo", "valor", "entrada", "pagamento", "parcela", "obs"), show='headings')
        tv.column("data",width=100)
        tv.column("cliente",width=100)
        tv.column("processo",width=100)
        tv.column("valor",width=100)
        tv.column("entrada",width=100)
        tv.column("pagamento",width=100)
        tv.column("parcela",width=100)
        tv.column("obs",width=100)

        tv.heading("data",text="DATA")
        tv.heading("cliente",text="CLIENTE")
        tv.heading("processo",text="PROCESSO")
        tv.heading("valor",text="VALOR")
        tv.heading("entrada",text="ENTRADA")
        tv.heading("pagamento",text="PAGAMENTO")
        tv.heading("parcela",text="PARCELA")
        tv.heading("obs",text="OBS")
        tv.pack()
        
            
        
        for (data,cli,pro,val,ent,pag,par,ob) in self.dados:
            tv.insert("","end",values=(data,cli,pro,val,ent,pag,par,ob))
    
    def cadastrarCliente(self,dat, cli,pro,val,ent,pag,par,ob):
        data = dat
        cliente = str(cli.title())
        processo = str(pro.title())
        valor = float(val)
        entrada = float(ent)
        pagamento = str(pag)
        parcela = str(par)
        obs = str(ob)
        valor = locale.currency(valor, symbol=True, grouping=True, international=False) 
        entrada = locale.currency(entrada, symbol=True, grouping=True, international=False)
        if obs == 'n' or obs == '':
            obs = '-'
        if parcela == 'n' or parcela == '':
            parcela = '-'
    
        lista = [data, cliente, processo, valor, entrada, pagamento, parcela, obs]
        r = len(excel.col_values(1))+1
        print(r)
        if r % 2 == 0:
            excel.format(f"A{r}:Z{r}", {
                "backgroundColor": {
                    "red": 239/255,
                    "green": 239/255,
                    "blue": 239/255
                }})
        print('colocando os dados')
        try:
            excel.update(f'A{r}:Z{r}', [lista])
            print('Dados enviados')
        except NameError as ex:
            print(ex)
        

programa = True
while programa == True:
    tam = len(excel.col_values(1))+1
    dados = excel.get(f'A2:Z{tam}')
    app = App(dados)
    escolha = input('1 - Cadastrar Cliente\n2 - Ver Clientes\nDigite aqui a opção:')
    if escolha == "1":
        data = input('Digite a data (dd/mm/yyyy):').strip()
        cliente = input('Digite o nome do Cliente:').title().strip()
        processo = input('Digite o tipo do Processo:').strip().title()
        valor = float(input('Digite o valor:'))
        entrada = float(input('Digite o valor de Entrada:'))
        pagamento = str(input('Digite o tipo de Pagamento:'))
        parcela = str(input('Digite a quantidade Parcelas:'))
        obs = str(input('Observação:'))
        app.cadastrarCliente(data,cliente,processo,valor,entrada,pagamento,parcela,obs)
        continue
    elif escolha == "2":
        app.consultarDados()
        continue
    elif escolha == "3":
        print('Programa encerrado')
        break
janela.mainloop()




    