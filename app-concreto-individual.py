# Librerías
import time
import joblib
import pandas as pd
from PIL import Image
import streamlit as st
image = Image.open(r'.\Data\Logo.png')

# Agregando una imagen y el título
st.title("Calculadora de Resistencia para Mezclas de Concreto")
st.write("---")

# Presentación de la aplicación
st.markdown("""
#### Integrantes:
- Cárdenas Gallardo Paula Daniela | 733720
- Haces López José Manuel | 734759
- Martin Vázquez Misael | 721908
- Villa Domínguez Paulo Adrián | 733773

**Aprendizaje Máquina | Juan Antonio Vega Fernández** 

Jueves 24 de Noviembre 2022
""")
st.image(image)

st.write("---")


def user_input_features():
    cement = st.sidebar.slider("Cement", 102.0, 272.0, 540.0)  # Nombre, Mínimo, Máximo, Default
    water = st.sidebar.slider("Water", 121.80, 185.0, 247.0)
    superplaticizer = st.sidebar.slider("Superplaticizer", 0.0, 6.4, 32.2)
    age = st.sidebar.slider("Age", 1, 28, 365)
    data = {
        "cement": cement,
        "water": water,
        "superplaticizer": superplaticizer,
        "age": age
    }
    features = pd.DataFrame(data, index=[0])
    return features


# Df con los inpts
df = user_input_features()
st.subheader("User input parameters")
st.write(df)

if st.button("Predecir"):
    # Mostrando la barra de carga para la predicción
    st.write("---")
    st.write("Cargando la Predicción...")
    loading = st.progress(0)
    # cargando el Modelo
    model = joblib.load(r'.\model\rf_regressor.pkl')
    # Haciendo la Predicción
    pred = model.predict(df)

    # Moviendo la barra de carga hasta que termine
    for percent_complete in range(100):
        time.sleep(0.01)
        loading.progress(percent_complete + 1)
    time.sleep(1.5)

    # Dandole formato al Df final
    pred = pd.DataFrame(pred)
    pred.rename(columns={0: 'Predicción_Strength'}, inplace=True)
    df_final = pd.concat([df, pred], axis=1)

    # Mostrando la Predicción
    st.write("Predicción:")
    st.write(df_final)
