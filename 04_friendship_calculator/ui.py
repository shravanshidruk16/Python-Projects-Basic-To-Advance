import logging
from validator import get_valid_name
from calculator import friendship_score_calculator

def run_ui():
    print("\n" + "*" * 60)
    print("🧑‍🤝‍🧑 FRIENDSHIP COMPATIBILITY CALCULATOR 🧑‍🤝‍🧑")
    print("*" * 60)

    name1 = get_valid_name("Enter first name: ")
    name2 = get_valid_name("Enter second name: ")

    result = friendship_score_calculator(name1, name2)

    logging.info(f"Calculated score for {name1} & {name2}")

    print("\n📊 RESULT")
    print(f"Score: {result['score']}%")
    print(f"Shared Letters: {', '.join(result['shared_letters'])}")
    print(f"Shared Vowels: {', '.join(result['shared_vowels'])}")

    if result["score"] >= 75:
        print("🔥 Excellent Compatibility!")
    elif result["score"] >= 50:
        print("😊 Good Compatibility")
    elif result["score"] >= 25:
        print("😐 Average Compatibility")
    else:
        print("🥲 Low Compatibility")
