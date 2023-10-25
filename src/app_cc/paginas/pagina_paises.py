# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Países"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Pagina Países"
# License: MIT License

import streamlit as st
import modulos.modolo_paises as mp
from paginas.pagina_tratamento import get_data_transformed

def apresentacao_paises(data):
    """
    Este método é responsável por organizar a estrutura da página de apresentação "Países".
    
    Args:
        data = DataFrame
        Normalmente esse DataFrame já vem limpo do arquivo "paginas.pagina_tratamento.py",
        da função "get_data_transformed", cujo é acessado dentro da função app() neste mesmo arquivo.
    
    Esta função não possui retorno
    """
    st.header("Pagina dos paises1")

def app():
    """
    Este método é o responsável por inicializar a página países no Streamlit.
    Ele é chamado pelo arquivos app.py
    
    Essa função não possui nenhum argumento ou retorno.
    """
    st.header("Página dos Países")
    
    data = get_data_transformed()
    
    mp.filtro_lateral(data)
    
    apresentacao_paises(data)