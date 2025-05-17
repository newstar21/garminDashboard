import pandas as pd
import streamlit as st
from garmin.client import GarminClient
from garminconnect import *  # Ersetze durch deinen realen API-Wrapper


def main():
    st.title("Garmin Tennis Dashboard")
    st.write("Visualisierung der Herzfrequenz und Trainingseffekte der letzten Tennis-Sessions")

    st.sidebar.header("Login")
    email = st.sidebar.text_input("E-Mail")
    password = st.sidebar.text_input("Passwort", type="password")

    if st.sidebar.button("Daten laden"):
        # 1. Login und Daten holen
        client = GarminClient(api=Garmin(email=email, password=password))
        client.login()
        tennis_data = client.get_parsed_tennis_activities()

        if not tennis_data:
            st.warning("Keine Tennisdaten gefunden.")
            return

        # 2. In DataFrame umwandeln
        df = pd.DataFrame(tennis_data)
        df["start_time_local"] = pd.to_datetime(df["start_time_local"])
        df = df.sort_values(by="start_time_local")

        # 3. Tabelle anzeigen
        st.subheader("Letzte Tennis-Sessions")
        st.dataframe(df[["start_time_local", "avg_hr", "training_effect_aerob", "training_effect_anaerob"]])

        # 4. Chart anzeigen
        st.subheader("Entwicklung: Herzfrequenz & Trainingseffekt")
        st.line_chart(df.set_index("start_time_local")[["avg_hr", "training_effect_aerob", "training_effect_anaerob"]])

    else:
        st.info("Bitte Login-Daten eingeben und 'Daten laden' klicken.")


if __name__ == "__main__":
    main()
