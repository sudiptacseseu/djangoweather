from django.shortcuts import render


def home(request):
    import json
    import requests

    if request.method == 'POST':
        zipcode = request.POST['zipcode_input']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application"
                                   "/json&zipCode=" + zipcode +
                                   "&date=2021-06-23T00-0000&distance=5&API_KEY=89D608E0-6419-43DD-936F-51E9B6C0F902")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable.However, there may be a risk for some people, " \
                                   "particularly those who are unusually sensitive to air pollution. "
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Members of sensitive groups may experience health effects.The general " \
                                   "public is less likely to be affected. "
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Some members of the general public may experience health effects; " \
                                   "members of sensitive groups may experience more serious health effects. "
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        else:
            category_description = "(301 or more) Health warning of emergency conditions: everyone is more likely to " \
                                   "be affected."
            category_color = "hazardous"

        return render(request, 'home.html',
                      {'api': api, 'category_description': category_description, 'category_color': category_color})

    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/historical/?format=application"
                                   "/json&zipCode=89129&date=2021-06-23T00-0000&distance=5&API_KEY=89D608E0-6419-43DD"
                                   "-936F-51E9B6C0F902")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_description = "(0 - 50) Air quality is satisfactory, and air pollution poses little or no risk."
            category_color = "good"
        elif api[0]['Category']['Name'] == "Moderate":
            category_description = "(51 - 100) Air quality is acceptable.However, there may be a risk for some " \
                                   "people, particularly those who are unusually sensitive to air pollution. "
            category_color = "moderate"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_description = "(101 - 150) Members of sensitive groups may experience health effects.The general " \
                                   "public is less likely to be affected. "
            category_color = "usg"
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_description = "(151 - 200) Some members of the general public may experience health effects; " \
                                   "members of sensitive groups may experience more serious health effects. "
            category_color = "unhealthy"
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_description = "(201 - 300) Health alert: The risk of health effects is increased for everyone."
            category_color = "veryunhealthy"
        else:
            category_description = "(301 or more) Health warning of emergency conditions: everyone is more likely to " \
                                   "be affected."
            category_color = "hazardous"

        return render(request, 'home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
