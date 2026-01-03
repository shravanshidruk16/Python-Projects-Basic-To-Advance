import datetime
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator 

def calculate_solution(age_in_years):
    DAYS_IN_YEARS = 365.25
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60

    total_days = DAYS_IN_YEARS * age_in_years
    total_hours = HOURS_IN_DAY * total_days
    total_minutes =  MINUTES_IN_HOUR * total_hours

    return round(total_days) , round(total_hours) , round(total_minutes)

if __name__ == "__main__":
    while True:
        print("\n")
        print("*"*20)
        print("Welcome to Minutes Alive Calculator")
        print("*"*20)
        print("1.Calculate")
        print("2.Quit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                try:
                    age = inquirer.number(
                        message = "Enter your current completed age:",
                        validate = EmptyInputValidator("Age cannot be negative")
                    ).execute()
                    age = float(age)
                    if 10<age<80:
                        total_days , total_hours , total_minutes = calculate_solution(age)
                        print("\nYou are approx:\n")
                        print(f" - {total_days} days old")
                        print(f" - {total_hours} hours old")
                        print(f" - {total_minutes} minutes old")
                    else:
                        print("Invalid age entered")
                except:
                    print("Error occured try again!")
            case 2:
                break
        
