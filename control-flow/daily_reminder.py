def main():
   
   
    Task = input("Enter the task description: ")
    Priority = input(" Priority level (high, medium, low): ")
    Time_bound = input("Is it time-bound? (yes or no): ").lower()

   
    match Priority:
        case "high":
            reminder = f"Task '{Task}' is of high priority."
        case "medium":
            reminder = f"Task '{Task}' is of medium priority."
        case "low":
            reminder = f"Task '{Task}' is of low priority."
        case _:
            reminder = f"Task '{Task}' has an unrecognized priority level."

 
    if Time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an immediate time constraint."

    print(reminder)

if __name__ == "__main__":
    main()
