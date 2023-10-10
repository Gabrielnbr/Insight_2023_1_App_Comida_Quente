'''
pagina_votoss
Ela deve conter os principais valores de um dash para visualização dos votoss:

1. Tabela estatística dos valores de gasto médio para dois com as colunas: 
    mínimo, máximo, média, mediana seguido de um histograma e boxplot.
        1.1 Esses valores poderão ser filtrados por:
            país, cidade, price range
2. Indicadores como:
    Total de atendimentos, faturamento total
'''

import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import plotly.express as px

from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_votos as mv

def apresentacao_votos(data):
    
    st.header('Página de avaliação dos clientes', divider=True)
    
    data = mv.filtro_lateral(data)
    
    # 1º Linha - Inicadores dos votos 
    mv.layout_indicadores(data)
    
    # Linha 2 - votoss x Pais
    mv.layout_pais(data)
    
    # Linha 3 - votos x Cidade
    mv.layout_cidade(data)
    
    # Linha 4 - votoss x Cozinhas
    mv.layout_culinaria(data)
    
    # Linha 5 - Tabelão
    mv.tabelao(data)

def app():
    
    data = get_data_transformed()
    
    apresentacao_votos(data)