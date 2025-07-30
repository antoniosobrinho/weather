from django.conf import settings
import requests

from apps.climate.dtos.coordinates_dto import CoordinatesDTO


class OpenWeatherMapService:
    def __init__(self):
        self.host = settings.OPENWEATHERMAP_API_HOST
        self.api_key = settings.OPENWEATHERMAP_API_KEY

    def get_cities_by_name(self, name: str) -> list:
        params = {"q": name, "limit": 1000, "appid": self.api_key}

        cities = requests.get(self.host + "/geo/1.0/direct", params=params)

        return cities.json()

    def get_weather_by_coordinates(self, coordinates: CoordinatesDTO) -> dict:
        params = {
            "lat": coordinates.lat,
            "lon": coordinates.lon,
            "units": "metric",
            "appid": self.api_key,
        }
        weather_request = requests.get(self.host + "/data/3.0/onecall", params=params)

        weather = weather_request.json()

        return weather["current"]
