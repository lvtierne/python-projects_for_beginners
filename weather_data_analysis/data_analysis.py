# data_analysis.py

import csv  # To read the CSV file containing weather data

def analyze_weather_data(filename='weather_data.csv'):
    """
    Analyze the weather data stored in the CSV file.

    The function calculates:
    - Average temperature
    - Maximum temperature
    - Minimum temperature
    - Average humidity

    Args:
        filename (str): The name of the CSV file (default is 'weather_data.csv').
    """
    temperatures = []  # List to store all temperatures from the CSV file
    humidities = []    # List to store all humidity values from the CSV file
    
    try:
        # Open the CSV file in read mode ('r')
        with open(filename, mode='r') as file:
            # Create a CSV reader object to read rows from the file
            reader = csv.DictReader(file)

            # Loop through each row in the CSV file
            for row in reader:
                # Convert the 'temperature' and 'humidity' values to floats and add to the respective lists
                temperatures.append(float(row['temperature']))
                humidities.append(float(row['humidity']))
        
        # If we have collected temperature and humidity data, perform the calculations
        if temperatures and humidities:
            # Calculate and print the average, maximum, and minimum temperatures
            print(f"Average Temperature: {sum(temperatures) / len(temperatures):.2f}°C")
            print(f"Max Temperature: {max(temperatures)}°C")
            print(f"Min Temperature: {min(temperatures)}°C")
            
            # Calculate and print the average humidity
            print(f"Average Humidity: {sum(humidities) / len(humidities):.2f}%")
        else:
            # If no data was found, let the user know
            print("No data to analyze.")
    
    # Handle the case where the CSV file doesn't exist
    except FileNotFoundError:
        print(f"{filename} not found.")
    
    # Handle any other unexpected errors that may occur during file reading or analysis
    except Exception as e:
        print(f"Error while analyzing data: {e}")

if __name__ == "__main__":
    # Run the analysis function when this script is executed directly
    analyze_weather_data()
