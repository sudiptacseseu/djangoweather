from django.shortcuts import render


def home(request):
    import json
    import requests
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json"
                               "&zipCode=89129&date=2021-06-23T00-0000&distance=5&API_KEY=89D608E0-6419-43DD-936F"
                               "-51E9B6C0F902")
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"

    return render(request, 'home.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
