# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina de Tratamentos"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Pagina de Tratamentos"
# License: MIT License

import pandas       as pd
import streamlit    as st

import inflection

from modulos import tratamento_numerico     as tn
from modulos import tratamento_categorico   as tc

def get_data_raw():
    data = pd.read_csv('src/data/raw/zomato.csv')
    return data

def sem_duplicadas(data):
    return data.drop_duplicates(subset='Restaurant ID')

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
    data = data.loc[data['Custo para dois corrigido'] < 10000,:]
    
    return data

# Retirando as colunas numéricas que não precisarão ser utilizadas
def drop_colunas_numericas(data):
    colunas_numerica_drop = ['Average Cost for two', 'Switch to order menu', 'Indice de correcao']
    data = data.drop( columns = colunas_numerica_drop)
    return data

# Criação de nova coluna para cozinhas com 1 único atributo
def valor_unico_cosinha(data):
    data["Cuisines"].fillna('Cozinha não encontrada', inplace=True)
    data["cuisines"] = data.loc[:, "Cuisines"].astype(str).apply(lambda x: x.split(",")[0])
    return data

# 
def avaliacao_texto_ptbr(data):
    mudanca_rating_text = tc.get_rating_text()
    data = data.merge(mudanca_rating_text, on='Rating text', how='inner')
    return data

# 
def nome_cores(data):
    cores = tc.get_rating_collors()
    data = data.merge(cores, on='Rating color', how='inner')
    return data

# 
def drop_colunas_categoricas(data):
    colunas_categoricas_drop = ['Cuisines', 'Rating text']
    data = data.drop( columns = colunas_categoricas_drop)
    return data

def ajuste_colunas(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

# Inicialização da página do aplicativo
def app():
    
    st.title("Teste dos tratamentos")
    
    data = get_data_transformed()
    
    #colocar os métodos desta página
    st.dataframe(data)

def get_data_transformed():
    
    #Local dos dados
    data = get_data_raw()
    data = sem_duplicadas(data)
    
    #Métodos para tratamento de valores numéricos
    data = paises(data)
    data = conversao_currency(data)
    data = drop_colunas_numericas(data)
    
    #Métodos para tratamento de valores categóricos
    data = valor_unico_cosinha(data)
    data = avaliacao_texto_ptbr(data)
    data = nome_cores(data)
    data = drop_colunas_categoricas(data)
    
    data = ajuste_colunas(data)
    
    return data