import gspread
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
CODE = "1X9PTWhz0ceadTCQzKDzNuIYiQQLuKJI_Rwp5tJPQ5Ss"
gc = gspread.service_account(filename='key.json')
sheet = gc.open_by_key(CODE)
caminho = 'Financeiro'
excel = sheet.worksheet(caminho)



class App:
    def __init__(self, dados):
        self.dados = dados
        return None
    
    def consultarDados(self):
        for d in range(len(self.dados)):
            print(f'Cliente {d}')
            for f in range(len(self.dados[d])):
                print(self.dados[d][f])
            print('')
    
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



    