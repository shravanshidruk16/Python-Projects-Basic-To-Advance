from logger_config import setup_logger
from ui import run_ui
from cli import run_cli
import sys

def main():
    setup_logger()

    if len(sys.argv) > 1:
        run_cli()
    else:
        while True:
            print("\n1. Calculate Compatibility")
            print("2. Exit")
            choice = input("Enter choice: ")

            if choice == "1":
                run_ui()
            elif choice == "2":
                break
            else:
                print("❌ Invalid choice")

if __name__ == "__main__":
    main()
