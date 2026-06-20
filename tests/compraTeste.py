import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.FactoryJogo import FactoryJogo
from models.compra import Compra
from models.StrategyDesconto import DescontoPIX, DescontoPromocional

jogo_venda = FactoryJogo.criarJogo(
    tipo="venda",
    nome="Star Fox Zero",
    genero="Shooter/Adventure",
    classfIndicativa="10",
    data_lancamento="21/04/2016",
    desenvolvedora="PlatinumGames",
    estoque=3,
    plataforma="Wii U",
    preco=160.20,
    garantia="19/11/2027"
)

compra_pix = Compra(
    data_pagamento="11/06/2026",
    forma_pagamento="pix",
    jogo_comprado=jogo_venda,
    estrategia_desconto=DescontoPIX()
)

compra_promo = Compra(
    data_pagamento="19/06/2026",
    forma_pagamento="crédito",
    jogo_comprado=jogo_venda,
    estrategia_desconto=DescontoPromocional()
)

compra_sdesc = Compra(
    data_pagamento="19/06/2026",
    forma_pagamento="crédito",
    jogo_comprado=jogo_venda
)

compra_pix.exibir_dados()
print(f"\nTotal a pagar (com 5% de desconto): R$ {compra_pix.calcular_total():.2f}\n")

compra_promo.exibir_dados()
print(f"\nTotal a pagar (com 12% de desconto): R$ {compra_promo.calcular_total():.2f}")

compra_sdesc.exibir_dados()
print(f"\nTotal a pagar (sem desconto): R$ {compra_sdesc.calcular_total():.2f}")