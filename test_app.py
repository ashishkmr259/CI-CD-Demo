from app import calculate_growth

def test_positive_growth():
    assert calculate_growth(100, 0.1) == 110

def test_zero_growth():
    assert calculate_growth(100, 0) == 100
