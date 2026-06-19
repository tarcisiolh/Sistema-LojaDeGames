from abc import ABC, abstractmethod
#https://www.alura.com.br/artigos/design-patterns-python
class StrategyDesconto(ABC):
    @abstractmethod
    def calcular_desconto(self, valor_base: float):
        pass

class SemDesconto(StrategyDesconto):
    def calcular_desconto(self, valor_base: float):
        return valor_base 

class DescontoPIX(StrategyDesconto):
    def calcular_desconto(self, valor_base: float):
        return valor_base * 0.95 

class DescontoPromocional(StrategyDesconto):
    def calcular_desconto(self, valor_base: float):
        return valor_base *0.88