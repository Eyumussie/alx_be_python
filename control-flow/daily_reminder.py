def main():
    Task = input("Enter your task : ")
     Time_bound = input("Is it time-bound? (yes / no): ").lower()
    Priority = input("Priority  (high/ medium/ low): ")
    print("\nCustomized Reminder:")
    print("-" * 20)
    match priority:
        case "high":
            reminder = f"Task '{task}' is of high priority task."
        case "medium":
            reminder = f"Task '{task}' is of medium priority task."
        case "low":
            reminder = f"Task '{task}' is of low priority task."
        case _:
            reminder = f"Task '{task}' has an unrecognized priority level."
    if time_bound == "yes":
        reminder += " This task is time-bound and requires immediate attention today!"
    else:
        reminder += " This task does not have an need to be done immediatly."
    print(reminder)
