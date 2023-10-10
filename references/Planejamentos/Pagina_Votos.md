# Planjemaneto da Página de Votos

## 1. Premissas
Premissas, para esta página existir estou assumindo:

1. A quantidade de votos em cada estabelecimento é a mesma quantidade de votoss que ele recebeu de forma mais recente.
2. Os votoss só podem fazer 1 único voto no aplicativo.
3. Quando o votos vota  em outro restaurante o voto anterior é descartado. Isso ocorre para mostrar a dinamicidade com que as pessoas escolhem restaurante A ou B e quanto tempo essa escolha dura.
4. Estamos pegando um recorte de um curto espaço de tempo.

## 1.1. Estrutura da página

A página terá 6 linhas ao total, sendo:

1. Na linha 1, será subdividaida em colunas para colocar os principais indicadores, no máximo 5.

| Indicador A | Indicador B | Indicador C | ... |
|---|---|---|--|

1. Da linha 2 a 4 todas terão o mesmo formato. Composto por 2 colunas. A primeira terá um agráfico ainda a ser estudado, e a segunda terá o Dataframe do Gráfico.
2. Todas as colunas terão como base o votos e serão combinadas com outros valores.
   1. A 2ª linha votos x País
   2. A 3ª linha votos x Cidade
   3. A 4ª linha votos x Culinária

| Gráfico | DataFrame |
|---|---|

5. A ultima coluna será um tabelão com todos os valores apresentados acima.

### 1.1.1. Estrutura comum a todos

1. Será possível baixar o Dataframe de todos os gráficos de forma isolada.
2. Os filtros alterarão todas as visões e valores.
3. Todos terão um terceiro valor que será o gasto médio para duas pessoas.

## 1.2. Filtros
Terão os filtros por:
1. País
2. Cidade
3. Cosinhas
4. Gasto médio para duas pessoas.

Os filtros ainda serão decididos, mas possivelmente será slidebar e multiselect.