def calculate_total(items, discount_percent=0) -> int:
    total = 0

    for item in items:
        total += item["price"]

    return total
