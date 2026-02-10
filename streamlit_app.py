import streamlit as st
from supabase import create_client

# 1. TUS LLAVES (Copia y pega aquí lo de Supabase)
URL_DE_SUPABASE = "https://ckvhfbawbcmscrjpsdpa.supabase.co"
KEY_DE_SUPABASE = "sb_publishable_iGxYeTG7SyG4LKBJW7XwlQ_tWFjiffs"

# Conexión con el Cerebro (Base de Datos)
try:
    supabase = create_client(URL_DE_SUPABASE, KEY_DE_SUPABASE)
except Exception as e:
    st.error("Error de conexión: Revisa tus llaves de Supabase")

# Diseño de la Web
st.set_page_config(page_title="La Redera - Ingeniería de Autoridad", page_icon="🕸️")

st.title("🕸️ La Redera")
st.subheader("Sistema de Ingeniería de Autoridad V1.0")
st.markdown("---")

# Leer los datos de la tabla que creaste
try:
    response = supabase.table("nodos_autoridad").select("*").execute()
    nodos = response.data

    if nodos:
        for nodo in nodos:
            with st.expander(f"📍 Claim: {nodo['claim']}", expanded=True):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.write(f"**Entidad:** {nodo['entidad']}")
                    st.write(f"**Evidencia:** [Ver documento o fuente]({nodo['evidencia_url']})")
                
                with col2:
                    if nodo['validado']:
                        st.success("✅ Verificado")
                    else:
                        st.warning("⏳ Pendiente")
                
                # Espacio para el futuro JSON-LD
                if nodo['json_ld']:
                    st.code(nodo['json_ld'], language="json")
    else:
        st.info("La base de datos está conectada pero no tiene nodos. ¡Añade uno en Supabase!")

except Exception as e:
    st.error(f"Hubo un problema al leer los datos: {e}")

st.sidebar.info("Este es un MVP propietario construido con tecnología abierta.")
