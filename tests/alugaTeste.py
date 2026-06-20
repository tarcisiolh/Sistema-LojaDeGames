import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from models.FactoryJogo import FactoryJogo
from models.aluga import Aluga

jogo_aluguel = FactoryJogo.criarJogo(
    tipo="aluguel",
    nome="Rayman Legends",
    genero="Platform/Adventure",
    classfIndicativa="10",
    data_lancamento="29/08/2013",
    desenvolvedora="Ubisoft",
    estoque=3,
    plataforma="Wii U, PS Vita",
    preco_por_dia = 10.00
)

aluga = Aluga(
    data_inicio="17/06/2026",
    data_fim="22/06/2026",
    forma_pagamento="boleto",
    jogo_alugado=jogo_aluguel
)

jogo_aluguel2 = FactoryJogo.criarJogo(
    tipo="aluguel",
    nome="Sonic Frontiers",
    genero="Platform/Adventure",
    classfIndicativa="10",
    data_lancamento="11/07/2022",
    desenvolvedora="Sonic Team",
    estoque=1,
    plataforma="PS5",
    preco_por_dia = 20.00
)

aluga2 = Aluga(
    data_inicio="16/06/2026",
    data_fim="18/06/2026",
    forma_pagamento="boleto",
    jogo_alugado=jogo_aluguel2
)

jogo_aluguel3 = FactoryJogo.criarJogo(
    tipo="aluguel",
    nome="Crazy Taxi",
    genero="Racing/Arcade",
    classfIndicativa="10",
    data_lancamento="24/01/1999",
    desenvolvedora="Hitmaker",
    estoque=2,
    plataforma="Dreamcast",
    preco_por_dia = 7.20
)

aluga3 = Aluga(
    data_inicio="17/06/2026",
    data_fim="20/06/2026",
    forma_pagamento="boleto",
    jogo_alugado=jogo_aluguel3
)

aluga.devolver_jogo()
aluga2.devolver_jogo()
aluga3.devolver_jogo()



