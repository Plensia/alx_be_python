task = input("Enter the task description: ")
priority = input("Enter the task priority (high/medium/low): ")
time_bound = input("Is the task time-bound? (yes/no): ")

reminder = f"Reminder: '{task}' is a {priority} priority task"

match priority:
    case "high":
        reminder += " that requires urgent attention"
    case "medium":
        reminder += " that should be addressed soon"
    case "low":
        reminder += " that can be handled later"
    case _:
        reminder = f"Invalid priority for '{task}'. Please use high, medium, or low."

if time_bound.lower() == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)