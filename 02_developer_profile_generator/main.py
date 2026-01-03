import datetime
from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator 

def main():
    name = inquirer.text(
        message="Enter Your Name:",
        validate=EmptyInputValidator("Name cannot be empty ! Try again...")
    ).execute()

    age = inquirer.number(
        message="Enter your age:",
        validate=EmptyInputValidator("Age cannot be empty! ")
    ).execute()

    age = int(age)
    if 10<age<80:
        pass
    else:
        print("Age should be greater than 10 and less than 80 , please enter valid age")
        main()

    city = inquirer.text(
        message="Enter Your Current City:",
        validate=EmptyInputValidator("Your current city location can't be empty!")
    ).execute()

    role = inquirer.select(
        message="Select Your Current Role:",
        choices=[
            "Student",
            "Working Professional person"
        ]
    ).execute()

    skills = inquirer.checkbox(
        message = "Please check all your current skills(NOTE. click space to select): ",
        choices=[
            "Python",
            "C++",
            "Java",
            "JavaScript",
            "DSA",
            "Machine Learning",
            "Web Development",
            "Databases"
        ],
        validate=lambda result: len(result) > 0 or "Select at least one skill"
    ).execute()

    experience_level = inquirer.select(
        message="Please Select One Skill Level from the below: ",
        choices = ['Beginner','Intermediate','Advanced']
    ).execute()

    hobby = inquirer.text(
        message = "Enter your 1 specific hobby: "
    ).execute()

    email = inquirer.text(
        message = "Enter your Email-ID: ",
        validate = EmptyInputValidator("Email can be empty , give appropriate Email-ID")
    ).execute()


    confirm = inquirer.confirm(
        message = "Do you want to confirm all your changes?",
        default = True
    ).execute()

    if confirm:
        date_format = "%d-%m-%Y"
        current_date = datetime.date.today().strftime(date_format)
        time_format = "%H:%M:%S"
        current_time = datetime.datetime.now().strftime(time_format)
        print("\n")
        print("*"*25)
        print("✅ Developer Profile Generated\n")
        print(f"""Hello! my name is {name} , I'm {age} year's old currently living in {city} city.\nI am  a {role} and I absolutely enjoy {hobby} in my free time.\nMy skills are {' , '.join(skills)}. \nI am now at {experience_level} experience level on my skills.\nContact me: {email} \nNice to meet You!\nLet's Connect On GitHub , LinkedIn and on other platforms!\n""")
        print(f"Logged on: \n - {current_date}\n - {current_time}")
        print("*"*25)
    else:
        print("Try again")


if __name__ == "__main__":
    while True:
        print("\n")
        print("~"*20)
        print("Welcome to Developer Profile Generator")
        print("~"*20)
        print("1.Generate a developer profile")
        print("2.Quit")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                main()
            case 2: 
                break

    
