from models.JogoAlugado import JogoAlugado
from models.JogoVenda import JogoVenda
class FactoryJogo:
    
    @staticmethod
    def criarJogo(tipo: str, **kwargs):
        #para informação, não vim na aula sobre o Factory e não lembro de ter visto sobre kwargs
        #li nesse site como funciona https://realpython.com/python-kwargs-and-args/ e com sugestão de IA decidi usar pela praticidade, já que ele passa todos os argumentos nomeados diretamente
        tipo = str(tipo).strip().lower()
        
        if tipo == "aluguel":
            return JogoAlugado(**kwargs)
            
        elif tipo == "venda":
            return JogoVenda(**kwargs)
            
        else:
            raise ValueError("Tipo de jogo inválido. Escolha 'aluguel' ou 'venda'.")