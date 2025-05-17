import altair as alt
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def plot_tennis_activity(df: pd.DataFrame):
    """
    Erwartet ein DataFrame mit mindestens diesen Spalten:
    - date (Datum der Aktivität)
    - average_heart_rate
    - aerobic_training_effect
    - anaerobic_training_effect
    """

    # Basislinie mit Datum auf der X-Achse
    base = alt.Chart(df).encode(
        x='date:T'
    )

    # Linien für verschiedene Werte
    heart_rate_line = base.mark_line(point=True, color='red').encode(
        y='average_heart_rate:Q',
        tooltip=['date', 'average_heart_rate']
    ).properties(
        title='Durchschnittliche Herzfrequenz (bpm)'
    )

    aerobic_line = base.mark_line(point=True, color='green').encode(
        y='aerobic_training_effect:Q',
        tooltip=['date', 'aerobic_training_effect']
    ).properties(
        title='Aerober Trainingseffekt'
    )

    anaerobic_line = base.mark_line(point=True, color='blue').encode(
        y='anaerobic_training_effect:Q',
        tooltip=['date', 'anaerobic_training_effect']
    ).properties(
        title='Anaerober Trainingseffekt'
    )

    # Wir wollen alle 3 Linien in einem Chart, also mit Mehrfach-Achsen. Altair unterstützt das mit "layer".
    chart = alt.layer(
        heart_rate_line, aerobic_line, anaerobic_line
    ).resolve_scale(
        y='independent'  # separate Y-Achsen für bessere Sichtbarkeit
    ).properties(
        width=700,
        height=400,
        title='Tennis Aktivitäten - Herzfrequenz & Trainingseffekt über Zeit'
    )

    return chart