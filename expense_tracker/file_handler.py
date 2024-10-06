# Import the JSON module to work with JSON data
import json

def load_expenses():
    """
    Loads expenses from the 'expenses.json' file.
    Returns a dictionary of expenses or an empty dictionary if the file doesn't exist.
    """
    try:
        # Try to open and load the JSON file
        with open("expenses.json", "r") as file:
            return json.load(file)  # Load the data as a Python dictionary
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is corrupted, return an empty dictionary
        return {}

def save_expenses(expenses):
    """
    Saves the current expenses to the 'expenses.json' file.
    """
    # Open the file in write mode ('w') and save the dictionary as JSON
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)  # Save with indentation for readability
