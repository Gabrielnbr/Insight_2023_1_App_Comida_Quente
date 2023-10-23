import streamlit as st

import modulos.modolo_paises as mp

from paginas.pagina_tratamento import get_data_transformed

def apresentacao_paises(data):
    st.header("Pagina dos paises1")

def app():
    st.header("Página dos Países")
    
    data = get_data_transformed()
    
    apresentacao_paises(data)