Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import random

def get_player_choice():
    print("\nChoose one of the following options:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    
    player_input = input("Enter your choice (1/2/3): ")
    
    if player_input == '1':
        return 'Rock'
    elif player_input == '2':
        return 'Paper'
    elif player_input == '3':
        return 'Scissors'
    else:
        print("Invalid input. Please enter 1, 2, or 3.")
        return get_player_choice()

def get_computer_choice():
    options = ['Rock', 'Paper', 'Scissors']
    return random.choice(options)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
...         return "It's a tie!"
...     elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
...          (player_choice == 'Paper' and computer_choice == 'Rock') or \
...          (player_choice == 'Scissors' and computer_choice == 'Paper'):
...         return "You win!"
...     else:
...         return "You lose!"
... 
... def play_game():
...     player_score = 0
...     computer_score = 0
...     while True:
...         player_choice = get_player_choice()
...         computer_choice = get_computer_choice()
...         
...         print(f"\nYou chose: {player_choice}")
...         print(f"Computer chose: {computer_choice}\n")
...         
...         result = determine_winner(player_choice, computer_choice)
...         print(result)
...         
...         if result == "You win!":
...             player_score += 1
...         elif result == "You lose!":
...             computer_score += 1
...         
...         print(f"Score: You {player_score} - {computer_score} Computer")
...         
...         play_again = input("\nDo you want to play again? (yes/no): ").lower()
...         if play_again != 'yes':
...             break
... 
...     print("\nFinal Score:")
...     print(f"You: {player_score}")
...     print(f"Computer: {computer_score}")
...     print("Thanks for playing!")
... 
... if __name__ == "__main__":
...     play_game()
