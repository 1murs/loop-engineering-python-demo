# Cart Total Specification

We need a small Python function for an online shop.

Function name:

calculate_total(items, discount_percent=0)

Rules:

1. Each item is a dictionary with:
   - name
   - price
   - quantity

2. Total price = price * quantity for each item.

3. If discount_percent is provided, apply it to the final total.

4. If discount_percent is missing, use 0.

5. The function should return a number.

Example:

items = [
    {"name": "Book", "price": 10, "quantity": 2},
    {"name": "Pen", "price": 5, "quantity": 1},
]

discount_percent = 10

Result:
22.5

Why:
10 * 2 = 20
5 * 1 = 5
Total = 25
Discount 10% = 2.5
Final total = 22.5

