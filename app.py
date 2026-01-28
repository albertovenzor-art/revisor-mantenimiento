import streamlit as st
import google.generativeai as genai

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Revisor Mantenimiento Industrial", page_icon="🛠️")

st.title("🛠️ Revisor Académico de Mantenimiento")
st.markdown("Sube tu reporte en PDF para recibir una autoevaluación basada en competencias.")

# --- CONEXIÓN CON GEMINI ---
# Sustituye 'TU_API_KEY_AQUI' por la que obtuviste en AI Studio
API_KEY = st.secrets["GEMINI_KEY"] 
genai.configure(api_key=API_KEY)

# --- TU PROMPT DE REVISOR ---
SYSTEM_PROMPT = """
Eres un Revisor Académico de Proyectos de Mantenimiento Industrial, alineado a un modelo educativo por competencias.
Tu objetivo es realizar una AUTOEVALUACIÓN FORMATIVA basada ÚNICAMENTE en el PDF.
Reglas: Si no está la evidencia, marca "No". Usa lenguaje técnico y formativo.
Salida: 1) Tabla de evidencias, 2) Comentarios técnicos, 3) Rúbrica, 4) Calificación (1-10), 5) Retroalimentación.
"""

# --- INTERFAZ DE USUARIO ---
uploaded_file = st.file_uploader("Cargar Reporte Técnico (PDF)", type=["pdf"])

if uploaded_file is not None:
    if st.button("Iniciar Evaluación"):
        try:
            with st.spinner("Analizando documento..."):
                # Configuración del modelo
               # Configuración del modelo
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
                
                # Preparar el archivo para Gemini
                file_data = uploaded_file.getvalue()
                
                # Generar contenido
                response = model.generate_content([
                    {"mime_type": "application/pdf", "data": file_data},
                    "Por favor, evalúa este reporte técnico según las instrucciones de sistema."
                ])
                
                st.success("Evaluación Completada")
                st.markdown("---")
                st.markdown(response.text)
                
        except Exception as e:
            st.error(f"Hubo un error: {e}")


st.sidebar.info("Herramienta docente para apoyo académico.")



