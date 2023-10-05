import inflection
import datetime
import pickle

import pandas       as pd
import numpy        as np
import streamlit    as st

from paginas.tratamento_numerico import TratamentoNumerico as tn

def get_data():
    data = pd.read_csv('src/data/raw/zomato.csv')
    return data

# Acrescentando coluna com o nome dos países
def paises(data):
    df_paises = tn.get_coluna_paises()
    data = data.merge(df_paises, on='Country Code', how='inner')
    return data

# Atualizando valor da moeda com base no indice de correcao
def conversao_currency(data):
    
    df_indice_correcao = tn.get_indice_correcao()
    data = data.merge(df_indice_correcao, on='Currency', how='inner')
    
    data['Custo para dois corrigido'] = data.apply(lambda x : round( x['Average Cost for two'] / x['Indice de correcao'],2), axis =1)
    return data

# Retirando as colunas numéricas que não precisarão ser utilizadas
def drop_colunas_numericas(data):
    colunas_numerica_drop = ['Average Cost for two', 'Switch to order menu', 'Indice de correcao']
    data = data.drop( columns = colunas_numerica_drop)
    return data

# Inicialização da página do aplicativo
def app():
    
    data = get_data()
    data = paises(data)
    data = conversao_currency(data)
    data = drop_colunas_numericas(data)
    
    #colocar os métodos desta página
    st.dataframe(data)