import pandas as pd

def get_sample_data():
    # Beispielhafte Dummy-Daten als Platzhalter für echte Garmin-Daten
    data = {
        "Datum": pd.date_range(start="2025-01-01", periods=7),
        "Schritte": [10000, 8500, 12000, 9000, 11000, 7500, 10500],
        "Kalorien": [300, 250, 350, 270, 320, 220, 310],
        "Distanz (km)": [7.5, 6.0, 8.2, 6.8, 7.9, 5.4, 7.6],
    }
    df = pd.DataFrame(data)
    return df
