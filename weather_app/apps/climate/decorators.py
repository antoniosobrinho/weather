from functools import wraps
from apps.climate.models import WeatherQueryHistory

def log_weather_query(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        city = request.query_params.get("city")
        state = request.query_params.get("state")
        country = request.query_params.get("country")

        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        ip = x_forwarded_for.split(",")[0] if x_forwarded_for else request.META.get("REMOTE_ADDR")

        WeatherQueryHistory.objects.create(
            city=city,
            state=state,
            country=country,
            ip_address=ip,
        )

        return func(request, *args, **kwargs)
    return wrapper
