# Loop Engineering Python Demo

A small Python project to test the idea of Loop Engineering with an AI coding agent.

The goal of this project is not to build a complex application.

The goal is to demonstrate a simple engineering loop:

```text
Specification → Agent reads task → Agent writes code → Run tests → Read errors → Fix code → Tests pass → Save result
```

## What is this project about?

This project contains a small Python function for calculating the total price of a shopping cart.

The function should:

* calculate price * quantity for each item
* apply a discount if `discount_percent` is provided
* return the final total as a number

The project is intentionally simple, so the main focus is not the code itself, but the workflow around the code.

## Project structure

```text
loop-engineering-python-demo/
├── AGENTS.md
├── README.md
├── docs/
│   └── SPEC.md
├── skills/
│   └── cart-development.md
├── src/
│   ├── __init__.py
│   └── cart.py
└── tests/
    ├── __init__.py
    └── test_cart.py
```

## The loop

This demo is based on the following loop:

```text
1. Write a clear specification
2. Create a broken implementation
3. Write tests that describe the expected behavior
4. Run tests
5. Read the error message
6. Fix the implementation
7. Run tests again
8. Stop only when all tests pass
```

## Specification

The main specification is in:

```text
docs/SPEC.md
```

It describes the expected behavior of the function:

```python
calculate_total(items, discount_percent=0)
```

Example:

```python
items = [
    {"name": "Book", "price": 10, "quantity": 2},
    {"name": "Pen", "price": 5, "quantity": 1},
]
```

Expected result without discount:

```text
25
```

Expected result with 10% discount:

```text
22.5
```

## Running the project locally

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install pytest
```

Run tests:

```bash
pytest
```

## Broken implementation

The project starts with a broken implementation:

```python
def calculate_total(items, discount_percent=0):
    total = 0

    for item in items:
        total += item["price"]

    return total
```

This implementation is wrong because it:

* ignores `quantity`
* ignores `discount_percent`

So the first test run should fail.

Example failure:

```text
Expected: 25
Actual: 15
```

This is intentional.

The failing tests are the feedback mechanism for the loop.

## Correct implementation

The correct implementation should look like this:

```python
def calculate_total(items, discount_percent=0):
    total = 0

    for item in items:
        total += item["price"] * item["quantity"]

    discount = total * (discount_percent / 100)

    return total - discount
```

After this fix, all tests should pass:

```text
3 passed
```

## Agent instructions

The project includes an `AGENTS.md` file with instructions for an AI coding agent.

The agent should:

* read `docs/SPEC.md`
* not change tests
* update only the implementation
* run `pytest`
* read test errors
* fix the code
* stop only when all tests pass

## Skill file

The project also includes a small skill file:

```text
skills/cart-development.md
```

This file describes project-specific rules for cart calculation logic.

For example:

* do not forget quantity
* apply discount after calculating the full total
* return a number, not a string

## Why this demo exists

This project was created as a small experiment to understand Loop Engineering in practice.

The main idea is:

AI-assisted development is not only about writing better prompts.

It is about designing better systems around agents.

A good loop gives the agent:

* context
* rules
* tests
* feedback
* a clear stopping condition

The developer is still responsible for understanding the specification, reviewing the result, and making sure the system is correct.

## Main lesson

Do not just ask an AI agent to write code.

Give it a loop.

```text
specification → code → tests → feedback → fix → verified result
```

Build the loop.

But stay the engineer.
