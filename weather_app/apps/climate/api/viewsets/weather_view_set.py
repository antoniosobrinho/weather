from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from apps.climate.api.serializers.weather_query_serializer import (
    WeatherQuerySerializer,
)
from apps.climate.services.weather_service import WeatherService
from apps.climate.api.serializers.weather_serializer import WeatherSerializer


class WeatherViewSet(ViewSet):
    @method_decorator(cache_page(60 * 10))
    def list(self, request):
        weather_query_serializer = WeatherQuerySerializer(data=request.query_params)
        if not weather_query_serializer.is_valid():
            return Response(weather_query_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        city = weather_query_serializer.validated_data["city"]
        state = weather_query_serializer.validated_data["state"]
        country = weather_query_serializer.validated_data["country"]

        weather_service = WeatherService()

        current_weather = weather_service.get_current_weather(city, state, country)

        if not current_weather:
            return Response(status=status.HTTP_404_NOT_FOUND)

        weather_serializer = WeatherSerializer(current_weather)

        return Response(weather_serializer.data)
