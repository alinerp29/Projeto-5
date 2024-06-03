import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')

#dados_separados=car_data[car_data].str.split(",",expand=True)

st.header('Quatro rodas', divider='rainbow') 
st.header ('Conheça mais sobre nossos veículos')

hist_button = st.button('Conheça mais sobre nossos veículos que passaram por nossas lojas.') # criar um botão
if hist_button: # se o botão for clicado
    fig = px.histogram(car_data, x="days_listed")
    st.plotly_chart(fig, use_container_width=True)


hist_button = st.button('Grandes oportunidade!  Vejam os carros questão a venda em nossa loja.') # criar um botão
if hist_button:     
    fig = px.scatter(car_data, x="model_year", y="price") # criar um gráfico de dispersão
    fig.show() # exibindo