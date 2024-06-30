def main():
   
    task = ( r"input\s*\(\s*['\"]Enter your task:\s*['\"]\s*\)")
    Time_bound = ( r"input\s*\(\s*['\"]Is it time-bound\?\s*\(yes\/no\):\s*['\"]\s*\)" )
   Priority = ( r"input\s*\(\s*['\"]Priority\s*\(high\/medium\/low\):\s*['\"]\s*\)" )


   
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
