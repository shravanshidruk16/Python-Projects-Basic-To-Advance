LETTER_WEIGHT = 5
VOWEL_WEIGHT = 10
VOWELS = set("aeiou")

def friendship_score_calculator(name1: str, name2: str) -> dict:
    name1, name2 = name1.lower(), name2.lower()

    shared_letters = set(name1) & set(name2)
    shared_vowels = shared_letters & VOWELS

    score = (
        len(shared_letters) * LETTER_WEIGHT +
        len(shared_vowels) * VOWEL_WEIGHT
    )

    score = min(score, 100)  # Normalize to 100%

    return {
        "score": score,
        "shared_letters": sorted(shared_letters),
        "shared_vowels": sorted(shared_vowels)
    }
