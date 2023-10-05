import pandas as pd

class TratamentoNumerico:
    
    '''
    Classe referente a todo o tratemento das colunas numéricas do DataFrame
    '''
    
    def get_coluna_paises():
        
        '''
        Esse método retorna um DataFrame com duas colunas.
        A primeira coluna é o código do pais.
        A segunda coluna é o nome do pais.
        
        Exemplo:
        coluna_paises = {'Country Code':[ 1, 14, 30], 'Name Country':[ "India", "Australia", "Brazil"]}
        df = pd.DataFrame(coluna_paises)
        '''
        
        paises = { 'Country Code':[ 1, 14, 30, 37, 94, 148, 162, 166, 184, 189, 191, 208, 214, 215, 216],
                    'Name Country':[ "India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines", "Qatar", "Singapure", "South Africa", "Sri Lanka", "Turkey", "United Arab Emirates", "England", "United States of America"]}
        paises = pd.DataFrame(paises)  
        
        return paises

    def get_indice_correcao():
        '''
        Este método retorna um DataFrame com duas colunas.
        A primeira coluna é o nome da moeda.
        A segunda coluna é o indice de correnção para a moeda brasileira atualizada no dia 01/10/2023.
        
        Exemplo:
        conversao_moeda = {'Currency': ['Brazilian Real(R$)', 'Botswana Pula(P)', 'Dollar($)'], 'Indice de correcao': [1, 2.75, 0.2]}
        conversao_moeda = pd.DataFrame(conversao_moeda)
        '''
        
        
        conversao_moeda = {'Currency': ['Brazilian Real(R$)', 'Botswana Pula(P)', 'Dollar($)', 'Emirati Diram(AED)','Indian Rupees(Rs.)', 'Indonesian Rupiah(IDR)', 'NewZealand($)', 'Pounds(£)', 'Qatari Rial(QR)', 'Rand(R)', 'Sri Lankan Rupee(LKR)', 'Turkish Lira(TL)'],
                    'Indice de correcao': [1, 2.75, 0.2, 0.74, 16.83, 3117.62, 0.33, 0.16, 0.73, 3.80, 65.68, 5.50]}
        conversao_moeda = pd.DataFrame(conversao_moeda) 
        
        return conversao_moeda