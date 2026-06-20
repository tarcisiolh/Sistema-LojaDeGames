from models.jogo import Jogo
from datetime import datetime, date

class JogoVenda(Jogo):
    def __init__(self, nome: str, genero: str, classfIndicativa: str, data_lancamento: str, desenvolvedora: str, estoque: int, plataforma:str, preco: float, garantia: str):
        super().__init__(nome, genero, classfIndicativa, data_lancamento, desenvolvedora, estoque, plataforma)
        self.preco = preco
        self.garantia = garantia

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, novo_preco: float):
        if novo_preco < 0:
            raise ValueError("O preço de venda não pode ser menor que 0.")
        self.__preco = novo_preco

    @property
    def garantia(self):
        return self.__garantia

    @garantia.setter
    def garantia(self, data):
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("A data de garantia deve estar no formato DD/MM/AAAA.")
        if not isinstance(data, date):
            raise ValueError("Data de garantia inválida.")
        self.__garantia = data

    def exibir_dados(self):
        super().exibir_dados()
        data_formatada = self.garantia.strftime("%d/%m/%Y")
        print(f"Preço: R$ {self.preco:.2f}\nGarantia: {data_formatada}")

    def __str__(self):
        return super().__str__() + f"\nPreço: R$ {self.preco:.2f}\nGarantia: {self.garantia.strftime('%d/%m/%Y')}"
    
    def obter_preco(self):
        return self.preco