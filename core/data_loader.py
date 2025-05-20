from garminconnect import Garmin
from config import GARMIN_EMAIL, GARMIN_PASSWORD
import datetime

def get_garmin_client():
    client = Garmin(GARMIN_EMAIL, GARMIN_PASSWORD)
    client.login()
    return client

def get_today_data():
    client = get_garmin_client()
    today = datetime.date.today()
    return {
        "steps": client.get_steps_data(today),
        "sleep": client.get_sleep_data(today),
        "stress": client.get_stress_data(today),
        "heart_rate": client.get_heart_rates(today.isoformat())
    }
