import os
from classes import player, getinput


# Function to show existing player menu
def check_existing_player():
    os.system("cls")
    print(30 * "-", "EXISTING PLAYER", 30 * "-")
    player_name = input("\nEnter player name: ")
    player_password = input("Enter player password: ")

    existing_player = player.Player(player_name, player_password)

    if existing_player.check_player():
        return existing_player
    else:
        print("\nPlayer name or password incorrect")
        input("Enter a key to continue: ")
        show_login()


# Function to add new player
def add_new_player():
    os.system("cls")
    print(30 * "-", "NEW PLAYER", 30 * "-")
    while True:
        player_name = input("\nEnter player name: ")
        if len(player_name) < 3:
            print("\nPlayer name is too short")
        elif len(player_name) > 10:
            print("\nPlayer name is too long")
        else:
            break

    while True:
        player_password = input("Enter player password: ")
        if len(player_password) < 5:
            print("\nPassword is too short")
        elif len(player_password) > 15:
            print("\nPassword is too long")
        else:
            break

    new_player = player.Player(player_name, player_password)
    new_player.add_player()

    return new_player


# Function to show player login options
def show_login():
    os.system("cls")
    print(30 * "-", "PLAYER MENU", 30 * "-")
    print("1. EXISTING PLAYER")
    print("2. CREATE NEW PLAYER")
    print("3. EXIT")
    print(73 * "-")

    choice = getinput.getinput_between(1, 3)

    if choice == 1:
        current_player = check_existing_player()
        return current_player
    elif choice == 2:
        current_player = add_new_player()
        return current_player
    elif choice == 3:
        exit()
