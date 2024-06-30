def main():

    task = input("Enter your task: ")
   
    priority = input("Priority (high/medium/low): ")
  
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    print("\nReminder:")
    
     match priority:
        case 'high':
            print(f"- Task: {task} (Priority: {priority})")
            if time_bound == 'yes':
                print("- This task requires immediate attention today!")
            else:
                print("- This task does not require immediate attention.")
        case 'medium':
            print(f"- Task: {task} (Priority: {priority})")
            if time_bound == 'yes':
                print("- This task requires immediate attention today!")
            else:
                print("- This task does not require immediate attention.")
        case 'low':
            print(f"- Task: {task} (Priority: {priority})")
            if time_bound == 'yes':
                print("- This task requires immediate attention today!")
            else:
                print("- This task does not require immediate attention.")
        case _:
            print("- Invalid priority level entered.")

if __name__ == "__main__":
    main()
