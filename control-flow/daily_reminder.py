# daily_reminder.py

# Step 1: Prompt for the task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Step 2: Generate a reminder message based on priority and time-sensitivity
reminder_message = f"Reminder: '{task}' is a "

# Step 3: Use Match Case to handle priority levels
match priority:
    case "high":
        reminder_message += "high priority task"
    case "medium":
        reminder_message += "medium priority task"
    case "low":
        reminder_message += "low priority task"
    case _:
        print("Invalid priority level. Please enter high, medium, or low.")
        exit()

# Step 4: Check if the task is time-sensitive
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += ". Consider completing it when you have free time."
else:
    print("Invalid input for time sensitivity. Please enter yes or no.")
    exit()

# Step 5: Display the final reminder
print(reminder_message)

# End of the script
print\s*\(\s*f?['\"]Reminder:\s*
