import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    
    secret_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    attempts = 0

    while True:
        try:
            user_guess = int(input("Enter your guess: "))  # User inputs a number
            attempts += 1  # Increase attempt count

            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
        
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                break  # Exit the loop if the guess is correct

        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Run the game
guess_the_number()
