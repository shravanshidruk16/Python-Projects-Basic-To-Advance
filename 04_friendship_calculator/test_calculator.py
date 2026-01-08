from calculator import friendship_score_calculator

def test_score_is_not_negative():
    result = friendship_score_calculator("abc", "xyz")
    assert result["score"] >= 0

def test_shared_letters():
    result = friendship_score_calculator("Anna", "Anand")
    assert "a" in result["shared_letters"]

def test_score_cap():
    result = friendship_score_calculator("aaaaa", "aaaaa")
    assert result["score"] <= 100
