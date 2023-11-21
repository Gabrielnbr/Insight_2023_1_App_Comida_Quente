# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Cozinhas"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Pagina Cozinhas"
# License: MIT License

import streamlit as st
import modulos.modulo_cozinhas as mc
import modulos.modulo_filtro as mf
from paginas.pagina_tratamento import get_data_transformed

def apresentacao_cozinhas(data):
    """
    Este método é responsável por organizar a estrutura da página de apresentação "Cozinhas".
    
    Args:
        data = DataFrame
        Normalmente esse DataFrame já vem limpo do arquivo "paginas.pagina_tratamento.py",
        da função "get_data_transformed", cujo é acessado dentro da função app() neste mesmo arquivo.
    
    Esta função não possui retorno
    """
    st.header('Página de Cozinhas', divider=True)
    
    data = mf.filtro_lateral(data)
    
    mc.df_top_cozinhas(data)
    
    mc.top_cozinhas(data)
    
def app():
    """
    Este método é o responsável por inicializar a página cozinhas no Streamlit.
    Ele é chamado pelo arquivos app.py
    
    Essa função não possui nenhum argumento ou retorno.
    """
    data = get_data_transformed()
    
    apresentacao_cozinhas(data)