from models.compra import Compra
from models.aluga import Aluga

class Cliente:
    def __init__(self, nome :str, cpf:str, email:str, telefone:str, endereco:str):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.__compras = []
        self.__alugueis = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def email(self):
        return self.__email
    
    @property
    def telefone(self):
        return self.__telefone
    
    @property
    def endereco(self):
        return self.__endereco
    
    @nome.setter
    def nome(self, novoNome: str):
        if not novoNome or not novoNome.strip():
            raise Exception("Nome é obrigatório.")
        self.__nome = novoNome.strip()

    @cpf.setter
    def cpf(self, novoCPF:str):
        if not novoCPF or not novoCPF.strip():
            raise Exception("CPF é obrigatório.")
        cpf_limpo = novoCPF.strip()
        if len(cpf_limpo) != 11:
            raise ValueError("O CPF não pode ter mais ou menos de 11 caracteres.")
        self.__cpf = cpf_limpo
    
    @email.setter
    def email(self, novo_email: str):
        if not novo_email or not novo_email.strip():
            raise Exception("Email é obrigatório.")
        email_limpo = novo_email.strip().lower()
        if not email_limpo.endswith(".com"):
            raise ValueError("O email deve terminar com '.com'.")
        self.__email = email_limpo

    @telefone.setter
    def telefone(self, novoTelefone:str):
        if not novoTelefone or not novoTelefone.strip():
            raise Exception("Telefone é obrigatório.")
        telefone_limpo = novoTelefone.strip()
        if len(telefone_limpo) != 11:
            raise ValueError("O Telefone não pode ter mais ou menos de 11 caracteres.")
        self.__telefone = telefone_limpo
    
    @endereco.setter
    def endereco(self, novoEndereco: str):
        if not novoEndereco or not novoEndereco.strip():
            raise Exception("Endereco é obrigatório.")
        self.__endereco = novoEndereco.strip()

    def realizar_compra(self, compra: Compra):
        if not isinstance(compra, Compra):
            raise ValueError("O objeto passado não é uma Compra válida.")
        self.__compras.append(compra)

    def realizar_aluguel(self, aluga: Aluga):
        if not isinstance(aluga, Aluga):
            raise ValueError("O objeto passado não é um Aluguel válido.")
        self.__alugueis.append(aluga)

    def listar_compras(self):
        if not self.__compras:
            print("Nenhuma compra realizada por este cliente.\n")
            return
        print(f"--- Histórico de Compras de {self.nome} ---")
        for compra in self.__compras:
            compra.exibir_dados()

    def listar_alugueis(self):
        if not self.__alugueis:
            print("Nenhum aluguel realizado por este cliente.\n")
            return
        print(f"--- Histórico de Aluguéis de {self.nome} ---")
        for aluguel in self.__alugueis:
            aluguel.exibir_dados()

    def exibir_dados(self):
        print(f"Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\n")

    def __str__(self):
        return f"Nome: {self.nome}\nCPF: {self.cpf}\nEmail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\n"
    
    def __eq__(self, other):
        if not isinstance(other, Cliente):
            return False
        return self.nome == other.nome and self.cpf == other.cpf
    