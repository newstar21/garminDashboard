import unittest
from unittest.mock import MagicMock
from dashboard.garmin.client import GarminClient, DataParserHelper  # Ersetze your_module durch den Modulnamen


class TestGarminClient(unittest.TestCase):
    def setUp(self):
        # Mock API-Objekt
        self.mock_api = MagicMock()

        # Beispiel-Rohdaten (inkl. Tennis- und Nicht-Tennis-Aktivitäten)
        self.raw_activities = [
            {
                "activityId": 1,
                "activityType": {"typeKey": "tennis_v2"},
                "activityName": "Tennis Match 1",
                "startTimeLocal": "2025-05-17T14:00:00",
            },
            {
                "activityId": 2,
                "activityType": {"typeKey": "running"},
                "activityName": "Lauf",
                "startTimeLocal": "2025-05-16T10:00:00",
            },
            {
                "activityId": 3,
                "activityType": {"typeKey": "tennis_v2"},
                "activityName": "Tennis Match 2",
                "startTimeLocal": "2025-05-18T16:00:00",
            },
        ]

        # Mock API-Methoden
        self.mock_api.get_activities.return_value = self.raw_activities
        self.mock_api.login.return_value = None

        # GarminClient mit mock_api
        self.client = GarminClient(api=self.mock_api)

    def test_login_calls_api_login(self):
        self.client.login()
        self.mock_api.login.assert_called_once()

    def test_get_raw_activities_returns_api_data(self):
        activities = self.client.get_raw_activities()
        self.assertEqual(activities, self.raw_activities)
        self.mock_api.get_activities.assert_called_once_with(10)

    def test_get_parsed_tennis_activities_filters_and_parses(self):
        # Patch DataParserHelper.parseTennisActivities, damit wir einfaches Ergebnis erzwingen können
        original_parse = DataParserHelper.parseTennisActivities
        DataParserHelper.parseTennisActivities = MagicMock(side_effect=lambda a: {"id": a["activityId"]})

        parsed = self.client.get_parsed_tennis_activities()

        # Es sollen nur Tennis-Aktivitäten sein (id=1 und id=3)
        expected = [{"id": 1}, {"id": 3}]
        self.assertEqual(parsed, expected)

        # Restore Originalfunktion
        DataParserHelper.parseTennisActivities = original_parse


if __name__ == "__main__":
    unittest.main()
