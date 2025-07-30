from django.test import TestCase
from unittest.mock import patch
from apps.climate.services.weather_service import WeatherService
from apps.climate.dtos.coordinates_dto import CoordinatesDTO


class GetCityCoordinatesTest(TestCase):

    @patch("apps.climate.services.weather_service.OpenWeatherMapService")
    @patch.object(WeatherService, "_WeatherService__get_matched_city")
    def test_should_return_coordinates_when_city_matches(
        self, mock__get_matched_city, MockOpenWeatherMapService,
    ):
        mock_open_weather_map_service = MockOpenWeatherMapService.return_value
        mock_open_weather_map_service.get_cities_by_name.return_value = [
            {"lat": 10.0, "lon": 20.0, "state": "São Paulo", "country": "BR"},
            {"lat": 30.0, "lon": 40.0, "state": "Rio de Janeiro", "country": "BR"},
        ]

        mock__get_matched_city.return_value = {"lat": 10.0, "lon": 20.0, "state": "São Paulo", "country": "BR"}

        service = WeatherService()
        coordinates = service.get_city_coordinates("Guarulhos", "São Paulo", "BR")

        self.assertIsInstance(coordinates, CoordinatesDTO)
        self.assertEqual(coordinates.lat, 10.0)
        self.assertEqual(coordinates.lon, 20.0)

    @patch("apps.climate.services.weather_service.OpenWeatherMapService")
    @patch.object(WeatherService, "_WeatherService__get_matched_city")
    def test_should_return_none_when_city_does_no_matches(
        self, mock__get_matched_city, MockOpenWeatherMapService,
    ):
        mock_open_weather_map_service = MockOpenWeatherMapService.return_value
        mock_open_weather_map_service.get_cities_by_name.return_value = [
            {"lat": 10.0, "lon": 20.0, "state": "São Paulo", "country": "BR"},
            {"lat": 30.0, "lon": 40.0, "state": "Rio de Janeiro", "country": "BR"},
        ]

        mock__get_matched_city.return_value = None

        service = WeatherService()
        coordinates = service.get_city_coordinates("Guarulhos", "São Paulo", "BR")

        self.assertEqual(coordinates, None)
