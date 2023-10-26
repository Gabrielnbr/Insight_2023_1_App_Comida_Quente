import streamlit as st

def filtro_lateral(data):
    """
    Este método retorna o DataFrame filtrado conforme seleções do usuário.
    
    Args:
        data = Dataframe
    
    Retorno:
        Dataframe filtrado
    """
    
    st.header("Filtros")
    
    with st.sidebar:
        
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
            
    return data