# weather_data.py

import requests  # To make HTTP requests to the OpenWeatherMap API
import csv       # To handle writing weather data to a CSV file
from datetime import datetime  # To record the current date and time when data is fetched

# OpenWeatherMap API key (replace 'your_openweathermap_api_key' with your actual API key)
API_KEY = '70b28742e7023dcaf570a86bda9a7a61'
# Base URL for the OpenWeatherMap API
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city_name):
    """
    Fetch weather data for a specific city from the OpenWeatherMap API.

    Args:
        city_name (str): The name of the city for which weather data is to be fetched.

    Returns:
        dict: A dictionary containing weather data (temperature, humidity, etc.).
        None: If there's an error fetching the data (e.g., invalid city or network issue).
    """
    try:
        # Construct the full API URL by adding the city name and API key.
        # We also set 'units=metric' to get the temperature in Celsius.
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

        # Send the GET request to the API and store the response
        response = requests.get(url)

        # Convert the JSON response into a Python dictionary
        data = response.json()

        # Check if the city was found (if not, the 'cod' field will not be 200)
        if data['cod'] != 200:
            print(f"Error fetching data for {city_name}: {data['message']}")
            return None

        # Extract the important information from the API response
        weather_info = {
            "city": city_name,  # The city name
            "temperature": data['main']['temp'],  # Temperature in Celsius
            "humidity": data['main']['humidity'],  # Humidity percentage
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # The current time
        }

        # Return the extracted weather data as a dictionary
        return weather_info

    except Exception as e:
        # If any error occurs (like network issue or API being down), print an error message
        print(f"Error: {e}")
        return None

def save_to_csv(data, filename='weather_data.csv'):
    """
    Save the fetched weather data to a CSV file.

    Args:
        data (dict): The weather data to save.
        filename (str): The name of the CSV file (default is 'weather_data.csv').
    """
    # Define the headers (column names) for the CSV file
    headers = ['city', 'temperature', 'humidity', 'timestamp']

    # Open the CSV file in append mode ('a'), which allows us to add rows to the file
    with open(filename, mode='a', newline='') as file:
        # Create a CSV writer object that will help write rows of data to the file
        writer = csv.DictWriter(file, fieldnames=headers)

        # Write the headers to the CSV only if the file is empty (i.e., if we're writing for the first time)
        if file.tell() == 0:
            writer.writeheader()

        # Write the weather data (as a row in the CSV file)
        writer.writerow(data)

if __name__ == "__main__":
    # Get the city name from the user
    city = input("Enter the city name: ")

    # Fetch the weather data for the city
    weather_data = fetch_weather(city)
    
    # If we successfully fetched the weather data, save it to the CSV
    if weather_data:
        save_to_csv(weather_data)
        print(f"Weather data for {city} saved to weather_data.csv")
