import argparse
from calculator import friendship_score_calculator

def run_cli():
    parser = argparse.ArgumentParser(
        description="Friendship Compatibility Calculator"
    )

    parser.add_argument("--name1", required=True, help="First name")
    parser.add_argument("--name2", required=True, help="Second name")

    args = parser.parse_args()

    result = friendship_score_calculator(args.name1, args.name2)

    print("\n📊 RESULT")
    print(f"Score: {result['score']}%")
    print(f"Shared Letters: {', '.join(result['shared_letters'])}")
    print(f"Shared Vowels: {', '.join(result['shared_vowels'])}")
