def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    print('Reminder:')
    match priority:
        case 'high':
            Reminder = f"Task '{task}' is of '{priority}' priority."
            if time_bound == 'yes':
                Reminder += " This task is time-bound and requires immediate attention today!"
            else:
                Reminder += " This task does not require immediate attention."
        case 'medium':
            Reminder = f"Task '{task}' is of '{priority}' priority."
            if time_bound == 'yes':
                Reminder += " This task is time-bound and requires immediate attention today!"
            else:
                Reminder += " This task does not require immediate attention."
        case 'low':
            Reminder = f"Task '{task}' is of '{priority}' priority."
            if time_bound == 'yes':
                Reminder += " This task is time-bound and requires immediate attention today!"
            else:
                Reminder += " This task does not require immediate attention."
        case _:
            Reminder = f"Task '{task}' has an unrecognized priority level."
    
    print(Reminder)

if __name__ == "__main__":
    main()
