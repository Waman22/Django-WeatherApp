import requests
from django.shortcuts import render

def weather_view(request):
    api_key = "your OpenWeatherMap API key"  # Replace with your OpenWeatherMap API key
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.POST.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                error = "City not found or API error."
        else:
            error = "Please enter a city name."

    return render(request, "weather/index.html", {"weather_data": weather_data, "error": error})
