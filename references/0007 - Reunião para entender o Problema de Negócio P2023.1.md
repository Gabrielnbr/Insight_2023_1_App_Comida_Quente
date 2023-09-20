# 0007 - Reunião para entender o Problema de Negócio P2023.1

ID: 19
Status: Concluído
Descrição: Será a partir do problema de negócio que iremos complementar as tarefas
Data Entrega: 20/09/2023
DS - Projetos: [Projeto APP Comida Quente P2023.1](https://www.notion.so/Projeto-APP-Comida-Quente-P2023-1-6ccc249b1b134bf08eb5dfd40692e4dc?pvs=21)
Prioridade: Média
Próxima Tarefa: [0008 - Separar as questões de negócio P2023.1](https://www.notion.so/0008-Separar-as-quest-es-de-neg-cio-P2023-1-af06bb5e38c446668a89b790b24db8f3?pvs=21)
Tarefa Anterior: [0006 - Design Pattern Commit P2023.1](https://www.notion.so/0006-Design-Pattern-Commit-P2023-1-a844324c38364a3b96ec8e63ef0675b9?pvs=21)

Tipo de Empresa: E-commerce voltado ao ramo alimentício

Core Business: Disponibilizar uma plataforma de comunicação entre restaurante e cliente, no qual o cliente possa encontrar a comida selecionada no restaurante da sua escolha.

Problema principal: O CEO é novo na empresa e precisa entender como seu desempenho está ao longo do tempo. Com isso, ele levantou uma série de questões que precisamos responder dentro de, no máximo 5 dias e também pediu que selecionássemos as principais métricas que ele precise acompanhar para identificar a saúde da empresa.

Dúvidas do CEO: As dúvidas que ele levantou estão listadas abaixo.

- Gerais
    1. Quantos restaurantes únicos estão registrados?
    2. Quantos países únicos estão registrados?
    3. Quantas cidades únicas estão registradas?
    4. Qual o total de avaliações feitas?
    5. Qual o total de tipos de culinária registrados?
- Pais
    1. Qual o nome do país que possui mais cidades registradas?
    2. Qual o nome do país que possui mais restaurantes registrados?
    3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
    4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
    5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
    6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
    7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
    8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
    9. Qual o nome do país que possui, na média, a maior nota média registrada?
    10. Qual o nome do país que possui, na média, a menor nota média registrada?
    11. Qual a média de preço de um prato para dois por país?
- Cidade
    1. Qual o nome da cidade que possui mais restaurantes registrados?
    2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
    3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
    4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
    5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
    6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
    7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
    8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
- Restaurante
    1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
    2. Qual o nome do restaurante com a maior nota média?
    3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
    4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
    5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
    6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
    7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
    8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
- Tipos de Culinária
    1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
    2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
    3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
    4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
    5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
    6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
    7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
    8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
    9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
    10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
    11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
    12. Qual o tipo de culinária que possui a maior nota média?
    13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

Ações a serem tomadas:

1. Responder as 45 questões levantadas pelo CEO.
2. Anotar os insights durante o período.
3. Selecionar as métricas principais.
4. Desenhar a base dos dashboards para cada área listada de parguntas
    1. Selecionas as perguntas mais relevantes e construir o dahsboard.
5. Utilizar a plataforma do Streamlit para entregar dashboads ao CEO.