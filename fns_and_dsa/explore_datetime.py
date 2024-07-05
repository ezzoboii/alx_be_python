from datetime import datetime

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format the date and time as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted date and time
    print("Current date and time:", formatted_date)

display_current_datetime()
from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()

    # Format the date and time as YYYY-MM-DD HH:MM:SS
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted date and time
    print("Current date and time:", formatted_date)

def calculate_future_date():
    # Prompt the user to enter a number of days
    number_of_days = int(input("Enter the number of days to add to the current date: "))

    # Get current date
    current_date = datetime.now()

    # Calculate future date by adding number_of_days to current_date
    future_date = current_date + timedelta(days=number_of_days)

    # Format the future date as YYYY-MM-DD
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print("Future date:", formatted_future_date)

# Call the functions
display_current_datetime()
calculate_future_date()
