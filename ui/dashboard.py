import streamlit as st
import plotly.graph_objects as go

def zeige_kpis(kpis):
    st.subheader("📊 Tägliche Kennzahlen")
    for key, value in kpis.items():
        st.metric(key, value)

def zeige_rohdaten(data):
    with st.expander("📂 Rohdaten anzeigen"):
        st.json(data)
