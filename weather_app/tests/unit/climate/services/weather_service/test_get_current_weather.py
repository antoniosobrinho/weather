from django.test import TestCase
from unittest.mock import Mock, patch
from apps.climate.services.weather_service import WeatherService
from apps.climate.dtos.weather_dto import WeatherDTO


class GetCurrentWeatherTest(TestCase):
    @patch("apps.climate.services.weather_service.OpenWeatherMapService")
    @patch.object(WeatherService, "get_city_coordinates")
    def test_should_return_weather_dto_when_coordinates_found(
        self, mock_get_city_coordinates, MockOpenWeatherMapService
    ):
        city_coordinates = Mock()
        mock_get_city_coordinates.return_value = city_coordinates

        mock_service_instance = MockOpenWeatherMapService.return_value
        mock_weather_dto = WeatherDTO(
            pressure=25.0, humidity=60, temp=10
        )

        mock_service_instance.get_weather_by_coordinates.return_value = mock_weather_dto

        service = WeatherService()

        result = service.get_current_weather("Guarulhos", "São Paulo", "BR")

        mock_get_city_coordinates.assert_called_once_with("Guarulhos", "São Paulo", "BR")
        mock_service_instance.get_weather_by_coordinates.assert_called_once_with(city_coordinates)

        self.assertEqual(result, mock_weather_dto)
