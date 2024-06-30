def main():

    task = input("Enter your task: ")
   
    priority = input("Priority (high/medium/low): ")
  
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    print("\nReminder:")
    
     match priority:
        case 'high':
           reminder = f"Task '{task}' is of high priority."
            if time_bound == 'yes':
                reminder += " This task is time-bound and requires immediate attention today!"
            else:
                reminder += " This task is time-bound and requires immediate attention today!"
        case 'medium':
            reminder = f"Task '{task}' is of medium priority."
            if time_bound == 'yes':
                reminder += " This task is time-bound and requires immediate attention today!"
            else:
                reminder += " This task is time-bound and requires immediate attention today!"
        case 'low':
            reminder = f"Task '{task}' is of low priority."
             if time_bound == 'yes':
                reminder += " This task is time-bound and requires immediate attention today!"
            else:
                reminder += " This task is time-bound and requires immediate attention today!"
        case _:
            reminder = f"Task '{task}' has an unrecognized priority level."
      print(reminder)
if __name__ == "__main__":
    main()
