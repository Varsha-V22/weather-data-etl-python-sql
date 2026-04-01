import requests
from config import API_URL

def extract_data():
    response = requests.get(API_URL)
    data = response.json()

    return {
        "temperature": data["current_weather"]["temperature"],
        "wind_speed": data["current_weather"]["windspeed"] 
    }
