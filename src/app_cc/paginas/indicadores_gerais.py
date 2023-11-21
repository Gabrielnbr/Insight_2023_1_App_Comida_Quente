# Autor: Gabriel Nobre
# Data: 20 de Novembro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Indicadores gerais"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Indicadores gerais"
# License: MIT License

import streamlit as st
from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_filtro as mf
import modulos.modulo_indicadores_gerais as mig

def apresentacao_home(data):
    """
    Este método é responsável por organizar a estrutura da página de apresentação "Indicadores gerais".
    
    Args:
        data = DataFrame
        Normalmente esse DataFrame já vem limpo do arquivo "paginas.pagina_tratamento.py",
        da função "get_data_transformed", cujo é acessado dentro da função app() neste mesmo arquivo.
    
    Esta função não possui retorno
    """
    st.header('Indicadores Gerais', divider=True)
    
    data = mf.filtro_lateral(data)
    
    mig.indicadores(data)
    
    mig.map(data)

def app():
    """
    Este método é o responsável por inicializar a página "Indicadores gerais" no Streamlit.
    Ele é chamado pelo arquivo "app.py" 
    
    Essa função não possui nenhum argumento ou retorno.
    """
    data = get_data_transformed()
    
    apresentacao_home(data)