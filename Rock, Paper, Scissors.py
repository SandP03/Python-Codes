player_wins = 0
computer_wins = 0
ties = 0
player_choices = {'R': 0, 'P': 0, 'S': 0}

# Define the rules
RULES = {
    "scissors": {"paper": "cut"},
    "paper": {"rock": "covers"},
    "rock": {"scissors": "breaks"}
}

# This starts the loop for the main game
gameon = True
while gameon:
    player_input = input("Enter R for Rock, P for Paper, S for Scissors, or Q to quit: ").upper()
    
    if len(player_input) != 1:
        print("Invalid input, please enter a single character.")
    elif player_input not in ['R', 'P', 'S', 'Q']:
        print("Invalid input, please try again.")
    elif player_input == 'Q':
        gameon = False
    else:
        player_choices[player_input] += 1
        
        # This determines the computer's choice based the users previous inputs
        if player_choices['R'] > player_choices['P']:
            if player_choices['R'] > player_choices['S']:
                comp_choice = 'P'  # Paper beats Rock
            else:
                comp_choice = 'R'  # Rock beats Scissors
        elif player_choices['P'] > player_choices['S']:
            comp_choice = 'S'  # Scissors beat Paper
        else:
            comp_choice = 'R'  # Rock beats Scissors

        if player_choices['R'] == player_choices['P'] == player_choices['S']:
            import random
            comp_choice = random.choice(['R', 'P', 'S'])

        player_full = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}[player_input]
        comp_full = {'R': 'rock', 'P': 'paper', 'S': 'scissors'}[comp_choice]

        print("Computer chose: " + comp_full)

        if player_full == comp_full:
            ties += 1
            print("It's a tie!")
        elif comp_full in RULES[player_full]:
            player_wins += 1
            print(player_full.capitalize() + " " + RULES[player_full][comp_full] + " " + comp_full.capitalize() + ". You win!")
        else:
            computer_wins += 1
            print(comp_full.capitalize() + " " + RULES[comp_full][player_full] + " " + player_full.capitalize() + ". Computer wins!")


print()
print("Game Summary:")
print("Rounds you won: " + str(player_wins))
print("Rounds computer won: " + str(computer_wins))
print("Rounds tied: " + str(ties))
print("Your choices: Rock - " + str(player_choices['R']) + ", Paper - " + str(player_choices['P']) + ", Scissors - " + str(player_choices['S']))
