def main():
    task = input("Enter the your task : ")
    priority = input("priority(high, medium, low):")
    time_bound = input("Is it time-bound? (yes or no): ").lower()
    
    match priority:
        case "high":
            reminder = f"Task '{task}' is of high priority."
        case "medium":
            reminder = f"Task '{task}' is of medium priority."
        case "low":
            reminder = f"Task '{task}' is of low priority."
        case _:
            reminder = f"Task '{task}' has an unrecognized priority level."
             print("\nCustomized Reminder:")
    print("-" * 20)
    if time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an immediate time constraint."
    print(reminder)
if __name__ == "__main__":
    main()
