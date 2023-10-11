import streamlit as st
from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_home as mh

def apresentacao_home(data):
    
    st.header('Home Page', divider=True)
    
    st.subheader("Essa é a home page", divider=True)
    
    data = mh.filtro_lateral(data)
    
    mh.indicadores(data)
    
    mh.map(data)

def app():
    data = get_data_transformed()
    
    apresentacao_home(data)