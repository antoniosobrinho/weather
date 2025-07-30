from rest_framework import serializers

class WeatherDescriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    main = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    icon = serializers.CharField(required=False)

class WeatherSerializer(serializers.Serializer):
    dt = serializers.IntegerField(required=False)
    sunrise = serializers.IntegerField(required=False)
    sunset = serializers.IntegerField(required=False)
    temp = serializers.FloatField(required=False)
    feels_like = serializers.FloatField(required=False)
    pressure = serializers.IntegerField(required=False)
    humidity = serializers.IntegerField(required=False)
    dew_point = serializers.FloatField(required=False)
    uvi = serializers.FloatField(required=False)
    clouds = serializers.IntegerField(required=False)
    visibility = serializers.IntegerField(required=False)
    wind_speed = serializers.FloatField(required=False)
    wind_deg = serializers.IntegerField(required=False)
    wind_gust = serializers.FloatField(required=False)
    weather = WeatherDescriptionSerializer(many=True)