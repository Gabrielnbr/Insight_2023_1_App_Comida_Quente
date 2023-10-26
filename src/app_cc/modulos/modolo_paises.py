# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Países"
# no aplicativo Streamlit. Ele define as funções que serão utilizadas pelo arquivo "pagina_paises.py"
# para gerar os elementos de visualização da página, bem como seus filtros.
# License: MIT License

import streamlit as st
import plotly.express as px

def restaurante_pais_graph(data):
    """
    Esta função plota um gráfico de barras da contagem de restaurantes por países no applicativo streamlit.
    
    Args:
        Data = DataFrame contendo as colunas 'restaurante_id' e 'name_country'
    
    Return:
        Não retorna nenhum valor
    """
    data_aux = data.loc[:,['restaurant_id','name_country']].groupby('name_country').count().sort_values(by='restaurant_id', ascending = False).reset_index()
    fig = px.bar(data_aux,
                x='name_country',
                y='restaurant_id',
                title='Quantidade de restaurantes por País', 
                labels={'name_country': 'País', 'restaurant_id': 'Qtde Restaurantes'})
    fig.update_traces(texttemplate = '%{y}')
    
    st.plotly_chart(fig, use_container_width=True);

def cidade_pais_graph(data):
    """
    Esta função plota um gráfico de barras da contagem única de cidades por países no applicativo streamlit.
    
    Args:
        Data = DataFrame contendo as colunas 'city' e 'name_country'
    
    Return:
        Não retorna nenhum valor
    """
    data_aux = data.loc[:,['city','name_country']].groupby('name_country').nunique().sort_values(by='city', ascending = False).reset_index()
    fig = px.bar(data_aux,
                x='name_country',
                y='city',
                title='Quantidade de cidades por País',
                labels={'name_country': 'País', 'city': 'Qtde Cidades'})
    fig.update_traces(texttemplate = '%{y}')
    
    st.plotly_chart(fig, use_container_width=True);

def mean_pais_graphs(data):
    """
    Esta função plota dois gráficos de barras, lado a lado, no applicativo streamlit, sendo:
    1º A média de votos por país
    2º A média do custo do prato para dois por país
    
    Args:
        Data = DataFrame contendo as colunas 'restaurante_id', 'name_country' e 'custo_para_dois_corrigido'
    
    Return:
        Não retorna nenhum valor
    """
    vote_pais, prato2_pais = st.columns(2)
    
    # 1º Coluna A média de votos por país
    with vote_pais:
        data_aux = data.loc[:,['votes','name_country']].groupby('name_country').mean().sort_values(by='votes', ascending = False).reset_index()
        fig_vote_pais = px.bar(data_aux,
                                x='name_country',
                                y='votes',
                                title='Quantidade de votos por País', 
                                labels={'name_country': 'País', 'votes': 'Avaliações'})
        fig_vote_pais.update_traces(texttemplate = '%{y}')
        
        st.plotly_chart(fig_vote_pais, use_container_width=True);
    
    #2º Coluna A média do custo do prato para dois por país
    with prato2_pais:
        data_aux = data.loc[:,['custo_para_dois_corrigido','name_country']].groupby('name_country').mean().sort_values(by='custo_para_dois_corrigido', ascending = False).reset_index()
        fig_prato2_pais = px.bar(data_aux,
                                x='name_country',
                                y='custo_para_dois_corrigido',
                                title='Quantidade de votos por País', 
                                labels={'name_country': 'País', 'custo_para_dois_corrigido': 'Valor do prato para 2'})
        fig_prato2_pais.update_traces(texttemplate = '%{y}')
        
        st.plotly_chart(fig_prato2_pais, use_container_width=True);