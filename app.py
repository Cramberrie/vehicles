import streamlit as st
import pandas as pd
import plotly.express as px


st. header("Grafico de conjunto de datos para venta de coches")
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.checkbox('Construir histograma')  # crear un botón
scatter_button = st.checkbox('Construir grafico de burbujas')

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para coches con transmision automatica')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un grafico de burbujas para coches con transmision manual')

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
