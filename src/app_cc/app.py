# ============
# 0 Imports
# ============
import streamlit as st
from multiapp import MultiApp
from paginas import home_page, pagina_cidades, pagina_cozinhas, pagina_paises, pagina_tratamento, pagina_votos

st.set_page_config( layout='wide' )

app = MultiApp()

# Inicialização do app
app.add_app("4. Página Paises",pagina_cozinhas.app )
app.add_app("4. Página Cidades",pagina_cozinhas.app )
app.add_app("4. Página Cozinhas",pagina_cozinhas.app )
app.add_app("3. Home Page",home_page.app )
app.add_app("1. Pagina Inicial",pagina_tratamento.app)
app.add_app("2. Pagina Votos",pagina_votos.app)


# Main app
app.run()