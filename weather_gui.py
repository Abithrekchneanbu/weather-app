import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "20176a8a3e2edee00ad67168dd0a7031"

def get_weather():
    city = city_entry.get()

    if city == "":
        messagebox.showerror("Error", "Please enter city name")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]

        result_label.config(
            text=f"City: {city}\nTemperature: {temp}°C\nWeather: {weather}\nHumidity: {humidity}%"
        )

    else:
        messagebox.showerror("Error", "City not found")

root = tk.Tk()
root.title("Weather App")
root.geometry("400x400")
root.config(bg="lightblue")

title_label = tk.Label(
    root,
    text="Weather Application",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)

title_label.pack(pady=20)

city_entry = tk.Entry(root, font=("Arial", 14))
city_entry.pack(pady=10)

search_button = tk.Button(
    root,
    text="Get Weather",
    font=("Arial", 12),
    command=get_weather
)

search_button.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="lightblue",
    justify="left"
)

result_label.pack(pady=20)

root.mainloop()