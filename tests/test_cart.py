from src.cart import calculate_total


def test_calculates_total_with_quantity():
    items = [
        {"name": "Book", "price": 10, "quantity": 2},
        {"name": "Pen", "price": 5, "quantity": 1},
    ]

    assert calculate_total(items) == 25


def test_applies_discount_percent():
    items = [
        {"name": "Book", "price": 10, "quantity": 2},
        {"name": "Pen", "price": 5, "quantity": 1},
    ]

    assert calculate_total(items, 10) == 22.5


def test_returns_zero_for_empty_cart():
    assert calculate_total([]) == 0