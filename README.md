# Weather App 🌤️
A simple Flask-based web application that fetches real-time weather data using the OpenWeather API. Users can search any city and view the current weather along with a 5-day forecast.

---

## Features
• Search weather by city name  
• Displays current temperature, min/max temp, wind speed, and weather condition  
• 5-day forecast (midday temperature + condition)  
• Error page for invalid city names  
• Responsive UI (desktop + mobile)  
• Built with Flask and Jinja templates  

---

## Tech Stack
**Backend:** Python, Flask  
**Frontend:** HTML, CSS (Grid + Flexbox), Jinja2  
**API:** OpenWeather Geocoding + Weather + Forecast API  
**Deployment:** Supports Gunicorn / Render / Heroku  
**Environment Vars:** python-dotenv  

---

## Installation

### 1. Clone the repository
```
git clone <repo-url>
cd python-weather-app
```

### 2. (Optional) Create and activate a virtual environment
```
python3 -m venv .venv
source .venv/bin/activate    # Mac/Linux
.venv\Scripts\activate       # Windows
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

---

## Environment Variables
Create a file named `.env` in the project folder and add:

```
OWM_API_KEY=your_openweather_api_key_here
```

Get a free API key at: https://openweathermap.org/api

---

## Running the App
```
python3 main.py
```

Then open in your browser:

```
http://127.0.0.1:5000
```

---

## Project Structure
- **main.py** → Flask app  
- **requirements.txt** → Dependencies  
- **templates/** → HTML files (index, city, error)  
- **static/** → CSS + assets  
- **.env** → Stores API key (not committed)  
- **README.md**  

---

## Screenshots (Desktop)
<img src="/screenshots/weather_app_desktop_home_page_screenshot.png">
<img src="/screenshots/weather_app_desktop_forecast_page_screenshot.png">
<img src="/screenshots/weather_app_desktop_error_page_screenshot.png">

## Screenshots (Mobile)
<img src="/screenshots/weather_app_iphone_forecast_page_screenshot.png" style="width:400px;"> <img src="/screenshots/weather_app_iphone_home_page_screenshot.png" style="width:400px;">
---

## API Reference
- Current Weather: `api.openweathermap.org/data/2.5/weather`  
- 5-Day Forecast: `api.openweathermap.org/data/2.5/forecast`  
- City Lookup / Geocoding: `api.openweathermap.org/geo/1.0/direct`  

---

## Future Improvements
• Toggle °C / °F  
• Auto-detect user’s location  
• Support country selection for cities with same name  
• Show daily high/low instead of just noon temp  
• Add recent searches or favorites list  

---

## License
MIT License — free to use and modify.

---

## Acknowledgments
• OpenWeather API  
• Flask Documentation  
• CSS Grid & Flexbox guides  

# Feature Request: Temperature Unit Toggle (°C / °F)

## Description
Participants will add a temperature unit toggle that lets users switch between Celsius and Fahrenheit within the weather app. The feature should update all displayed temperatures when toggled and visually indicate the selected unit. The preference should persist across sessions so that the app remembers the user’s last choice.

## Expected Outcome
A working toggle button or switch that changes all temperature values in the app and stores the user’s preferred unit for later sessions.

## Notes for Participants
You may choose how to style or position the toggle (e.g., header switch, dropdown, or button group) as long as it clearly switches between °C and °F and updates the displayed values.