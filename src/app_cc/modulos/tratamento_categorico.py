# Autor: Gabriel Nobre
# Data: 25 de Outubro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Pagina de Tratamentos"
# no aplicativo Streamlit. Ele define as funções que serão utilizadas pelo arquivo "pagina_tratamentos.py"
# para tratamentos de valores categóricos no Dataframe.
# License: MIT License

import pandas as pd

def get_rating_text():
    
    '''
    Esta função gera um DataFrame com duas colunas,
    com o ojetivo correlacionar palavras de linguagem estrangeira para linguegem PT-BR.
    A primeira é a avaliação textual nas linguas originais
    A segunda é a tradução e a readequação em escala para a língua portuguesa.
    
    Essa função não possui argumentos
    
    Return:
        Dataframe.
    '''
    
    mudanca_rating_text = { 'Rating text': ['Average', 'Baik', 'Bardzo dobrze', 'Biasa', 'Bom', 'Bueno', 'Buono', 'Eccellente', 'Excelente', 'Excellent', 'Good', 'Harika', 'Muito Bom', 'Muito bom', 'Muy Bueno', 'Not rated', 'Poor', 'Sangat Baik', 'Skvělá volba', 'Skvělé', 'Terbaik', 'Velmi dobré', 'Very Good', 'Veľmi dobré', 'Vynikajúce', 'Wybitnie', 'Çok iyi', 'İyi'],
                            'Avalicao texto': ['Normal', 'Bom', 'Muito bom', 'Normal', 'Bom', 'Bom', 'Bom', 'Excelente', 'Excelente', 'Excelente', 'Bom', 'Muito Bom', 'Muito Bom', 'Muito Bom', 'Muito Bom', 'Não Avaliado', 'Ruim', 'Muito Bom', 'Excelente', 'Muito Bom', 'Excelente', 'Muito Bom', 'Muito Bom', 'Muito Bom', 'Excelente', 'Excelente', 'Muito Bom', 'Bom']}
    mudanca_rating_text = pd.DataFrame(mudanca_rating_text)
    return mudanca_rating_text

def get_rating_collors():
    '''
    Esta função gera um Dataframe com duas colunas,
    com o objetivo de correlacionar o valor da cor de hexadecimal em linguegem natural PT-BR.
    A primeira é o valor em hexadecimal das cores.
    A segunda é o nome das cores.
    
    Essa função não possui argumentos
    
    Return:
        Dataframe.
    '''
    
    cores_hex = {"Rating color": ["3F7E00", "5BA829", "9ACD32", "CDD614", "FFBA00", "CBCBC8", "FF7800"],
                "Nome cor": ["Verde Escuro", "Verde", "Verde Claro", "Laranja", "Vermelho", "Cinza Claro", "Vermelho Escuro"]}
    cores_hex = pd.DataFrame(cores_hex)
    return cores_hex