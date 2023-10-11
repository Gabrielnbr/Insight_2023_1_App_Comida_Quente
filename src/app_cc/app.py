# ============
# 0 Imports
# ============
import streamlit as st
from multiapp import MultiApp
from paginas import pagina_votos, home_page, pagina_tratamento, pagina_cozinhas

st.set_page_config( layout='wide' )

app = MultiApp()

# Inicialização do app
app.add_app("4. Página Cozinhas",pagina_cozinhas.app )
app.add_app("3. Home Page",home_page.app )
app.add_app("1. Pagina Inicial", pagina_tratamento.app)
app.add_app("2. Pagina Votos",pagina_votos.app)


# Main app
app.run()