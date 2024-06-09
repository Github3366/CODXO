import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    digit_chars = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special else ''
    
    # Combine all selected character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars
    
    if not all_chars:
        raise ValueError("No character types selected. Please select at least one character type.")

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    
    return password

def password_generator():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(length, use_uppercase, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    password_generator()
