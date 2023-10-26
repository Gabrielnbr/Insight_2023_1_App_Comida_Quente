# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina Votos"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Pagina Votos".
# License: MIT License

import streamlit            as st
import modulos.modulo_votos as mv

from paginas.pagina_tratamento import get_data_transformed
from modulos.modulo_filtro import filtro_lateral

def apresentacao_votos(data):
    """
    Este método é responsável por organizar a estrutura da página de apresentação "Votos".
    
    Args:
        data = DataFrame
        Normalmente esse DataFrame já vem limpo do arquivo "paginas.pagina_tratamento.py",
        da função "get_data_transformed", cujo é acessado dentro da função app() neste mesmo arquivo.
    
    Esta função não possui retorno
    """
    data = filtro_lateral(data)
    
    # Linha 1 
    mv.layout_indicadores(data)
    
    # Linha 2
    mv.layout_pais(data)
    
    # Linha 3
    mv.layout_cidade(data)
    
    # Linha 4
    mv.layout_culinaria(data)
    
    # Linha 5
    mv.tabelao(data)

def app():
    """
    Este método é o responsável por inicializar a página votos no Streamlit.
    Ele é chamado pelo arquivos app.py
    
    Essa função não possui nenhum argumento ou retorno.
    """
    st.header("Página de Votos")
    
    data = get_data_transformed()
    
    apresentacao_votos(data)