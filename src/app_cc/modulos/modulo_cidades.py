# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina cidades"
# no aplicativo Streamlit. Ele define as funções que serão utilizadas pelo arquivo "pagina_cidades.py"
# para gerar os elementos de visualização da página, bem como seus filtros.
# License: MIT License

import streamlit as st
import plotly.express as px

def cidade_restaurante_graph(data):
    data_top = (data.loc
                [:,['city','restaurant_id']]
                .groupby('city')
                .count()
                .sort_values(by='restaurant_id', ascending = False)
                .reset_index().
                head(10))
    fig = px.bar(data_top,
             y='restaurant_id',
             x='city',
             title='Top 10 cidades com mais restaurantes cadastrados', 
             labels={'city': 'Cidade','restaurant_id': 'Qtde Restaurantes'})
    fig.update_traces(texttemplate = '%{y}')
    st.plotly_chart(fig,use_container_width=True)

def min_max_restaurante_cidade(data):
    
    #max, min = st.columns(2)
    
    #with max:
        data_max = (
        data.loc[
            (data["aggregate_rating"] >= 4),
            ["restaurant_id", "name_country", "city"],
        ]
        .groupby(["name_country", "city"])
        .count()
        .sort_values(["restaurant_id", "city"], ascending=[False, True])
        .reset_index()
        )
        fig_max = px.bar(data_max,
                     y='restaurant_id',
                     x='city',
                     title='Quantidade restaurantes cadastrados por cidade com média de avaliação acima de 4', 
                     labels={'city': 'Cidade','restaurant_id': 'Qtde Restaurantes'})
        fig_max.update_traces(texttemplate = '%{y}')
        st.plotly_chart(fig_max,use_container_width=True)
    
    #with min:
        data_min = (data.loc[
                        (data["aggregate_rating"] <= 2.5) & (data["name_country"].isin(data['name_country'])),
                        ["restaurant_id", "name_country", "city"],
                    ]
                    .groupby(["name_country", "city"])
                    .count()
                    .sort_values(["restaurant_id", "city"], ascending=[False, True])
                    .reset_index()
                    )

        fig_min = px.bar(
            data_min.head(7),
            x="city",
            y="restaurant_id",
            text="restaurant_id",
            text_auto=".2f",
            color="name_country",
            title="Top 7 Cidades com Restaurantes com média de avaliação abaixo de 2.5",
            labels={
                "city": "Cidade",
                "restaurant_id": "Quantidade de Restaurantes",
                "name_country": "País",
                },
            )
        st.plotly_chart(fig_min,use_container_width=True)