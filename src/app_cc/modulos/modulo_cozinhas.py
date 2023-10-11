import streamlit as st
import plotly.express as px

def df_top_cozinhas(data):
    
    st.markdown("### Top 10 Restaurantes")
    
    data = (data.loc[:,['restaurant_id', 'restaurant_name', 'name_country','city', 'cuisines', 'custo_para_dois_corrigido','aggregate_rating','votes']]
            .sort_values(by='aggregate_rating',ascending=False)
            .head(10)
            .reset_index(drop=True))
    st.dataframe(data)

def top_cozinhas(data):
    melhores, piores = st.columns(2)
    
    top_head = (data.loc[:,['cuisines','aggregate_rating','custo_para_dois_corrigido','name_country','city']]
             .groupby('cuisines')
             .agg({'aggregate_rating': 'mean'})
             .sort_values(by='aggregate_rating',ascending=False)
             .head(5)
             .reset_index())
    
    fig_head = px.bar(top_head,
                 x="cuisines",
                 y="aggregate_rating",
                 text="aggregate_rating",
                 text_auto=".2f",
                 title=f"Top 5 Melhores Tipos de Culinárias",
                 labels={"cuisines": "Tipo de Culinária",
                         "aggregate_rating": "Média da Avaliação Média"})
    
    melhores.plotly_chart(fig_head,use_container_width=True)
    
    top_tail = (data.loc[:,['cuisines','aggregate_rating','custo_para_dois_corrigido','name_country','city']]
             .groupby('cuisines')
             .agg({'aggregate_rating': 'mean'})
             .sort_values(by='aggregate_rating',ascending=False)
             .tail(5)
             .reset_index())
    
    fig_tail = px.bar(top_tail,
                 x="cuisines",
                 y="aggregate_rating",
                 text="aggregate_rating",
                 text_auto=".2f",
                 title=f"Top 5 Piores Tipos de Culinárias",
                 labels={"cuisines": "Tipo de Culinária",
                         "aggregate_rating": "Média da Avaliação Média"})
    
    piores.plotly_chart(fig_tail,use_container_width=True)

def filtro_lateral(data):
    with st.sidebar:
        st.header("Filtros Cozinha")
    return data