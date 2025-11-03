# rock_paper_scissors.py
from random import randrange

def main():
    print("Welcome to Rock, Paper, Scissors!")

    # Variable to control the game loop
    continue_game = "y"

    while continue_game.lower() == "y":
        # Get the user's weapon
        user_weapon = get_user_weapon()

        # Get the opponent's weapon
        opponent_weapon = get_opponent_weapon()

        # Display the choices
        print(f"\nYou chose: {weapon_name(user_weapon)}")
        print(f"The opponent chose: {weapon_name(opponent_weapon)}")

        # Determine and display the result
        determine_winner(user_weapon, opponent_weapon)

        # Ask if user wants to continue
        continue_game = input("\nWould you like to play again? (y/n): ")

    print("\nThanks for playing Rock, Paper, Scissors!")
    print("Completed by, [Isaac Davis]")


# ------------------------------------------------------
# Function to get user's weapon
def get_user_weapon():
    print("\nChoose your weapon:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    while True:
        try:
            choice = int(input("Enter the number of your choice (1-3): "))
            if choice in (1, 2, 3):
                return choice
            else:
                print("Invalid selection. Please choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number (1, 2, or 3).")


# ------------------------------------------------------
# Function to get opponent's weapon
def get_opponent_weapon():
    # Generate random number between 1 and 3
    opponent_choice = randrange(1, 4)
    return opponent_choice


# ------------------------------------------------------
# Function to determine the winner
def determine_winner(user, opponent):
    if user == opponent:
        print("It's a tie!")
    elif (user == 1 and opponent == 3) or \
         (user == 2 and opponent == 1) or \
         (user == 3 and opponent == 2):
        print("You win!")
    else:
        print("You lose!")


# ------------------------------------------------------
# Helper function to display the name of the weapon
def weapon_name(num):
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    elif num == 3:
        return "Scissors"


# ------------------------------------------------------
# Call main using the __name__ method
if __name__ == "__main__":
   main() 