
# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = f"'{task}' is a "

# Process the task based on priority
match priority:
    case "high":
        reminder += "high priority task"
    case "medium":
        reminder += "medium priority task"
    case "low":
        reminder += "low priority task"
    case _:
        reminder += "task with unspecified priority"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Print the customized reminder
print("\nReminder:", reminder)
