from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('api/weather-forecast/', views.weather_forecast, name='weather-forecast'),
    path('api/current-forecast/', views.current_forecast, name='current-forecast'),
]
