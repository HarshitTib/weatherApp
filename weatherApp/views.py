from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
import requests


def index(request):
    context = { }
    return render(request, "index.html", context)

def weather_forecast(request):
    city = request.GET.get('city', 'Bengaluru')  # Default to Bengaluru if city not provided
    url = f"{settings.WEATHER_API_BASE_URL}weather?q={city}&units=metric&APPID={settings.WEATHER_API_KEY}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return JsonResponse(weather_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "Weather API request failed"}, status=500)
    


def current_forecast(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    api_key = settings.WEATHER_API_KEY
    base_url = settings.WEATHER_API_BASE_URL + "/weather"

    if lat is None or lon is None:
        return JsonResponse({"error": "Latitude and longitude are required."}, status=400)

    params = {
        'lat': lat,
        'lon': lon,
        'units': 'metric',
        'APPID': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return JsonResponse(weather_data)
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": "Weather API request failed"}, status=500)