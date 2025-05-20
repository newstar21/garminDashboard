import streamlit as st
from core.data_loader import get_today_data
from core.analytics import berechne_kpis
from ui.dashboard import zeige_kpis, zeige_rohdaten
from ui.chat_interface import zeige_chat_interface

st.set_page_config(page_title="Garmin Dashboard", layout="wide")
st.title("🏃 Garmin + LLM Dashboard")

if "garmin_data" not in st.session_state:
    with st.spinner("📡 Garmin-Daten werden geladen..."):
        st.session_state["garmin_data"] = get_today_data()

garmin_data = st.session_state["garmin_data"]
kpis = berechne_kpis(garmin_data)

zeige_kpis(kpis)
zeige_rohdaten(garmin_data)
zeige_chat_interface(garmin_data)
