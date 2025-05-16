import streamlit as st
from garminconnect import Garmin
from datetime import datetime, timedelta
import pandas as pd
import plotly.express as px

# Anmeldung über Secrets
email = st.secrets["email"]
password = st.secrets["password"]

# Garmin-Login
try:
    client = Garmin(email, password)
    client.login()
except Exception as e:
    st.error(f"Fehler beim Login: {e}")
    st.stop()

# Aktivitäten abrufen (letzte 30)
activities = client.get_activities(0, 30)

# In DataFrame umwandeln
data = []
for activity in activities:
    start = datetime.strptime(activity["startTimeLocal"], "%Y-%m-%d %H:%M:%S")
    duration_minutes = round(activity["duration"] / 60, 2)
    sport = activity["activityType"]["typeKey"]
    data.append({"Datum": start.date(), "Sport": sport, "Dauer (Minuten)": duration_minutes})

df = pd.DataFrame(data)

# Nur letzte 7 Tage
heute = datetime.now().date()
letzte_woche = heute - timedelta(days=6)
df7 = df[df["Datum"] >= letzte_woche]

# Sportzeit summieren
gesamt_minuten = df7["Dauer (Minuten)"].sum()
gesamt_stunden = round(gesamt_minuten / 60, 2)

st.title("🏋️ Garmin Sport Dashboard")
st.subheader("Sportzeit der letzten 7 Tage")
st.metric("🕒 Gesamte Zeit", f"{gesamt_stunden} Stunden")

# Diagramm: Sportdauer pro Tag
df_grouped = df7.groupby("Datum")["Dauer (Minuten)"].sum().reset_index()
fig = px.bar(df_grouped, x="Datum", y="Dauer (Minuten)", title="Sportzeit pro Tag")
st.plotly_chart(fig)

# Optional: Tabelle anzeigen
with st.expander("📋 Alle Aktivitäten der letzten 7 Tage"):
    st.dataframe(df7)
