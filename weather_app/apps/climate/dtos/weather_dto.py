from dataclasses import dataclass
from typing import Optional, List

@dataclass
class WeatherDescriptionDTO:
    id: Optional[int] = None
    main: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None

@dataclass
class WeatherDTO:
    dt: Optional[int] = None
    sunrise: Optional[int] = None
    sunset: Optional[int] = None
    temp: Optional[float] = None
    feels_like: Optional[float] = None
    pressure: Optional[int] = None
    humidity: Optional[int] = None
    dew_point: Optional[float] = None
    uvi: Optional[float] = None
    clouds: Optional[int] = None
    visibility: Optional[int] = None
    wind_speed: Optional[float] = None
    wind_deg: Optional[int] = None
    wind_gust: Optional[float] = None
    weather: Optional[List[WeatherDescriptionDTO]] = None
