# How to Run the Weather App

## Clone the repository
Open your terminal and run:
``  git clone https://github.com/rachanahegde/python-weather-app.git 
cd python-weather-app ``

## Set up a virtual environment
**Mac/Linux:**
`` python3 -m venv .venv
source .venv/bin/activate ``
**Windows:**
`` python -m venv .venv
.venv\Scripts\activate ``

## Install the dependencies
`` pip install -r requirements.txt ``
If the file doesn’t exist, you can install the main packages manually:
`` pip install Flask requests python-dotenv ``

## Create an OpenWeather account
Go to https://openweathermap.org  
Make a free account and generate an API key.  
Verify email to confirm account / subscribe to FREE OpenWeatherMap.  
This may take a couple minutes to activate.

## Add your API key
In the project folder, make a file called `.env`  
Paste this inside (replace with your key):
`` OWM_API_KEY=your_api_key_here
FLASK_DEBUG=1 ``

## Run the app
**Mac/Linux:**
`` python3 main.py ``
**Windows:**
`` python main.py ``
You should see something like:
`` * Running on http://127.0.0.1:5000 ``

## View it in your browser
Open (Cmd + Click) http://127.0.0.1:5000  
Type a city name to see the current weather and 5-day forecast.

## Stop the app
Click (Ctrl + C) in the terminal to stop it.
