from models.jogo import Jogo

class JogoAlugado(Jogo):
    def __init__(self, nome: str, genero: str, classfIndicativa: str, data_lancamento: str, desenvolvedora: str, estoque: int, plataforma:str, preco_por_dia: float):
        super().__init__(nome, genero, classfIndicativa, data_lancamento, desenvolvedora, estoque, plataforma)
        self.preco_por_dia = preco_por_dia

    @property
    def preco_por_dia(self):
        return self.__preco_por_dia

    @preco_por_dia.setter
    def preco_por_dia(self, novo_preco: float):
        if novo_preco < 0:
            raise ValueError("O preço por dia não pode ser menor que 0.")
        self.__preco_por_dia = novo_preco

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Preço por dia: R$ {self.preco_por_dia:.2f}")

    def obter_preco(self):
        return self.preco_por_dia