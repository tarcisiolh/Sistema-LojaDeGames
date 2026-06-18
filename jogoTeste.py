from models.FactoryJogo import FactoryJogo
#https://www.igdb.com/
print("Criando Jogo para Aluguel via Factory")
jogo_aluguel = FactoryJogo.criarJogo(
            tipo="aluguel",
            nome="Metroid Prime 2: Echoes",
            genero="Shooter/Platform/Adventure",
            classfIndicativa="14",
            data_lancamento="15/11/2004",
            desenvolvedora="Retro Studios",
            estoque=2,
            plataforma = "Gamecube",
            preco_por_dia=12.50
        )
jogo_aluguel.exibir_dados()
print(f"Preço obtido: R$ {jogo_aluguel.obter_preco():.2f}")
jogo_aluguel.atualizar_estoque(3)
print(f"Novo estoque: {jogo_aluguel.estoque}")


print("\nCriando Jogo para Venda via Factory")
jogo_venda = FactoryJogo.criarJogo(
            tipo="venda",
            nome="Metal Gear Solid 4: Guns of the Patriots",
            genero="Shooter/Tactical",
            classfIndicativa="18",
            data_lancamento="06/12/2008",
            desenvolvedora="Kojima Productions",
            estoque=6,
            plataforma="PS3",
            preco=100.00,
            garantia="20/10/2027"
        )
jogo_venda.exibir_dados()
print(f"Preço obtido: R$ {jogo_venda.obter_preco():.2f}")