import requests

def get_weather(city, api_key):
    """Fetch weather data from OpenWeather API."""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, Response: {response.text}")
        return None

def display_weather(weather_data):
    """Display the weather information."""
    if weather_data:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description.capitalize()}")
    else:
        print("City not found or API error.")

def main():
    """Main function to run the weather app."""
    api_key = "31459b99de5f17eadfa10765f4112e4d"  
    city = input("Enter city name: ")
    
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
