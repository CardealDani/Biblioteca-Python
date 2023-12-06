import gspread
import locale
locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
from datetime import datetime


CODE = "1X9PTWhz0ceadTCQzKDzNuIYiQQLuKJI_Rwp5tJPQ5Ss"
gc = gspread.service_account(filename='Custom-Tkinter-Python-main\projeto-main\key.json')
sheet = gc.open_by_key(CODE)
caminho = 'Financeiro'
excel = sheet.worksheet(caminho)

def inserirDados(dat, cli,pro,val,ent,pag,par,ob):
    data = dat
    cliente = str(cli.title())
    processo = str(pro.title())
    valor = float(val)
    entrada = float(ent)
    pagamento = str(pag)
    parcela = str(par)
    valor = locale.currency(valor, symbol=True, grouping=True, international=False) 
    entrada = locale.currency(entrada, symbol=True, grouping=True, international=False)
    obs = str(ob)
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
    except:
        print('Deu erro')
        
inserirDados('23/04/2023','teste','civel','100','10','dinheiro','0','nada')

