import random as rn
print("Welcome to Rock, Paper, Scissor Game")
while True:
    user_input = input("Enter your choice (rock, paper, scissor) or 'exit' to quit: ").lower()
    if user_input == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    elif user_input not in ['rock', 'paper', 'scissor']:
        print("Invalid input. Please try again.")
        continue

    choices = ['rock', 'paper', 'scissor']
    computer_choice = rn.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == 'rock' and computer_choice == 'scissor') or (user_input == 'paper' and computer_choice == 'rock') or (user_input == 'scissor' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")
