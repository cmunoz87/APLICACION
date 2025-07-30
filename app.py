import streamlit as st
import requests

st.title("Formulario Streamlit conectado a Google Sheets (Apps Script)")

# URL del Web App de Google Apps Script
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzoNhl7nQsiEKjnyE2mS9VSotNmhuurDKSfyk5AJ0v5Ol7ahdwKzg_AcnkNtLjbZNS8-w/exec"

with st.form("formulario"):
    nombre = st.text_input("Nombre")
    email = st.text_input("Correo electrónico")
    mensaje = st.text_area("Mensaje")
    enviado = st.form_submit_button("Enviar")

    if enviado:
        data = {"nombre": nombre, "email": email, "mensaje": mensaje}
        response = requests.post(WEB_APP_URL, json=data)
        if response.status_code == 200:
            st.success("Datos enviados correctamente a Google Sheets")
        else:
            st.error("Error al enviar los datos")
