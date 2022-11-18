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
# Muestra del Excel que se tiene que subir
st.markdown("""
### Formato para la Tabla:
| Cement | Blast Furnace Slag | Fly Ash | Water | Super-plasticizer | Coarse Aggregate | Fine Aggregate | Age | Strength of the Cement |
|--------|--------------------|---------|-------|-------------------|------------------|----------------|-----|------------------------|
| 540.0  | 0.0                | 0.0     | 162.0 | 2.5               | 1040.0           | 676.0          | 28  | 79.99                  |
""")

# objeto que carga el Archivo excel solicitado
uploaded_file = st.file_uploader("Subir el Archivo CSV")

# Cuando el archivo sea subido iniciamos con el proceso de predicción
if uploaded_file is not None:
    # Cargando el Excel que se suba
    carga = pd.read_excel(uploaded_file)
    # Mostrando el Dataset
    st.write('Esto fue lo que se subió...')
    st.write(carga)
    # Seleccionando las variables seleccionadas
    df = carga[["Cement", "Water", "Superplasticizer", "Age"]]

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
        df_final = pd.concat([carga, pred], axis=1)

        # Mostrando la Predicción
        st.write("Predicción:")
        st.write(df_final)
