import streamlit as st
import numpy as np


def filtro_lateral(data):
    """
    Este método retorna o DataFrame filtrado conforme seleções do usuário.
    
    Args:
        data = Dataframe
    
    Retorno:
        Dataframe filtrado
    """
    
    with st.sidebar:
        
        st.header("Filtros")
        st.subheader("Os filtros devem ser escolhidos na ordem disposta")
        
        multi_pais = st.multiselect('Pais', sorted(set(data['name_country'].unique())))
        if multi_pais != []:
            data = data.loc[data['name_country'].isin(multi_pais)]
        else:
            data = data.copy()
        
        multi_cidade = st.multiselect('Cidade', sorted(set(data['city'].unique())))
        if multi_cidade != []:
            data = data.loc[data['city'].isin(multi_cidade)]
        else:
            data = data.copy()
        
        multi_culinaria = st.multiselect('Tipo de Cozinha', sorted(set(data['cuisines'].unique())))
        if multi_culinaria != []:
            data = data.loc[data['cuisines'].isin(multi_culinaria)]
        else:
            data = data.copy()
        
        slider_valor_min = data['custo_para_dois_corrigido'].min()
        slider_valor_max = data['custo_para_dois_corrigido'].max()
        slide_valor = st.slider("Valor médio para duas pessoas",
                                min_value= slider_valor_min,
                                max_value= slider_valor_max,
                                value=(slider_valor_min,
                                      slider_valor_max)
                                )
        
        data = data[(data['custo_para_dois_corrigido'] >= slide_valor[0]) & (data['custo_para_dois_corrigido'] <= slide_valor[1])]
        
        
        
    return data