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
            print(f"- Task: {task} (Priority: {priority})")
            if time_bound == 'yes':
                reminder += " This task is time-bound and requires immediate attention today!"
            else:
                reminder += " This task is time-bound and requires immediate attention today!"
        case 'low':
            print(f"- Task: {task} (Priority: {priority})")
             if time_bound == 'yes':
                reminder += " This task is time-bound and requires immediate attention today!"
            else:
                reminder += " This task is time-bound and requires immediate attention today!"
        case _:
            print("- Invalid priority level entered.")

if __name__ == "__main__":
    main()
