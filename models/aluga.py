from datetime import date, datetime, timedelta
from models.JogoAlugado import JogoAlugado

class Aluga:
    def __init__(self, data_inicio:str, data_fim:str, forma_pagamento:str, jogo_alugado:JogoAlugado):
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.forma_pagamento = forma_pagamento
        self.jogo_alugado =  jogo_alugado

    @property
    def data_inicio(self):
        return self.__data_inicio
        
    @property
    def data_fim(self):
        return self.__data_fim
    
    @property
    def forma_pagamento(self):
        return self.__forma_pagamento
        
    @property
    def jogo_alugado(self):
        return self.__jogo_alugado
        
    @data_inicio.setter
    def data_inicio(self, data: str):
            if isinstance(data, str):
                try:
                    data = datetime.strptime(data, "%d/%m/%Y").date()
                except ValueError:
                    raise ValueError("A data deve estar no formato DD/MM/AAAA.")
            if not isinstance(data, date):
                raise ValueError("Data inválida.")
            if data > date.today():
                raise ValueError("A data de início não pode ser maior que a data atual.")
            self.__data_inicio = data

    @data_fim.setter
    def data_fim(self, data: str):
            if isinstance(data, str):
                try:
                    data = datetime.strptime(data, "%d/%m/%Y").date()
                except ValueError:
                    raise ValueError("A data deve estar no formato DD/MM/AAAA.")
            if not isinstance(data, date):
                raise ValueError("Data inválida.")
            if data < self.data_inicio:
                raise ValueError("A data de fim não pode ser menor que a data de início.")
            self.__data_fim = data

    @forma_pagamento.setter
    def forma_pagamento(self, novaFpag: str):
        formas_validas = {"crédito", "débito", "pix", "boleto", "dinheiro"}
        novaFpag = str(novaFpag).strip().lower()
        if novaFpag not in formas_validas:
            raise ValueError("Forma de pagamento inválida.")
        self.__forma_pagamento = novaFpag

    @jogo_alugado.setter
    def jogo_alugado(self, jogo:JogoAlugado):
        if not isinstance(jogo, JogoAlugado):
            raise ValueError("O jogo alugado deve existir.")
        self.__jogo_alugado = jogo
        self.jogo_alugado.atualizar_estoque(-1)
    
    def exibir_dados(self):
        print(f"Data de início: {self.data_inicio}\nData de fim: {self.data_fim}\nForma de Pagamento: {self.forma_pagamento.capitalize()}\nJogo Alugado: {self.jogo_alugado}\n")

    def calcular_valor(self):
        periodo = (self.data_fim - self.data_inicio).days
        
        if periodo == 0:
            periodo = 1
            
        preco = self.jogo_alugado.obter_preco()
        return periodo * preco
    
    def devolver_jogo(self):
        self.jogo_alugado.atualizar_estoque(1)
        print(f"O jogo {self.jogo_alugado.nome} foi devolvido.")

        dias_atraso = self.verificar_atraso()
        valor_multa = self.calcular_multa()
        
        if dias_atraso > 0:
            print(f"O jogo foi entregue com {dias_atraso} dia(s) de atraso.")
            print(f"Valor da multa por atraso: R$ {valor_multa:.2f}")
            valor_aluguel = self.calcular_valor() + (self.jogo_alugado.obter_preco() * dias_atraso)
            total_geral = valor_aluguel + valor_multa
            print(f"Total a pagar (Aluguel(+dias atrasados) + Multa): R$ {total_geral:.2f}")
        else:
            print(f"Total a pagar: R$ {self.calcular_valor():.2f}")

    def renovar_aluguel(self, dias:int):
        if dias <=0:
            raise ValueError("Quantidade inválida de dias.")
        novo_fim = self.data_fim.days + timedelta(days=dias)
        self.data_fim = novo_fim
        print(f"Aluguel renovador por {dias}! Nova data de fim: {self.data_fim}")

    def verificar_atraso(self):
        hoje = date.today()

        if hoje>self.data_fim:
            dias_atraso = (hoje - self.data_fim).days
            return dias_atraso
        return 0
    
    def calcular_multa(self):
        dias_atraso = self.verificar_atraso()

        if dias_atraso > 0:
            precopdia = self.jogo_alugado.obter_preco()
            multa = dias_atraso * (precopdia * 0.3)
            return multa
        return 0.0
