import requests
import json
import pyttsx3
import tkinter as tk
from tkinter import messagebox

# Text-to-speech engine
engine = pyttsx3.init()

# Function to fetch weather
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    try:
        url = f"https://api.weatherapi.com/v1/current.json?key=a0b825bb5e1f418caee155605251506&q={city}"
        response = requests.get(url)
        data = json.loads(response.text)

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        result = (
            f"City: {city}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {condition}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind} km/h"
        )
        result_label.config(text=result)
        engine.say(f"The current weather in {city} is {temp} degrees Celsius with {condition}")
        engine.runAndWait()

    except Exception as e:
        messagebox.showerror("Error", "The City is not in the API right now.\n" + str(e))

# GUI setup
root = tk.Tk()
root.title("Weather App By RS")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter City Name:", font=("Arial", 14)).pack(pady=10)
city_entry = tk.Entry(root, font=("Arial", 14), justify='center')
city_entry.pack(pady=5)

tk.Button(root, text="How's the Weather", font=("Arial", 14), command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=10)

root.mainloop()
