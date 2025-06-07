import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character sets selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🛡️ Welcome to the Password Generator 🛡️")
length = int(input("Enter password length: "))

print("\nInclude the following in your password:")
use_upper = input("Uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Numbers? (y/n): ").lower() == 'y'
use_symbols = input("Special characters? (y/n): ").lower() == 'y'

password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
print("\nYour generated password is:", password)
