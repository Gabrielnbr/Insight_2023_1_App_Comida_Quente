# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Cidades"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Pagina Cidades"
# License: MIT License

import streamlit as st
import modulos.modulo_cidades as mc
import modulos.modulo_filtro as mf
from paginas.pagina_tratamento import get_data_transformed

def apresentacao_cidades(data):
    """
    Este método é responsável por organizar a estrutura da página de apresentação "Cidades".
    
    Args:
        data = DataFrame
        Normalmente esse DataFrame já vem limpo do arquivo "paginas.pagina_tratamento.py",
        da função "get_data_transformed", cujo é acessado dentro da função app() neste mesmo arquivo.
    
    Esta função não possui retorno
    """
    
    data = mf.filtro_lateral(data)
    
    mc.cidade_restaurante_graph(data)
    
    mc.min_max_restaurante_cidade(data)

def app():
    """
    Este método é o responsável por inicializar a página cidades no Streamlit.
    Ele é chamado pelo arquivos app.py
    
    Essa função não possui nenhum argumento ou retorno.
    """
    st.header('Página das Cidade', divider= True)
    
    data = get_data_transformed()
    
    apresentacao_cidades(data)  