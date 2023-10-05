# ============
# 0 Imports
# ============
import streamlit as st
from multiapp import MultiApp
from paginas import pagina_clientes, pagina_entregadores, pagina_restaurantes, pagina_tratamento

st.set_page_config( layout='wide' )

app = MultiApp()

# Inicialização do app
app.add_app("1. Pagina Inicial", pagina_tratamento.app())
app.add_app("2. Pagina nada",pagina_clientes.app() )
#app.add_app("", )
#app.add_app("", )

# Main app
app.run()