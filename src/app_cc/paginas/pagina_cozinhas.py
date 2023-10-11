import streamlit as st
from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_cozinhas as mc

def apresentacao_cozinhas(data):
    
    st.header('Página de Cozinhas', divider=True)
    
    st.subheader("Página de Cozinhas", divider=True)
    
    data = mc.filtro_lateral(data)
    
    mc.df_top_cozinhas(data)
    
    mc.top_cozinhas(data)
    
def app():
    data = get_data_transformed()
    
    apresentacao_cozinhas(data)