import random

currencies = ["рублей", "тенге", "долларов", "евро"]

def get_donation():
    amount = random.randint(10, 50000)
    currency = random.choice(currencies)
    return f"Задонатил {amount} {currency}!"
