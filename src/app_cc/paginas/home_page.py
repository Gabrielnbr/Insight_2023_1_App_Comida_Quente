# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Home Page"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Home Page"
# License: MIT License

import streamlit as st
from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_home_page as mh

def app():
    """
    Este método é o responsável por inicializar a página Home page no Streamlit.
    Ele é chamado pelo arquivos app.py
    
    Essa função não possui nenhum argumento ou retorno.
    """
    st.header("Seja bem vindo ao Dashboard do aplicativo comida quente.", divider= "blue")
    
    mh.apredentacao_geral()
    
    mh.estrutura_dashboard()
    
    mh.contato()