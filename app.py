import streamlit as st
import google.generativeai as genai

# Configuración básica
st.set_page_config(page_title="Revisor Mantenimiento", page_icon="🛠️")
st.title("🛠️ Revisor Académico de Mantenimiento")

# Conexión Segura
API_KEY = st.secrets["GEMINI_KEY"]
genai.configure(api_key=API_KEY)

SYSTEM_PROMPT = """
Eres un Revisor Académico de Proyectos de Mantenimiento Industrial.
Evalúa el PDF y entrega: 1) Tabla de evidencias, 2) Comentarios técnicos, 3) Rúbrica, 4) Calificación (1-10).
"""

uploaded_file = st.file_uploader("Cargar Reporte (PDF)", type=["pdf"])

if uploaded_file is not None:
    if st.button("Iniciar Evaluación"):
        try:
            with st.spinner("Analizando..."):
                # Uso del modelo correcto para la librería 0.8.3
                model = genai.GenerativeModel(
                    model_name="gemini-1.5-flash",
                    system_instruction=SYSTEM_PROMPT
                )
                
                file_data = uploaded_file.getvalue()
                
                response = model.generate_content([
                    {"mime_type": "application/pdf", "data": file_data},
                    "Evalúa este documento."
                ])

                st.success("¡Listo!")
                st.markdown(response.text)
        except Exception as e:
            st.error(f"Error crítico: {e}")
