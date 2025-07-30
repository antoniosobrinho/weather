from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from apps.climate.api.serializers.weather_query_serializer import (
    WeatherQuerySerializer,
)
from apps.climate.services.weather_service import WeatherService


class WeatherViewSet(ViewSet):
    def list(self, request):
        serializer = WeatherQuerySerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        city = serializer.validated_data["city"]
        state = serializer.validated_data["state"]
        country = serializer.validated_data["country"]

        weather_service = WeatherService()

        current_weather = weather_service.get_current_weather(city, state, country)

        if not current_weather:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(
            current_weather
        )
