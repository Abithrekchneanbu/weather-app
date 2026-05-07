Weather Application

A simple Python Weather Application built using Tkinter and OpenWeatherMap API.  
This application allows users to enter a city name and view live weather details such as temperature, weather condition, and humidity.


Features

- Live weather information
- Simple graphical user interface (GUI)
- Displays:
  - Temperature
  - Weather condition
  - Humidity
- Error handling for invalid city names
- Beginner-friendly Python project

Technologies Used

- Python
- Tkinter
- Requests Library
- OpenWeatherMap API


Project Structure

Weather_App/
│
├── weather_gui.py
└── README.md


Installation Steps

1. Install Python

Download Python from:
https://www.python.org/downloads/



2. Install Required Library

Open terminal and run:

pip install requests



3. Get API Key

Create a free account at:
https://openweathermap.org/api

Copy your API key.



4. Add API Key

Open `weather_gui.py`

Replace:

API_KEY = "your_api_key_here"

with your actual API key.

Example:

API_KEY = "abcd123xyz"


Run the Application

Open terminal inside the project folder and run:

python weather_gui.py

or

py weather_gui.py



How to Use

1. Enter a city name
2. Click the **Get Weather** button
3. Weather details will appear on the screen



Example Output

City: Chennai  
Temperature: 31°C  
Weather: Clear Sky  
Humidity: 72%



Future Improvements

- Add weather icons
- Add dark mode
- Add 5-day forecast
- Add search history
- Improve UI design



Author

Developed as a beginner Python project.
