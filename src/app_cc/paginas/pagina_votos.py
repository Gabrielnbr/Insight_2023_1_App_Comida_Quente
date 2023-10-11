import streamlit as st

from paginas.pagina_tratamento import get_data_transformed
import modulos.modulo_votos as mv

# Desenha a página
def apresentacao_votos(data):
    
    st.header('Página de avaliação dos clientes', divider=True)
    
    data = mv.filtro_lateral(data)
    
    # 1º Linha - Inicadores dos votos 
    mv.layout_indicadores(data)
    
    # Linha 2 - votoss x Pais
    mv.layout_pais(data)
    
    # Linha 3 - votos x Cidade
    mv.layout_cidade(data)
    
    # Linha 4 - votoss x Cozinhas
    mv.layout_culinaria(data)
    
    # Linha 5 - Tabelão
    mv.tabelao(data)

# Inicializa a página
def app():
    
    data = get_data_transformed()
    
    apresentacao_votos(data)