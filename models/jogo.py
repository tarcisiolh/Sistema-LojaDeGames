from abc import ABC, abstractmethod
from datetime import datetime, date

class Jogo(ABC):
    def __init__(self, nome:str, genero:str, classfIndicativa:str, data_lancamento:str, desenvolvedora:str, estoque:int, plataforma:str):
        self.nome = nome
        self.genero = genero
        self.classfIndicativa = classfIndicativa
        self.data_lancamento = data_lancamento
        self.desenvolvedora = desenvolvedora
        self.estoque = estoque
        self.plataforma= plataforma

    @property
    def nome(self):
        return self.__nome

    @property
    def genero(self):
        return self.__genero

    @property
    def classfIndicativa(self):
        return self.__classfIndicativa

    @property
    def data_lancamento(self):
        return self.__data_lancamento

    @property
    def desenvolvedora(self):
        return self.__desenvolvedora

    @property
    def estoque(self):
        return self.__estoque

    @property
    def plataforma(self):
        return self.__plataforma
    
    @nome.setter
    def nome(self, novoNome: str):
        if not novoNome or not novoNome.strip():
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.strip()

    @genero.setter
    def genero(self, novoGenero : str):
        if not novoGenero or not novoGenero.strip():
            raise Exception("Gênero é obrigatório.")
        self.__genero = novoGenero.strip()

    @classfIndicativa.setter
    def classfIndicativa(self, novaClassificacao:str):
        classificacoes_validas = {"E", "10", "12", "14", "16", "18"}
        novaClassificacao = str(novaClassificacao).strip().upper()
        if novaClassificacao not in classificacoes_validas:
            raise ValueError("Classificação indicativa inválida. Valores permitidos: E, 10, 12, 14, 16 ou 18.")
        self.__classfIndicativa = novaClassificacao

    @data_lancamento.setter
    def data_lancamento(self, data:str):
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("A data deve estar no formato DD/MM/AAAA.")
        if not isinstance(data, date):
            raise ValueError("Data inválida.")
        if data > date.today():
            raise ValueError("A data de lançamento não pode ser maior que a data atual.")
        self.__data_lancamento = data

    @desenvolvedora.setter
    def desenvolvedora(self, novaDesenvolvedora:str):
        if not novaDesenvolvedora or not novaDesenvolvedora.strip():
            raise Exception("Desenvolvedora é obrigatória.")
        self.__desenvolvedora = novaDesenvolvedora.strip()

    @estoque.setter
    def estoque(self, novoEstoque:int):
        if novoEstoque < 0:
            raise Exception("Estoque não pode ser menor que 0.")
        self.__estoque = novoEstoque

    @plataforma.setter
    def plataforma(self, novaPlataforma:str):
        if not novaPlataforma or not novaPlataforma.strip():
            raise Exception("Plataforma é obrigatória.")
        self.__plataforma = novaPlataforma.strip()

    def __str__(self):
        data_formatada = self.data_lancamento.strftime("%d/%m/%Y")
        return f"Nome: {self.nome}\nGenero: {self.genero}\nClassificação: {self.classfIndicativa}\nLançamento: {data_formatada}\nDesenvolvedora: {self.desenvolvedora}\nEstoque: {self.estoque}\nPlataforma: {self.plataforma}"

    def __eq__(self, other):
        if not isinstance(other, Jogo):
            return False
        return self.nome == other.nome and self.desenvolvedora == other.desenvolvedora and self.data_lancamento == other.data_lancamento
    
    def exibir_dados(self):
        data_formatada = self.data_lancamento.strftime("%d/%m/%Y")
        print(f"Nome: {self.nome}\nGenero: {self.genero}\nClassificação: {self.classfIndicativa}\nLançamento: {data_formatada}\nDesenvolvedora: {self.desenvolvedora}\nEstoque: {self.estoque}\nPlataforma: {self.plataforma}")

    def atualizar_estoque(self, quantidade):
        self.estoque += quantidade

    @abstractmethod
    def obter_preco(self):
        pass