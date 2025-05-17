class DataParserHelper:
    @staticmethod
    def parseTennisActivities(activity: dict) -> dict:
        return {
            "id": activity.get("activityId"),
            "name": activity.get("activityName"),
            "start_time_local": activity.get("startTimeLocal"),
            "start_time_gmt": activity.get("startTimeGMT"),
            "duration_sec": activity.get("duration"),
            "moving_duration": activity.get("movingDuration"),
            "distance_m": activity.get("distance"),
            "calories": activity.get("calories"),
            "steps": activity.get("steps"),
            "avg_hr": activity.get("averageHR"),
            "max_hr": activity.get("maxHR"),
            "training_effect_aerob": activity.get("aerobicTrainingEffect"),
            "training_effect_anaerob": activity.get("anaerobicTrainingEffect"),
            "training_effect_label": activity.get("trainingEffectLabel"),
            "hr_zone_times": {
                "z1": activity.get("hrTimeInZone_1"),
                "z2": activity.get("hrTimeInZone_2"),
                "z3": activity.get("hrTimeInZone_3"),
                "z4": activity.get("hrTimeInZone_4"),
                "z5": activity.get("hrTimeInZone_5"),
            },
            "location": activity.get("locationName"),
            "start_lat": activity.get("startLatitude"),
            "start_long": activity.get("startLongitude"),
            "end_lat": activity.get("endLatitude"),
            "end_long": activity.get("endLongitude"),
            "intensity_minutes": {
                "moderate": activity.get("moderateIntensityMinutes"),
                "vigorous": activity.get("vigorousIntensityMinutes"),
            },
            "body_battery_change": activity.get("differenceBodyBattery"),
            "training_load": activity.get("activityTrainingLoad"),
        }
