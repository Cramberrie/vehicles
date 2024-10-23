import streamlit as st
import pandas as pd
import plotly.express as px


st. header("Grafico de burbujas para venta de coches")
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.button('Construir grafico de burbujas')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de burbujas para el conjunto de datos de anuncios de venta de coches')

    # crear un grafico de burbujas
    fig = px.scatter(car_data.query("transmission=='manual'"),
                     x="odometer",
                     y="model_year",
                     size="price",
                     color="condition",
                     hover_name="model",
                     log_x=False,
                     size_max=60)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
