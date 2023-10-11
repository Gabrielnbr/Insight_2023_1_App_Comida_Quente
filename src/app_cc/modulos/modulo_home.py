import folium

import streamlit as st

from folium.plugins import MarkerCluster
from PIL import Image
from streamlit_folium import folium_static

def indicadores (data):
    
    col1, col2, col3, col4, col5 = st.columns(5)
    # Avaliações Feitas na Plataforma
    valor_metrica = data.loc[:,"votes"].sum()
    col1.metric(label = "Total de avaliações",
                value = valor_metrica
                )
    

        # Restaurante cadastrado
    restaurantes = len(data['restaurant_id'].unique())
    col2.metric(label = "Restaurantes Cadastrados",
                value= restaurantes
                )
    

        # Paises Cadastrados
    country = len(data['name_country'].unique())
    col3.metric(label = "Paises Cadastrados",
                value= country
                )
    

        # Cidades cadastradas
    city = len(data['city'].unique())
    col4.metric(label = "Cidades Cadastrados",
                value= city
                )
    
            # Cidades cadastradas
    city = len(data['cuisines'].unique())
    col5.metric(label = "Culinárias oferecidas",
                value= city
                )

def map(data):
    f = folium.Figure(width=1920, height=1080)

    m = folium.Map(max_bounds=True).add_to(f)

    marker_cluster = MarkerCluster().add_to(m)

    for _, line in data.iterrows():

        name = line["restaurant_name"]
        custo_para_dois_corrigido = line["custo_para_dois_corrigido"]
        cuisine = line["cuisines"]
        currency = line["currency"]
        rating = line["aggregate_rating"]
        color = f'{line["nome_cor"]}'

        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 ({}) para dois"
        html += "<br />Type: {}"
        html += "<br />Aggragate Rating: {}/5.0"
        html = html.format(name, custo_para_dois_corrigido, currency, cuisine, rating)

        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )

        folium.Marker(
            [line["latitude"], line["longitude"]],
            popup=popup,
            icon=folium.Icon(color=color, icon="home", prefix="fa"),
        ).add_to(marker_cluster)

    folium_static(m, width=1024, height=768)

def filtro_lateral(data):
    with st.sidebar:
        st.header('Home Page')
        
    return data