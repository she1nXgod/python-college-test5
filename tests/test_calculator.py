import pytest
from calculator import calculate_simple_interest, calculate_compound_interest, calculate_tax


def test_simple_interest_basic():
    assert calculate_simple_interest(1000, 5, 2) == 100.0
    assert calculate_simple_interest(5000, 10, 3) == 1500.0


def test_simple_interest_zero():
    assert calculate_simple_interest(0, 5, 2) == 0.0


def test_simple_interest_negative():
    with pytest.raises(ValueError):
        calculate_simple_interest(-1000, 5, 2)


def test_compound_interest_basic():
    result = calculate_compound_interest(1000, 5, 2, 1)
    assert result == pytest.approx(1102.5)


def test_compound_interest_zero():
    assert calculate_compound_interest(0, 5, 2) == 0.0


def test_compound_interest_invalid_n():
    with pytest.raises(ValueError):
        calculate_compound_interest(1000, 5, 2, 0)


def test_tax_basic():
    assert calculate_tax(1000, 13) == 130.0
    assert calculate_tax(50000, 20) == 10000.0


def test_tax_zero():
    assert calculate_tax(0, 13) == 0.0


def test_tax_invalid_rate():
    with pytest.raises(ValueError):
        calculate_tax(1000, 101)