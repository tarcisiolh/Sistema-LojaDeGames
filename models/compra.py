from datetime import date, datetime
from models.JogoVenda import JogoVenda
from models.StrategyDesconto import StrategyDesconto, SemDesconto

class Compra:
    def __init__(self, data_pagamento: str, forma_pagamento: str, jogo_comprado: JogoVenda, estrategia_desconto: StrategyDesconto = SemDesconto()):
        self.data_pagamento = data_pagamento
        self.jogo_comprado = jogo_comprado
        self.forma_pagamento = forma_pagamento 
        self.estrategia_desconto = estrategia_desconto
    @property
    def data_pagamento(self):
        return self.__data_pagamento
    
    @property
    def forma_pagamento(self):
        return self.__forma_pagamento
    
    @property
    def jogo_comprado(self):
        return self.__jogo_comprado

    @property
    def estrategia_desconto(self):
        return self.__estrategia_desconto
    
    @data_pagamento.setter
    def data_pagamento(self, data: str):
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("A data deve estar no formato DD/MM/AAAA.")
        if not isinstance(data, date):
            raise ValueError("Data inválida.")
        if data > date.today():
            raise ValueError("A data de pagamento não pode ser maior que a data atual.")
        self.__data_pagamento = data

    @forma_pagamento.setter
    def forma_pagamento(self, novaFpag: str):
        formas_validas = {"crédito", "débito", "pix", "boleto", "dinheiro"}
        novaFpag = str(novaFpag).strip().lower()
        if novaFpag not in formas_validas:
            raise ValueError("Forma de pagamento inválida.")
        self.__forma_pagamento = novaFpag

    @jogo_comprado.setter
    def jogo_comprado(self, jogo: JogoVenda):
        if not isinstance(jogo, JogoVenda):
            raise ValueError("O jogo comprado deve primeiramente existir.")
        self.__jogo_comprado = jogo
        self.jogo_comprado.atualizar_estoque(-1)

    @estrategia_desconto.setter
    def estrategia_desconto(self, estrategia: StrategyDesconto):
        if not isinstance(estrategia, StrategyDesconto):
            raise ValueError("Estratégia de desconto inválida.")
        self.__estrategia_desconto = estrategia

    def calcular_total(self):
        preco_do_jogo = self.jogo_comprado.obter_preco()
        valor_final = self.__estrategia_desconto.calcular_desconto(preco_do_jogo)       
        return valor_final

    def exibir_dados(self):
        nome_desconto = self.estrategia_desconto.__class__.__name__
        print(f"Data Pagamento: {self.data_pagamento}\nForma de Pagamento: {self.forma_pagamento.capitalize()}\nJogo Comprado: {self.jogo_comprado}\nDesconto Aplicado: {nome_desconto}\nValor Total Pago: R$ {self.calcular_total():.2f}")