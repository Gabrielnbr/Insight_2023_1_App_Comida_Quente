# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Votos"
# no aplicativo Streamlit. Ele define as funções que serão utilizadas pelo arquivo "pagina_votos.py"
# para gerar os elementos de visualização da página, bem como seus filtros.
# License: MIT License

import numpy            as np
import streamlit        as st
import plotly.express   as px

def indicador_qtde_total_votos(data):
    votos_totais = data['votes'].sum()
    st.metric(label = 'Total de Votos',
              value = votos_totais)

def indicador_media_votos(data):
    votos_medio = round(np.mean(data['votes']),2) 
    st.metric(label = 'Media de Votos',
          value = votos_medio)

def indicador_mediana_votos(data):
    votos_mediana = np.median(data['votes'])
    st.metric(label = 'Mediana dos Votos',
          value = votos_mediana)

def indicador_std_votos(data):
    votos_std = round(np.std(data['votes']),2)
    st.metric(label = 'Desvio Padrão dos Votos',
          value = votos_std)

def layout_indicadores(data):
        
    with st.container():
        st.markdown('## Indicadores dos votos')
        
        qtde, media, mediana, std = st.columns(4)
        
        with qtde:
            indicador_qtde_total_votos(data)
            
        with media:
            indicador_media_votos(data)
        
        with mediana:
            indicador_mediana_votos(data)
        
        with std:
            indicador_std_votos(data)
        
        st.divider()

def votos_pais_graph(data):
    voto_pais = data.loc[:,['votes','name_country','custo_para_dois_corrigido']].groupby('name_country').sum().sort_values(by='votes', ascending=False).reset_index()
    fig = px.bar(voto_pais, x='name_country', y='votes',text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

def votos_pais_df(data):
    voto_pais = data.loc[:,['votes','name_country','custo_para_dois_corrigido']].groupby('name_country').sum().sort_values(by='votes', ascending=False).reset_index()
    st.dataframe(voto_pais, use_container_width=True)

def layout_pais(data):
        # Linha 2 - votoss x Pais
    with st.container():
        st.markdown('## Votos x Pais')
        
        col1, col2 = st.columns(2)
        
        # Gráfico
        with col1:
            st.markdown('### votos_pais_graph')
            votos_pais_graph(data)
            
        # Data Frame
        with col2:
            st.markdown('### votos_pais_df')
            votos_pais_df(data)
        st.divider()

def votos_cidade_graph(data):
    voto_pais = data.loc[:,['votes','city','custo_para_dois_corrigido']].groupby('city').sum().sort_values(by='votes', ascending=False).reset_index()
    fig = px.bar(voto_pais, x='city', y='votes',text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

def votos_cidade_df(data):
    voto_pais = data.loc[:,['votes','city','custo_para_dois_corrigido']].groupby('city').sum().sort_values(by='votes', ascending=False).reset_index()
    st.dataframe(voto_pais, use_container_width=True)

def layout_cidade(data):
    # Linha 3 - votos x Cidade
    with st.container():
        st.markdown('## Votos x Cidade')
        
        col1, col2 = st.columns(2)
        
        # Gráfico
        with col1:
            st.markdown('### votos_cidade_graph')
            votos_cidade_graph(data)
            
        # Data Frame
        with col2:
            st.markdown('### votos_cidade_df')
            votos_cidade_df(data)
        st.divider()


def votos_culinaria_graph(data):
    voto_pais = data.loc[:,['votes','cuisines','custo_para_dois_corrigido']].groupby('cuisines').sum().sort_values(by='votes', ascending=False).reset_index()
    fig = px.bar(voto_pais, x='cuisines', y='votes',text_auto=True)
    st.plotly_chart(fig, use_container_width=True)

def votos_culinaria_df(data):
    voto_pais = data.loc[:,['votes','cuisines','custo_para_dois_corrigido']].groupby('cuisines').sum().sort_values(by='votes', ascending=False).reset_index()
    st.dataframe(voto_pais, use_container_width=True)

def layout_culinaria(data):
    # Linha 4 - votoss x Cozinhas
    with st.container():
        st.markdown('## Votos x Cozinhas')
        
        col1, col2 = st.columns(2)
        
        # Gráfico
        with col1:
            st.markdown('### votos_culinaria_graph')
            votos_culinaria_graph(data)
            
        # Data Frame
        with col2:
            st.markdown('### votos_culinaria_df')
            votos_culinaria_df(data)
        st.divider()

def tabelao(data):
    with st.container():
        st.markdown('# Tabela Resumo')
        voto_pais = data.loc[:,['votes','name_country','city','cuisines','custo_para_dois_corrigido']].groupby(['name_country','city','cuisines']).mean().sort_values(by='votes', ascending=False).reset_index()
        st.dataframe(round(voto_pais,2), use_container_width=True)

def filtro_lateral(data):
    with st.sidebar:
        st.header('Página de votos')
        
        multi_pais = st.multiselect('Pais', sorted(set(data['name_country'].unique())))
        if multi_pais != []:
            data = data.loc[data['name_country'].isin(multi_pais)]
        else:
            data = data.copy()
        
        multi_cidade = st.multiselect('Cidade', sorted(set(data['city'].unique())))
        if multi_cidade != []:
            data = data.loc[data['city'].isin(multi_cidade)]
        else:
            data = data.copy()
        
        multi_culinaria = st.multiselect('Tipo de Cozinha', sorted(set(data['cuisines'].unique())))
        if multi_culinaria != []:
            data = data.loc[data['cuisines'].isin(multi_culinaria)]
        else:
            data = data.copy()
        
    return data