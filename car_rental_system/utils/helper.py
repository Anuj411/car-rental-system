
import random

def generate_unique_username(first_name):
    special_character = random.choice(['+', '-', '@', '_'])
    digits = random.randint(100, 99999)
    username = f"{first_name.lower()}{special_character}{digits}"
    return username