import pandas as pd

def get_rating_text():
    
    '''
    Este método retorna um DataFrame com duas colunas.
    A primeira é a avaliação textual nas linguas originais
    A segunda é a tradução e a readequação em escala para a língua portuguesa.
    '''
    
    mudanca_rating_text = { 'Rating text': ['Average', 'Baik', 'Bardzo dobrze', 'Biasa', 'Bom', 'Bueno', 'Buono', 'Eccellente', 'Excelente', 'Excellent', 'Good', 'Harika', 'Muito Bom', 'Muito bom', 'Muy Bueno', 'Not rated', 'Poor', 'Sangat Baik', 'Skvělá volba', 'Skvělé', 'Terbaik', 'Velmi dobré', 'Very Good', 'Veľmi dobré', 'Vynikajúce', 'Wybitnie', 'Çok iyi', 'İyi'],
                            'Avalicao texto': ['Normal', 'Bom', 'Muito bom', 'Normal', 'Bom', 'Bom', 'Bom', 'Excelente', 'Excelente', 'Excelente', 'Bom', 'Muito Bom', 'Muito Bom', 'Muito Bom', 'Muito Bom', 'Não Avaliado', 'Ruim', 'Muito Bom', 'Excelente', 'Muito Bom', 'Excelente', 'Muito Bom', 'Muito Bom', 'Muito Bom', 'Excelente', 'Excelente', 'Muito Bom', 'Bom']}
    mudanca_rating_text = pd.DataFrame(mudanca_rating_text)
    return mudanca_rating_text

def get_rating_collors():
    '''
    Este método retorna um Dataframe com duas colunas.
    A primeira é o valor em hexa decimal das cores.
    A segunda é o nome das cores.
    '''
    
    cores_hex = {"Rating color": ["3F7E00", "5BA829", "9ACD32", "CDD614", "FFBA00", "CBCBC8", "FF7800"],
                "Nome cor": ["Verde Escuro", "Verde", "Verde Claro", "Laranja", "Vermelho", "Cinza Claro", "Vermelho Escuro"]}
    cores_hex = pd.DataFrame(cores_hex)
    return cores_hex