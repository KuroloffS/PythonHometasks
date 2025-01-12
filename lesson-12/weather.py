import requests

def fetch_weather(city):
    api_key = "c8a23e906ce6c62be6b14f0d7ec9124c"  
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        
        city_name = weather_data.get("name")
        temperature = weather_data["main"].get("temp")
        humidity = weather_data["main"].get("humidity")
        weather_description = weather_data["weather"][0].get("description")
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Unexpected response format. Please check the API key and city name.")

# Fetch weather for Tashkent
fetch_weather("Tashkent")
