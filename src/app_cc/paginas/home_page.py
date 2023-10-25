# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Home Page"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Home Page"
# License: MIT License

import streamlit as st
from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_home as mh

def apresentacao_home(data):
    """
    Este método é responsável por organizar a estrutura da página de apresentação "Home Page".
    
    Args:
        data = DataFrame
        Normalmente esse DataFrame já vem limpo do arquivo "paginas.pagina_tratamento.py",
        da função "get_data_transformed", cujo é acessado dentro da função app() neste mesmo arquivo.
    
    Esta função não possui retorno
    """
    st.header('Home Page', divider=True)
    
    st.subheader("Essa é a home page", divider=True)
    
    data = mh.filtro_lateral(data)
    
    mh.indicadores(data)
    
    mh.map(data)

def app():
    """
    Este método é o responsável por inicializar a página países no Streamlit.
    Ele é chamado pelo arquivo "app.py" 
    
    Essa função não possui nenhum argumento ou retorno.
    """
    data = get_data_transformed()
    
    apresentacao_home(data)