def main():
    task = input("Enter the task description: ")
    priority = input("Enter the priority level (high, medium, low): ")
    time_bound = input("Is the task time-bound? (yes or no): ").lower()
    print("\nCustomized Reminder:")
    print("-" * 20)
    match priority:
        case "high":
            reminder = f"Task '{task}' is of high priority."
             if time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an immediate time constraint."
        case "medium":
            reminder = f"Task '{task}' is of medium priority."
         if time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an immediate time constraint."
        case "low":
            reminder = f"Task '{task}' is of low priority."
         if time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an immediate time constraint."
        case _:
            reminder = f"Task '{task}' has an unrecognized priority level."
    if time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an immediate time constraint."
    print(reminder)
if __name__ == "__main__":
    main()
