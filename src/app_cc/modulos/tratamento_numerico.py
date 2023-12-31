# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina de Tratamentos"
# no aplicativo Streamlit. Ele define as funções que serão utilizadas pelo arquivo "pagina_tratamentos.py"
# para tratamentos de valores numéricos no Dataframe.
# License: MIT License

import pandas as pd

def get_coluna_paises():
    
    '''
    Esse função gera um DataFrame com duas colunas,
    cujo correlaciona o código numérico de países com os seus respectivos nomes.
    A primeira coluna é o código do pais.
    A segunda coluna é o nome do pais.
    
    Essa função não possui argumentos
    
    Return:
        Dataframe gerado.
    '''
    
    paises = { 'Country Code':[ 1, 14, 30, 37, 94, 148, 162, 166, 184, 189, 191, 208, 214, 215, 216],
                'Name Country':[ "India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar", "Singapure", "South Africa", "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America"]}
    paises = pd.DataFrame(paises)  
    
    return paises

def get_indice_correcao():
    
    '''
    Este função gera um DataFrame com duas colunas,
    cujo relaciona o nome da moeda em linguagem natural com o valor dela referênciano o valor
    base sendo o Real R$ Brasileiro com o valor 1. Com essa informação atualizada no dia 01/10/2023.
    A primeira coluna é o nome da moeda.
    A segunda coluna é o indice de correnção para a moeda brasileira atualizada no dia 01/10/2023.
    
    Essa função não possui argumentos
    
    Return:
        Dataframe gerado.
    '''
    
    conversao_moeda = {'Currency': ['Brazilian Real(R$)', 'Botswana Pula(P)', 'Dollar($)', 'Emirati Diram(AED)','Indian Rupees(Rs.)', 'Indonesian Rupiah(IDR)', 'NewZealand($)', 'Pounds(£)', 'Qatari Rial(QR)', 'Rand(R)', 'Sri Lankan Rupee(LKR)', 'Turkish Lira(TL)'],
                'Indice de correcao': [1, 2.75, 0.2, 0.74, 16.83, 3117.62, 0.33, 0.16, 0.73, 3.80, 65.68, 5.50]}
    conversao_moeda = pd.DataFrame(conversao_moeda) 
    
    return conversao_moeda