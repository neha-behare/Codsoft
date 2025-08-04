# Task 2 - Password Generator App 🔐
# CodSoft Python Internship Project
# Author: Neha Behere
# Date: August 2025

import random
import string

def generate_password(length, include_letters=True, include_digits=True, include_symbols=True):
    characters = ''
    
    if include_letters:
        characters += string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        print("⚠️ No character types selected. Please enable at least one.")
        return ""

    # Randomly select characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main Program
if __name__ == "__main__":
    print("🔐 Welcome to the Password Generator App!")

    try:
        length = int(input("Enter the desired password length: "))
        
        if length <= 0:
            print("❌ Password length must be greater than 0.")
        else:
            print("\nSelect complexity options (Y/N):")
            use_letters = input("Include Letters? (Y/N): ").strip().lower() == 'y'
            use_digits = input("Include Digits? (Y/N): ").strip().lower() == 'y'
            use_symbols = input("Include Symbols? (Y/N): ").strip().lower() == 'y'

            password = generate_password(length, use_letters, use_digits, use_symbols)

            if password:
                print(f"\n✅ Your secure password is:\n{password}")
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
