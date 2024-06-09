import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100. Can you guess it?")
    
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Set a fixed number of maximum attempts
    
    print(f"You have a maximum of {max_attempts} attempts to guess the correct number.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You've guessed the correct number {target_number} in {attempts} attempts.")
                break
            
            # Provide remaining attempts
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts left.")
            else:
                print(f"Sorry, you've used all your attempts. The correct number was {target_number}.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    print("Thank you for playing the Number Guessing Game!")

if __name__ == "__main__":
    number_guessing_game()
