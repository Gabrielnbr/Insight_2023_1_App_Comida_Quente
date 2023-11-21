# Autor: Gabriel Nobre
# Data: 20 de Novembro de 2023
# Descrição: Este é um arquivo Python que contém funções relacionadas à página "Home Page"
# no aplicativo Streamlit. Ele define a estrutura da página, bem como a inicialização
# da página "Home Page"
# License: MIT License

import streamlit as st

def apredentacao_geral():
    apresentacao = '''
    <p>Este dashborad surgiu do pedido do novo gestor da área de negócios cujo gostaria de entender como a empresa está atuamente.</p>
    <p>Desta forma, fiquei responsável por construir e orientar o novo gestor na utilização deste dashboard.</p>
    '''
    
    st.write(apresentacao, unsafe_allow_html= True)


def estrutura_dashboard():
    st.subheader("Estrutura do dashboard", divider= "green")
    estrutura = '''
    <p>Este dashboard é dividio em 4 partes:</p>
    <dl>
		<dt>Idicadores Gerais</dt>
		<dd>
			<p>Nesta página apresento os indicadores gerais da empresa e um mapa com a localização de cada restaurante cadastrado.</br>
            Para cada restaurante haverá um ponto mostrando os 3 principais elementos:
            <ul>
                <li>Preço médio dos pratos para dois.</li>
                <li>Tipo principal de comida oferecida pelo restaurante.</li>
                <li>Classificação.</li>
            </ul>
            </p>
		</dd>
		<dt>Página Paises</dt>
		<dd>
			<p>Nesta página é feito uma segmentação por paises.</p>
		</dd>
		<dt>Página Cidades</dt>
		<dd>
			<p>Nesta página é feito uma segmentação por cidades.</p>
		</dd>
  		<dt>Página Cozinhas</dt>
		<dd>
			<p>Nesta página é feito uma segmentação por cozinhas.</p>
		</dd>
	</dl>
    <p>O Dashboard foi construido com 4 filtros, no qual permitirá a mesma seleção de filtros sobre todas as telas, os filtros são:</p>
	<ol>
		<li>Países.</li>
		<li>Cidades</li>
		<li>Cozinhas</li>
		<li>Valor do prato para dois</li>
	</ol>
    <p>Por fim, caso o gestor queira fazer o download da base de dados com os filtros selecionados,
    ele poderá fazer apertando o botão "Download DataBase" ao final da área dos filtros.</p>
    '''
    
    st.write(estrutura, unsafe_allow_html= True)

def contato():
    st.subheader("Contato",divider= "orange")
    
    contato = '''                                                                                                                                                  
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">                                                                                                    

    <p><i class="fa-solid fa-folder-tree"></i><a href="https://gabrielnbr.github.io/portfolio/"> Portfólio de Projetos</a></p>
    <p><i class="fa-brands fa-linkedin"></i><a href="https://www.linkedin.com/in/gabriel-nobre-galvao/"> Linkedin</a></p>
    <p><i class="fa-brands fa-medium"></i><a href="https://medium.com/@gabrielnobregalvao"> Medium</a></p>
    <p><i class="fa-brands fa-github"></i><a href="https://github.com/Gabrielnbr"> Git Hub</a></p>
    <p><i class="fa-solid fa-envelope"></i><a href="mailto:gabrielnobregalvao@gmail.com"> E-mail</a></p>
    '''
    st.write(contato, unsafe_allow_html=True)