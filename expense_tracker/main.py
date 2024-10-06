# Importing necessary functions from other files
from expense_manager import add_expense, view_totals, edit_expense, quick_add_expense
from file_handler import save_expenses, load_expenses

def main_menu():
    """
    Displays the main menu with options for the user.
    Returns the user's choice as a string.
    """
    # Print a nice title and a menu
    print("\n" + "=" * 40)
    print("           Expense Tracker")
    print("=" * 40)
    print("Track your daily expenses efficiently!")
    print("\nChoose an option below:")
    print("1. View my Finances")
    print("2. Add an Expense")
    print("3. Quick Add (default category: Misc)")
    print("4. Edit an Expense")
    print("5. Save and Exit")

    # Ask the user for their choice (strip removes extra spaces)
    choice = input("\nEnter your choice (1-5, or press Enter for 'Quick Add'): ").strip()

    # If the user presses Enter without typing anything, we default to Quick Add
    if choice == "":
        return "3"  # Default to Quick Add if nothing is entered
    
    # Return whatever the user input (their choice)
    return choice

def main():
    """
    Main function to run the expense tracker.
    Loads saved expenses and handles user input for actions.
    """
    # Load expenses from file (if the file exists, otherwise start with an empty dictionary)
    expenses = load_expenses()

    # Loop to continuously display the menu and respond to user choices
    while True:
        # Call the main_menu function to get the user's choice
        choice = main_menu()

        # Check what the user's choice is and act accordingly
        if choice == "1":
            view_totals(expenses)  # Call the function to view total expenses
        elif choice == "2":
            add_expense(expenses)  # Call the function to add an expense
        elif choice == "3":
            quick_add_expense(expenses)  # Call the function to quickly add an expense (no category)
        elif choice == "4":
            edit_expense(expenses)  # Call the function to edit an existing expense
        elif choice == "5":
            # Save the current expenses to file and exit the loop (ending the program)
            save_expenses(expenses)
            print("Expenses saved! Exiting...")
            break
        else:
            # If the user enters an invalid choice, show this message and ask again
            print("Invalid choice. Please enter a number between 1 and 5.")

# Check if the script is being run directly (and not imported as a module)
if __name__ == "__main__":
    main()  # Call the main function to start the program

