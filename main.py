import datetime            # For working with dates and times (e.g., today's date)
import requests            # For making HTTP requests to the OpenWeather API
import string              # For formatting city names (capitalizing)
from flask import Flask, render_template, request, redirect, url_for  # Flask web framework
import os                  # For accessing environment variables
from dotenv import load_dotenv  # For loading variables from a .env file

# Load environment variables from a .env file in the project root
load_dotenv()

# OpenWeather API endpoints
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"      # Current weather data
OWM_FORECAST_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"  # 5-day forecast data
GEOCODING_API_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"     # Convert city name to lat/lon

# Read the OpenWeather API key from environment variable
api_key = os.getenv("OWM_API_KEY")
# Alternative way to access env var:
# api_key = os.environ.get("OWM_API_KEY")

# Create the Flask app instance
app = Flask(__name__)


# Display home page and handle city search form submission
@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home route:
    - GET: render the search page (index.html)
    - POST: get the city name from the form and redirect to /<city>
    """
    if request.method == "POST":
        # Get the city name entered by the user in the form with name="search"
        city = request.form.get("search")
        # Redirect to the get_weather route with the city in the URL
        return redirect(url_for("get_weather", city=city))
    # For GET requests, just render the home page with the search form
    return render_template("index.html")


# Display weather forecast for a specific city using data from OpenWeather API
@app.route("/<city>", methods=["GET", "POST"])
def get_weather(city):
    """
    Weather route:
    - Takes a city from the URL
    - Uses OpenWeather's Geocoding API to get latitude & longitude
    - Uses those coordinates to fetch current weather and 5-day forecast
    - Renders city.html with all the weather info
    """

    # Format city name (e.g., "oklahoma city" -> "Oklahoma City") for display
    city_name = string.capwords(city)

    # Get today's date and format it nicely for display (e.g., "Friday, November 21")
    today = datetime.datetime.now()
    current_date = today.strftime("%A, %B %d")

    # Build parameters to get latitude and longitude based on the city name
    location_params = {
        "q": city_name,   # City name (e.g., "Oklahoma City")
        "appid": api_key, # API key for authentication
        "limit": 3,       # Max number of location results to return
    }

    # Call the Geocoding API to convert city name to coordinates
    location_response = requests.get(GEOCODING_API_ENDPOINT, params=location_params)
    location_data = location_response.json()

    # If the city is not found or the API returns an empty list,
    # redirect user to the error page instead of crashing with IndexError
    if not location_data:
        return redirect(url_for("error"))
    else:
        # Take the first result's latitude and longitude
        lat = location_data[0]['lat']
        lon = location_data[0]['lon']

    # Build parameters for current weather and forecast requests
    weather_params = {
        "lat": lat,          # Latitude from geocoding
        "lon": lon,          # Longitude from geocoding
        "appid": api_key,    # API key
        "units": "metric",   # Use metric units (°C, m/s)
    }

    # Request current weather data
    weather_response = requests.get(OWM_ENDPOINT, weather_params)
    # Raise an exception if the API request failed (e.g., invalid key, rate limit, etc.)
    weather_response.raise_for_status()
    # Parse the JSON response into a Python dict
    weather_data = weather_response.json()

    # Extract the current weather details from the response
    current_temp = round(weather_data['main']['temp'])         # Current temperature in °C
    current_weather = weather_data['weather'][0]['main']       # Weather description (e.g., "Clouds")
    min_temp = round(weather_data['main']['temp_min'])         # Today's minimum temperature
    max_temp = round(weather_data['main']['temp_max'])         # Today's maximum temperature
    wind_speed = weather_data['wind']['speed']                 # Current wind speed

    # Request 5-day / 3-hour interval forecast data
    forecast_response = requests.get(OWM_FORECAST_ENDPOINT, weather_params)
    forecast_data = forecast_response.json()

    # The forecast endpoint returns data for every 3 hours.
    # Filter to only entries at 12:00:00 each day to get a single value per day.
    five_day_temp_list = [
        round(item['main']['temp'])
        for item in forecast_data['list']
        if '12:00:00' in item['dt_txt']
    ]

    # Similarly, extract the weather description at 12:00:00 for each of the next 5 days
    five_day_weather_list = [
        item['weather'][0]['main']
        for item in forecast_data['list']
        if '12:00:00' in item['dt_txt']
    ]

    # Build a list of the next 5 dates (today + 4 more days)
    five_day_unformatted = [
        today,
        today + datetime.timedelta(days=1),
        today + datetime.timedelta(days=2),
        today + datetime.timedelta(days=3),
        today + datetime.timedelta(days=4),
    ]

    # Format those dates as short weekday names (e.g., "Mon", "Tue")
    five_day_dates_list = [date.strftime("%a") for date in five_day_unformatted]

    # Render the city.html template, passing all the weather data to be displayed
    return render_template(
        "city.html",
        city_name=city_name,
        current_date=current_date,
        current_temp=current_temp,
        current_weather=current_weather,
        min_temp=min_temp,
        max_temp=max_temp,
        wind_speed=wind_speed,
        five_day_temp_list=five_day_temp_list,
        five_day_weather_list=five_day_weather_list,
        five_day_dates_list=five_day_dates_list,
    )


# Display error page for invalid city input or missing coordinates
@app.route("/error")
def error():
    """
    Error route:
    - Renders a simple error template when something goes wrong
      (e.g., invalid city entered by the user).
    """
    return render_template("error.html")


# Run the Flask development server when this file is executed directly
if __name__ == "__main__":
    # debug=True enables auto-reload on code changes and shows detailed error pages
    app.run(debug=True)
