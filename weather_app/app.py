from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Get API key from environment variable
API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather_data(city):
    """Fetch weather data from OpenWeather API"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            # Add additional weather info processing here
            return data
        else:
            print(f"Error: Status code {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            weather_data = get_weather_data(city)
            if weather_data is None:
                error = "Could not fetch weather data. Please try again."
    
    return render_template('index.html', 
                         weather_data=weather_data,
                         error=error)

if __name__ == '__main__':
    app.run(debug=True)
