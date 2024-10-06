# Import the datetime module for working with dates
import datetime

def add_expense(expenses):
    """
    Adds a new expense to the provided 'expenses' dictionary.
    """
    # Ask the user for the category of the expense (e.g., food, travel)
    category = input("Enter the category (e.g., food, travel): ").strip().lower()

    # Validate that the category contains only letters
    if not category.isalpha():
        print("Invalid category. Please use letters only.")
        return  # Stop execution if the category is invalid

    try:
        # Ask the user for the amount of the expense, and convert it to a float
        amount = float(input("Enter the amount: $").strip())
    except ValueError:
        # If the user doesn't enter a valid number, show an error and return
        print("Invalid amount. Please enter a number.")
        return

    # Ask for an optional description of the expense
    description = input("Enter a description (optional): ").strip()
    
    # Ask for the date of the expense or default to today's date
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ").strip()

    # If no date is provided, set it to today's date
    if not date:
        date = str(datetime.date.today())  # Get today's date as a string

    # Check if the category already exists in the expenses dictionary
    if category not in expenses:
        expenses[category] = []  # If not, create an empty list for this category
    
    # Append the new expense (as a dictionary) to the list for the given category
    expenses[category].append({
        "amount": amount,
        "description": description if description else "No description",  # Default to "No description" if empty
        "date": date
    })

    # Confirm that the expense was added
    print(f"Added ${amount:.2f} to {category} on {date}.")

def view_totals(expenses):
    """
    Displays total expenses by category.
    """
    # If there are no expenses recorded, print a message and return
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Print a header
    print("\nYour Finances:")
    print("=" * 40)
    
    # Loop through each category and its associated records in the expenses dictionary
    for category, records in expenses.items():
        print(f"\nCategory: {category.capitalize()}")  # Capitalize the category name
        print("-" * 30)
        total = 0  # Variable to keep track of the total amount in this category
        
        # Loop through each expense in this category and print details
        for record in records:
            print(f"Amount: ${record['amount']:.2f} | Date: {record['date']} | Description: {record['description']}")
            total += record["amount"]  # Add the expense amount to the total for this category
        
        # Print the total amount for this category
        print(f"Total for {category.capitalize()}: ${total:.2f}")

def quick_add_expense(expenses):
    """
    Adds a quick expense to a default 'Misc' category.
    This is useful for quick daily tracking without extra details.
    """
    try:
        # Ask for the amount of the expense and convert it to a float
        amount = float(input("Enter the amount: $").strip())
    except ValueError:
        # Handle invalid input
        print("Invalid amount. Please enter a number.")
        return

    # Set the category to "Misc" by default
    category = "misc"

    # Get today's date for the quick expense
    date = str(datetime.date.today())  # Get today's date as a string

    # If the category doesn't exist yet, create it
    if category not in expenses:
        expenses[category] = []

    # Add the quick expense to the "Misc" category
    expenses[category].append({
        "amount": amount,
        "description": "Quick add",  # Default description for quick adds
        "date": date
    })

    # Confirm that the expense was added
    print(f"Added ${amount:.2f} to Misc category.")

def edit_expense(expenses):
    """
    Allows the user to edit an existing expense by selecting a category and choosing a specific expense to modify.
    """
    # Ask the user for the category they want to edit
    category = input("Enter the category you want to edit: ").strip().lower()

    # Check if the category exists in the expenses dictionary
    if category not in expenses:
        print(f"No expenses found for {category}.")
        return

    try:
        # Print a list of expenses in this category for the user to choose from
        print(f"Current expenses in {category}:")
        for i, record in enumerate(expenses[category], start=1):  # Enumerate the expenses with numbers starting from 1
            print(f"{i}. ${record['amount']:.2f} on {record['date']} - {record['description']}")
        
        # Ask the user for the number of the expense they want to edit
        index = int(input("Enter the number of the expense to edit: ")) - 1
        
        # Validate the index (it must be within the list bounds)
        if index < 0 or index >= len(expenses[category]):
            print("Invalid number. Please try again.")
            return

        # Ask for the new amount and update the expense
        new_amount = float(input("Enter the new amount: $").strip())
        expenses[category][index]["amount"] = new_amount  # Update the amount
        print(f"Expense #{index + 1} updated to ${new_amount:.2f}.")
    except (ValueError, IndexError):
        # Handle invalid input (e.g., non-numeric input or out-of-bounds index)
        print("Invalid input. Please enter a valid number.")
