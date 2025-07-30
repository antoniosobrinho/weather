from rest_framework import serializers

class WeatherQuerySerializer(serializers.Serializer):
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
