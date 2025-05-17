from .parser import DataParserHelper


class GarminClient:
    def __init__(self, api):
        self.api = api  # z.B. Garmin(email, password)

    def login(self):
        self.api.login()  # Authentifiziert intern, kein Rückgabewert nötig

    def get_raw_activities(self):
        return self.api.get_activities(10)  # nur letzte 10

    def get_parsed_tennis_activities(self):
        raw_activities = self.get_raw_activities()
        tennis_activities = list(filter(lambda a: a.get("activityType", {}).get("typeKey") == "tennis_v2", raw_activities))
        return [DataParserHelper.parseTennisActivities(a) for a in tennis_activities]
