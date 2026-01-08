def get_valid_name(prompt: str) -> str:
    while True:
        name = input(prompt).strip()
        if name.isalpha():
            return name
        print("❌ Invalid input. Please enter alphabets only.")
