from datetime import date
from models.cliente import Cliente
from models.FactoryJogo import FactoryJogo
from models.compra import Compra
from models.aluga import Aluga
from models.StrategyDesconto import SemDesconto, DescontoPIX, DescontoPromocional

clientes = []
jogos = []

def cadastrar_cliente():
    print("\n--- CADASTRO DE CLIENTE ---")
    
    #objeto temporário válido para usar os setters
    try:
        cliente = Cliente("Temporario", "00000000000", "temp@teste.com", "00000000000", "Temporario")
    except Exception as e:
        print(f"Erro interno ao inicializar cadastro: {e}")
        return

    while True:
        try:
            cliente.nome = input("Nome: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            cliente.cpf = input("CPF: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            cliente.email = input("Email: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            cliente.telefone = input("Telefone: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            cliente.endereco = input("Endereço: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")
            
    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")

def cadastrar_jogo():
    print("\n--- CADASTRO DE JOGO ---")
    tipo = input("Tipo de jogo (venda / aluguel): ").strip().lower()
    if tipo not in ["venda", "aluguel"]:
        print("Tipo inválido!")
        return
        
    try:
        #pra poder usar os setters
        if tipo == "venda":
            jogo = FactoryJogo.criarJogo(
                "venda", nome="Temp", genero="Temp", classfIndicativa="E",
                data_lancamento="01/01/2000", desenvolvedora="Temp",
                estoque=1, plataforma="Temp", preco=0.0, garantia="01/01/2000"
            )
        else:
            jogo = FactoryJogo.criarJogo(
                "aluguel", nome="Temp", genero="Temp", classfIndicativa="E",
                data_lancamento="01/01/2000", desenvolvedora="Temp",
                estoque=1, plataforma="Temp", preco_por_dia=0.0
            )
    except Exception as e:
        print(f"Erro interno ao criar instância do jogo: {e}")
        return

    while True:
        try:
            jogo.nome = input("Nome do Jogo: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            jogo.genero = input("Gênero: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            jogo.classfIndicativa = input("Classificação Indicativa: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            jogo.data_lancamento = input("Data de Lançamento (DD/MM/AAAA): ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            jogo.desenvolvedora = input("Desenvolvedora: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            jogo.estoque = int(input("Quantidade em Estoque: "))
            break
        except ValueError:
            print("Erro: A quantidade de estoque deve ser um número inteiro. Tente novamente.")
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    while True:
        try:
            jogo.plataforma = input("Plataforma: ")
            break
        except Exception as e:
            print(f"Erro: {e} Tente novamente.")

    if tipo == "venda":
        while True:
            try:
                jogo.preco = float(input("Preço de Venda: R$ "))
                break
            except ValueError:
                print("Erro: O preço deve ser um número decimal. Tente novamente.")
            except Exception as e:
                print(f"Erro: {e} Tente novamente.")

        while True:
            try:
                jogo.garantia = input("Data de Fim da Garantia (DD/MM/AAAA): ")
                break
            except Exception as e:
                print(f"Erro: {e} Tente novamente.")
    else:
        while True:
            try:
                jogo.preco_por_dia = float(input("Preço por Dia de Aluguel: R$ "))
                break
            except ValueError:
                print("Erro: O preço deve ser um número decimal. Tente novamente.")
            except Exception as e:
                print(f"Erro: {e} Tente novamente.")
                
    jogos.append(jogo)
    print(f"\nJogo do tipo {tipo} cadastrado com sucesso!")

def listar_jogos():
    print("\n--- JOGOS CADASTRADOS ---")
    if not jogos:
        print("Nenhum jogo cadastrado.")
        return
    for i, jogo in enumerate(jogos):
        print(f"\nID: {i}")
        jogo.exibir_dados()
        print("-" * 30)

def listar_clientes():
    print("\n--- CLIENTES CADASTRADOS ---")
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for i, cliente in enumerate(clientes):
        print(f"ID: {i} | Nome: {cliente.nome} | CPF: {cliente.cpf}")

def realizar_compra():
    print("\n--- REALIZAR COMPRA ---")
    if not clientes or not jogos:
        print("É necessário ter clientes e jogos cadastrados.")
        return
        
    listar_clientes()
    try:
        id_cliente = int(input("\nDigite o ID do Cliente: "))
        cliente = clientes[id_cliente]
    except (ValueError, IndexError):
        print("ID de cliente inválido!")
        return
    
    listar_jogos()
    try:
        id_jogo = int(input("\nDigite o ID do Jogo de VENDA: "))
        jogo = jogos[id_jogo]
        if hasattr(jogo, 'preco_por_dia'):
            print("Este jogo é apenas para aluguel! Escolha um jogo de venda.")
            return
    except (ValueError, IndexError):
        print("ID de jogo inválido!")
        return
    
    try:
        data_pag = input("Data do Pagamento (DD/MM/AAAA): ")
        forma_pag = input("Forma de Pagamento (crédito, débito, pix, boleto, dinheiro): ")
        
        print("\nEscolha a Estratégia de Desconto:")
        print("1 - Sem Desconto")
        print("2 - Desconto PIX (5%)")
        print("3 - Desconto Promocional (12%)")
        op_desc = input("Opção: ")
        
        estrategia = SemDesconto()
        if op_desc == "2":
            estrategia = DescontoPIX()
        elif op_desc == "3":
            estrategia = DescontoPromocional()
            
        compra = Compra(data_pag, forma_pag, jogo, estrategia)
        cliente.realizar_compra(compra)
        print(f"\nCompra realizada com sucesso para {cliente.nome}!")
    except Exception as e:
        print(f"\nErro na compra: {e}")

def realizar_aluguel():
    print("\n--- REALIZAR ALUGUEL ---")
    if not clientes or not jogos:
        print("É necessário ter clientes e jogos cadastrados.")
        return
        
    listar_clientes()
    try:
        id_cliente = int(input("\nDigite o ID do Cliente: "))
        cliente = clientes[id_cliente]
    except (ValueError, IndexError):
        print("ID de cliente inválido!")
        return
    
    listar_jogos()
    try:
        id_jogo = int(input("\nDigite o ID do Jogo de ALUGUEL: "))
        jogo = jogos[id_jogo]
        if hasattr(jogo, 'preco'):
            print("Este jogo é apenas para venda! Escolha um jogo de aluguel.")
            return
    except (ValueError, IndexError):
        print("ID de jogo inválido!")
        return
    
    try:
        data_ini = input("Data de Início (DD/MM/AAAA): ")
        data_fim = input("Data de Fim (DD/MM/AAAA): ")
        forma_pag = input("Forma de Pagamento (crédito, débito, pix, boleto, dinheiro): ")
        
        aluguel = Aluga(data_ini, data_fim, forma_pag, jogo)
        cliente.realizar_aluguel(aluguel)
        print(f"\nAluguel registrado com sucesso para {cliente.nome}!")
    except Exception as e:
        print(f"\nErro no aluguel: {e}")

def consultar_historico_cliente():
    print("\n--- CONSULTAR HISTÓRICO DO CLIENTE ---")
    listar_clientes()
    if not clientes:
        return
    try:
        id_cliente = int(input("\nDigite o ID do Cliente para puxar o histórico: "))
        cliente = clientes[id_cliente]
        
        print("\n" + "="*40)
        cliente.exibir_dados()
        cliente.listar_compras()
        cliente.listar_alugueis()
        print("="*40)
    except (ValueError, IndexError):
        print("ID de cliente inválido!")

def menu():
    while True:
        print("\n" + "="*10 + " LOJA DE VIDEOGAMES " + "="*10)
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Jogo")
        print("3. Listar Jogos")
        print("4. Realizar Compra de Jogo")
        print("5. Realizar Aluguel de Jogo")
        print("6. Consultar Cliente (Histórico/Dados)")
        print("0. Sair")
        print("="*39)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            cadastrar_jogo()
        elif opcao == "3":
            listar_jogos()
        elif opcao == "4":
            realizar_compra()
        elif opcao == "5":
            realizar_aluguel()
        elif opcao == "6":
            consultar_historico_cliente()
        elif opcao == "0":
            print("\nSaindo...")
            break
        else:
            print("\nOpção inválida!")

if __name__ == "__main__":
    menu()