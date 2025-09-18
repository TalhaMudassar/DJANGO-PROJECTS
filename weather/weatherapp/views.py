from django.shortcuts import render
import requests
from datetime import date
from django.contrib import messages


def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'bahawalpur'

    # Weather API
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=13e5af3489efc332f4af88cc8c4eec3d'

    # Google Custom Search API
    API_KEY = 'AIzaSyBQD092DJTg_CI99lBOI5MoEvz3Wq8oosU'
    SEARCH_ENGINE_ID = 'c73e898f7291643bc'
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    search_Type = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={search_Type}&imgSize=xlarge"

    try:
        # Weather data
        weather_data = requests.get(weather_url, params={'units': 'metric'}).json()

        if weather_data.get('cod') == "404":
            messages.error(request, f"City '{city}' does not exist.")
            return render(request, 'weatherapp/home.html', {'day': date.today()})

        if weather_data.get('cod') in (401, "401"):
            messages.error(request, "Weather API key is not valid.")
            return render(request, 'weatherapp/home.html', {'day': date.today()})

        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = date.today()

        # Google Image Search
        try:
            image_data = requests.get(city_url).json()

            if "error" in image_data:
                messages.error(request, "Google Image API key is not valid or quota exceeded.")
                image_url = None
            else:
                search_items = image_data.get("items", [])
                if not search_items:
                    messages.error(request, "No image found for this city.")
                    image_url = None
                else:
                    image_url = search_items[0]['link']

        except Exception:
            messages.error(request, "Could not fetch city image.")
            image_url = None

        return render(request, 'weatherapp/home.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'image_url': image_url
        })

    except Exception:
        messages.error(request, "Something went wrong with the Weather API. Please try again.")
        return render(request, 'weatherapp/home.html', {'day': date.today()})
