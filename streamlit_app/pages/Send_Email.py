import streamlit as st
import subprocess
import sys
import os

st.set_page_config(page_title="Garmin Report Sender", page_icon="📧")

st.title("📧 Garmin Wochenbericht senden")

st.write("Drücke den Button, um den aktuellen Garmin-Bericht zu erzeugen und per E-Mail zu versenden.")

# Pfad zu deinem Python-Script
script_path = os.path.join(os.getcwd(), "garmin_report.py")  # anpassen, falls das Script anders heißt

if st.button("E-Mail senden 🚀"):
    with st.spinner("Bericht wird erstellt und E-Mail wird gesendet..."):
        try:
            # Script ausführen
            result = subprocess.run(
                [sys.executable, script_path],
                capture_output=True,
                text=True,
                check=True
            )
            st.success("✅ Garmin Maximalbericht erfolgreich gesendet!")
            st.code(result.stdout)
        except subprocess.CalledProcessError as e:
            st.error("❌ Fehler beim Senden des Berichts.")
            st.code(e.stderr)
