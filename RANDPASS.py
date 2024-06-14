import string
import random


def generate_password(length, use_digits=True, use_punctuation=True):
    # Define the character sets
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    punctuation = string.punctuation if use_punctuation else ''

    # Combine the character sets
    char_set = letters + digits + punctuation

    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password


# Get user input
try:
    length = int(input("Enter the desired password length: "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_punctuation = input("Include punctuation? (y/n): ").lower() == 'y'

    # Generate and display the password
    print(f"Generated password: {generate_password(length, use_digits, use_punctuation)}")
except ValueError:
    print("Please enter a valid number for the password length.")
