def calculate_total(items, discount_percent=0):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    return total * (1 - discount_percent / 100)
