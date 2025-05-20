import requests
from config import LLM_API_URL, LLM_MODEL_NAME

def frage_an_llm(frage, daten):
    prompt = f"Hier sind Garmin-Daten:\n\n{daten}\n\nFrage: {frage}"
    payload = {
        "model": LLM_MODEL_NAME,
        "messages": [
            {"role": "system", "content": "Du bist ein Fitness-Coach und analysierst Gesundheitsdaten."},
            {"role": "user", "content": prompt}
        ]
    }
    try:
        response = requests.post(LLM_API_URL, json=payload)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Fehler bei LLM-Anfrage: {e}"
