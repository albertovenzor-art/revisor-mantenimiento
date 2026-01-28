import streamlit as st
import google.generativeai as genai

# CONFIGURACIÓN
st.set_page_config(page_title="Revisor Mantenimiento", page_icon="🛠️")
st.title("🛠️ Revisor Académico de Mantenimiento")

# CONEXIÓN
genai.configure(api_key=st.secrets["GEMINI_KEY"])

SYSTEM_PROMPT = "Eres un Revisor Académico de Mantenimiento. Evalúa el PDF y entrega una tabla de evidencias y calificación."

# INTERFAZ
uploaded_file = st.file_uploader("Cargar Reporte (PDF)", type=["pdf"])

if uploaded_file is not None:
    if st.button("Iniciar Evaluación"):
        try:
            with st.spinner("Analizando..."):
                # CONFIGURACIÓN DEL MODELO
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=SYSTEM_PROMPT
                )
                
                # PROCESAR ARCHIVO
                file_data = uploaded_file.getvalue()
                response = model.generate_content([
                    {"mime_type": "application/pdf", "data": file_data},
                    "Evalúa este documento."
                ])

                st.success("Evaluación Completada")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

