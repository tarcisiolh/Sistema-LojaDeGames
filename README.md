# Sistema de uma Loja de Videogames

## Descrição do projeto

Este projeto consiste no desenvolvimento de um sistema para gerenciar o catálogo e as operações comerciais de uma loja de videogames. O objetivo principal é controlar de forma eficiente as informações dos jogos disponíveis, automatizando o acompanhamento do estoque e a diferenciação dos produtos.
No sistema, os jogos são tratados de duas formas: títulos destinados à venda (com preço fixo e garantia) e títulos destinados ao aluguel (com cobrança por diárias). Além do controle dos jogos, o sistema também gerencia o cadastro de clientes.


## Diagrama de classes

Link para acesso: https://drive.google.com/file/d/1ZcCxa3mVieWcdaBfNZIEWY_UkYkmOWF-/view?usp=sharing
<br><br><br>
# Descrição das classes e Pilares de POO

## Jogo: 

Descrição: Classe abstrata que serve como base para todos os títulos cadastrados no sistema. Define a estrutura comum e as regras de integridade compartilhadas por qualquer tipo de jogo.

**Abstração: Utiliza o módulo ABC. A classe serve como um molde genérico para qualquer jogo e não pode ser instanciada diretamente. Ela usa o @abstractmethod def obter_preco(self), obrigando suas classes filhas a implementarem essa lógica.**

## JogoVenda e JogoAlugado:

Descrição: Subclasses especializadas de Jogo que representam os títulos disponíveis especificamente para aquisição definitiva ou aquisição temporária pelo cliente.

**Herança: Ambas herdam da classe base Jogo, reaproveitando todos os atributos (nome, gênero, desenvolvedora) e validações, adicionando apenas o que é específico de cada contexto (como garantia para venda e preco_por_dia para aluguel).**

**Polimorfismo: As duas classes sobrescrevem os métodos obter_preco() e exibir_dados() para que tenham comportamentos diferentes, dependendo se o jogo é destinado a venda ou aluguel.**


## Cliente:

Descrição: Entidade responsável por gerenciar os dados cadastrais dos usuários da loja, bem como centralizar o histórico de interações comerciais de cada um.

## Compra

Descrição: Representa o fluxo de fechamento e registro de uma venda realizada. É a classe que conecta o cliente ao produto final adquirido.

## Aluga

Descrição: Responsável por gerenciar o ciclo de vida de uma locação, desde a retirada do jogo até o momento da devolução física na loja.
<br><br>

**Todas as classes utilizam do encapsulamento. O acesso e a modificação de seus atributos são feitos estritamente através de getters e setters, que contêm regras robustas de validação.**
<br><br><br>

# Padrões de Projeto:

## Factory:

A classe FactoryJogo possui um método estático criarJogo() que recebe o tipo do jogo ("venda" ou "aluguel") e delega a criação para a classe correta, instanciando facilmente jogos de venda ou de aluguel sem espalhar condicionais de criação pelo código principal (Princípio da Responsabilidade Única).

Foi utilizado o empacotamento de dicionários do Python (kwargs) para passar todos os argumentos nomeados dinamicamente para os construtores, tornando a Factory extremamente limpa e prática de manter.

## Strategy

Em uma compra, o cálculo do valor final variava de acordo com a forma de pagamento ou promoções. Se fosse feito na classe Compra, exigiria múltiplos if/elif que precisariam ser alterados a cada nova regra de negócio (violando o princípio Aberto/Fechado).

Então, foi criada uma interface base StrategyDesconto. A partir dela, diferentes strategies foram implementadas em classes separadas: SemDesconto, DescontoPIX (5% de desconto) e DescontoPromocional (12% de desconto). A classe Compra apenas recebe a estratégia escolhida no momento do pagamento e chama o método calcular_desconto(), sem precisar saber como a matemática é feita.
<br><br><br>

## Instruções para execução

O main.py foi designado como um menu, então a instanciação de todas as classes pode ser feita diretamente pelas opções presente nele.

O menu tem como funções: 
- Cadastrar cliente;
- Cadastrar Jogo;
- Listar os jogos criados;
- Realizar a **Compra** de um jogo;
- Realizar o **Aluguel** de um jogo;
- Consultar histórico de um cliente.

Recomenda-se cadastrar um cliente e um jogo primeiro para poder testar o resto das opções. Ao realizar a compra ou aluguel do jogo criado, ele aparecerá junto dos dados do cliente na opção de consulta de histórico.

Caso alguma inserção seja feita de forma errada, a partir de um while o sistema pede novamente a inserção, mostrando onde o usuário errou ao usar o própio sistema de setters de cada atributo.

Já que o sistema foi implementado pouco a pouco, a pasta tests são testes básicos de instanciação de classes que fui utilizando ao decorrer da criação do trabalho, recomendo usar o main.
<br><br><br>

## Detalhamento do Aprendizado

- Dificuldades encontradas: Não tive muitas, maior parte do que foi utilizado nesse sistema foi anteriormente explicado no trabalho feito em aula sobre RPG. Sendo incisivo, tive dificuldade com a criação do UML e com as sintaxes dos Padrões de Projeto. Eu mesmo durante a realização do factory aponto no código que eu não fui na aula no dia e não sabia sobre kwargs.
- Como resolvi: Eu utilizei a IA para sanar minhas dúvidas e também pesquisei sobre essa parte do factory, como também fiz para a implementação do Strategy, que após ler umm artigo da alura sobre design patterns, decidi usar.
- Principal Aprendizado: Acredito que consegui entender melhor a realização de um UML e como as design patterns também fazem parte e alteram ele. Também acredito que sei aplicar agora o Factory e o Strategy facilmente.

<br><br><br>
## Declaração de Uso de IA

Utilizei IA como ferramenta de apoio.

Ferramenta(s): Gemini Pro 3.1

Finalidade: Revisão dos códigos e esclarecimento de dúvidas (realização do menu/design patterns), principalmente na realização do UML.

Validação: Declaro que todo o código gerado foi lido, testado e ajustado conforme as
necessidades específicas do projeto e da disciplina. A responsabilidade pela arquitetura,
decisões de design e correção do código é de minha total responsabilidade.
