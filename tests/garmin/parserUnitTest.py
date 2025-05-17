import unittest
from dashboard.garmin.parser import DataParserHelper  # Ersetze your_module durch den tatsächlichen Modulnamen


class TestDataParserHelper(unittest.TestCase):
    def test_parseTennisActivities(self):
        sample_activity = {
            "activityId": 12345,
            "activityName": "Tennis Match",
            "startTimeLocal": "2025-05-17T14:00:00",
            "startTimeGMT": "2025-05-17T12:00:00Z",
            "duration": 3600,
            "movingDuration": 3500,
            "distance": 5000.0,
            "calories": 600,
            "steps": 7000,
            "averageHR": 140,
            "maxHR": 180,
            "aerobicTrainingEffect": 2.5,
            "anaerobicTrainingEffect": 1.5,
            "trainingEffectLabel": "Maintenance",
            "hrTimeInZone_1": 600,
            "hrTimeInZone_2": 900,
            "hrTimeInZone_3": 1200,
            "hrTimeInZone_4": 600,
            "hrTimeInZone_5": 300,
            "locationName": "Local Tennis Club",
            "startLatitude": 52.5200,
            "startLongitude": 13.4050,
            "endLatitude": 52.5205,
            "endLongitude": 13.4055,
            "moderateIntensityMinutes": 25,
            "vigorousIntensityMinutes": 35,
            "differenceBodyBattery": 10,
            "activityTrainingLoad": 150
        }

        expected_output = {
            "id": 12345,
            "name": "Tennis Match",
            "start_time_local": "2025-05-17T14:00:00",
            "start_time_gmt": "2025-05-17T12:00:00Z",
            "duration_sec": 3600,
            "moving_duration": 3500,
            "distance_m": 5000.0,
            "calories": 600,
            "steps": 7000,
            "avg_hr": 140,
            "max_hr": 180,
            "training_effect_aerob": 2.5,
            "training_effect_anaerob": 1.5,
            "training_effect_label": "Maintenance",
            "hr_zone_times": {
                "z1": 600,
                "z2": 900,
                "z3": 1200,
                "z4": 600,
                "z5": 300,
            },
            "location": "Local Tennis Club",
            "start_lat": 52.5200,
            "start_long": 13.4050,
            "end_lat": 52.5205,
            "end_long": 13.4055,
            "intensity_minutes": {
                "moderate": 25,
                "vigorous": 35,
            },
            "body_battery_change": 10,
            "training_load": 150,
        }

        result = DataParserHelper.parseTennisActivities(sample_activity)
        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
