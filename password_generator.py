import random
import string

def get_user_preferences():
    """Prompt the user for password settings."""
    try:
        length = int(input("Enter the desired password length (e.g., 12): "))
        if length <= 0:
            print("Password length must be positive.")
            return None

        include_letters = input("Include letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        if not (include_letters or include_digits or include_symbols):
            print("You must include at least one character type!")
            return None

        return length, include_letters, include_digits, include_symbols

    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

def generate_password(length, use_letters, use_digits, use_symbols):
    """Generate a random password based on user preferences."""
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Password Generator!")

    preferences = get_user_preferences()
    if preferences:
        length, use_letters, use_digits, use_symbols = preferences
        password = generate_password(length, use_letters, use_digits, use_symbols)
        print(f"\nYour generated password is:\n {password}")
main()
