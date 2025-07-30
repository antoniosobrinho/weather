from typing import Optional

from apps.climate.dtos.coordinates_dto import CoordinatesDTO
from apps.climate.services.open_weather_map_service import (
    OpenWeatherMapService,
)
import unicodedata


class WeatherService:
    def __init__(self):
        self.weather_api_service = OpenWeatherMapService()

    def get_city_coordinates(self, city_name: str, state: str, country: str) -> Optional[CoordinatesDTO]:
        cities = self.weather_api_service.get_cities_by_name(city_name)

        state = self.__remove_accents(state.lower())
        country = country.lower()

        for city in cities:
            state_city = self.__remove_accents(city.get("state", "").lower())
            if (
                state_city == state
                and city.get("country", "").lower() == country
            ):
                coordinates = CoordinatesDTO(lat=city["lat"], lon=city["lon"])
                return coordinates

        return

    def get_current_weather(self, city:str, state:str, country:str) -> Optional[dict]:
        city_coordinates = self.get_city_coordinates(city, state, country)

        if not city_coordinates:
            return

        weather_temp = self.weather_api_service.get_weather_by_coordinates(city_coordinates)

        return weather_temp

    def __remove_accents(self, text:str) -> str:
        normalized_text = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in normalized_text if not unicodedata.combining(c))