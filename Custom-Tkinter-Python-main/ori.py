from googlesheets import dados
while True:    
    
    class Cliente:
        def __init__(self, data, cliente, processo, valor, entrada, pagamento, parcela, obs='-'):
            self.data = data
            self.cliente = cliente
            self.processo = processo
            self.valor = valor
            self.entrada = entrada
            self.pagamento = pagamento
            self.parcela = parcela
            self.obs = obs
            # print(self.data,self.cliente,self.processo,self.valor,self.entrada,self.pagamento,self.parcela,self.obs)


        def consultarCliente(self):
            self.dados_cliente = [{
            'Data': self.data,
            'Cliente': self.cliente,
            'Processo': self.processo,
            'Valor': self.valor,
            'Entrada': self.entrada,
            'Pagamento': self.pagamento,
            'Parcela': self.parcela,
            'Obs': self.obs
            }
            ]
            return self.dados_cliente[0]

        def atualizarDados(self):
            print(f'Dados do Cliente:')
            print('')
            for k,i in self.dados_cliente[0].items():
                print(f'{k}: {i}')
            
            self.atualizar = input('O que você quer atualizar? (Data,Cliente,Processo,Valor,Entrada,Pagamento,Parcela,Obs)\n').title().strip()
            self.dado_atualizado = str(input('Digite o novo valor: ')).title().strip()
            self.dados_cliente[0][self.atualizar]=self.dado_atualizado
            
            print(f'Dados do Cliente atualizados:')
            for k,i in self.dados_cliente[0].items():
                print(f'{k}: {i}')
            return None

    teste = [Cliente(*elementos) for elementos in dados]

    # for t in range(len(teste)):
    #     print(teste[t].consultarCliente())

    teste[0].consultarCliente()
    teste[0].atualizarDados()






        # self.dados_cliente = {
        #     'Data': '',
        #     'Cliente': '',
        #     'Processo': '',
        #     'Valor': '',
        #     'Entrada': '',
        #     'Pagamento': '',
        #     'Parcela': '',
        #     'Obs': ''
        # }
        # for d in range(len(self.dados)):
        #     for f in range(len(self.dados[d])):
        #         self.dados_cliente['Data'] = self.dados[d][0]
        #         self.dados_cliente['Cliente']=self.dados[d][1]
        #         self.dados_cliente['Processo']=self.dados[d][2]
        #         self.dados_cliente['Valor']=self.dados[d][3]
        #         self.dados_cliente['Entrada']=self.dados[d][4]
        #         self.dados_cliente['Pagamento']=self.dados[d][5]
        #         self.dados_cliente['Parcela']=self.dados[d][6]
        #         self.dados_cliente['Obs']=self.dados[d][7]
        #     print(self.dados_cliente)        
        
    