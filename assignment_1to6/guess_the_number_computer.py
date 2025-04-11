import random

def computer_guesses():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("Something went wrong! Did you change your number? 😅")
            break

        guess = random.randint(low, high)  # Computer makes a guess
        attempts += 1
        print(f"My guess is: {guess}")
    
        feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").strip().lower()

        if feedback == "c":
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts!")
            break
    
        elif feedback == "h":
            high = guess - 1  # Adjust range to lower half
        elif feedback == "l":
            low = guess + 1  # Adjust range to upper half
        else:
            print("❌ Invalid input! Please enter 'H' for high, 'L' for low, or 'C' for correct.")
      
# Run the game
computer_guesses()
