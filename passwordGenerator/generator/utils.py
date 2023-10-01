import random
import string

def gen_pass(length, capital_letter=False, numbers=False, special_characters=False):
    characters = string.ascii_lowercase

    if capital_letter:
        characters += string.ascii_uppercase 

    if numbers:
        characters += string.digits

    if  special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password