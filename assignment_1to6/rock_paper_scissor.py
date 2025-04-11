import random

def play():
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user = input("Choose Rock, Paper, or Scissors (or type 'quit' to exit): ").strip().lower()
        
        if user == "quit":
            print("Thanks for playing! Goodbye! 👋")
            break
        
        if user not in choices:
            print("❌ Invalid choice! Please enter Rock, Paper, or Scissors.")
            continue
        
        computer = random.choice(choices)  # Computer randomly selects
        print(f"Computer chose: {computer}")

        # Determine the winner
        if user == computer:
            print("🤝 It's a tie!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

# Run the game
play()
