import random

options = ("rock", "paper", "scissors", "lizard", "spock")
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice (rock, paper, scissors, lizard, spock): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "rock" and computer == "lizard":
        print("Rock crushes lizard. You win!")
    elif player == "lizard" and computer == "spock":
        print("Lizard poisons spock. You win!")
    elif player == "scissors" and computer == "lizard":
        print("Scissors decapitates Lizard, You win!")
    elif player == "lizard" and computer == "paper":
        print("The lizard somehow eats paper, You win!")
    elif player == "paper" and computer == "spock":
        print("Paper disproves Spock, You Win!")
    elif player == "spock" and computer == "rock":
        print("Spock vaporizes rock, You Win!")
    elif player == "spock" and computer == "scissors":
        print("Spock smashes scissors, You Win!")
    else:
        print("You lose!")

    if not input("Play again? (yes or no): ").lower() == "yes":
        running = False

print("Thanks for playing!")
