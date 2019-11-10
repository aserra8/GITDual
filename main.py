import os
from classes import getinput
from program import challenges, players, ranking

# TODO Penalty points for wrong answer
# TODO Go back to menu if wrong input (add new player)


# Function to print menu
def print_menu():
    os.system("cls")
    print(30 * "-", "MENU", 30 * "-")
    print("1. VIEW CHALLENGES")
    print("2. VIEW LEADERBOARD")
    print("3. MANAGE CHALLENGES")
    print("4. EXIT")
    print(66 * "-")


# Function to print main menu
def main_menu(current_player):
    print_menu()
    choice = getinput.getinput_between(1, 4)

    if choice == 1:
        challenges.show_challenges_list(current_player)
    elif choice == 2:
        ranking.show_player_leaderboard()
    elif choice == 3:
        challenges.show_challenge_options()
    elif choice == 4:
        exit()


# Starts executing
# Prints login options
player = players.show_login()

# Prints main menu
flag = True
while flag:
    main_menu(player)
