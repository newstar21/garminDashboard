def berechne_kpis(data):
    schritte = sum(d.get("steps", 0) for d in data.get("steps", []))
    # du kannst weitere Kennzahlen hier ergänzen
    return {
        "Schritte": schritte,
        "Schlafdaten vorhanden": "summaryId" in data.get("sleep", {}),
        "Stresslevel-Einträge": len(data.get("stress", []))
    }
