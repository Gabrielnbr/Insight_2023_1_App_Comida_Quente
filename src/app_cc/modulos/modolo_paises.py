# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Países"
# no aplicativo Streamlit. Ele define as funções que serão utilizadas pelo arquivo "pagina_paises.py"
# para gerar os elementos de visualização da página, bem como seus filtros.
# License: MIT License

import streamlit as st
import plotly.express as px

def filtro_lateral(data):
    with st.sidebar:
        st.header('Filtro Países')
    return data