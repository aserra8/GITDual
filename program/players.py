import os
from classes import player, getinput


def delete_existing_player():
    player.Player.list_players()

    player_name = input("\nEnter player name: ")
    if player.Player.check_player_name(player_name):
        player.Player.delete_player(player_name)
    else:
        print("\nPlayer does not exist")
        input("Enter a key to continue: ")


def modify_existing_player():
    os.system("cls")
    print(28 * "-", "MODIFY PLAYER", 28 * "-")
    player.Player.list_players()

    player_name = input("\nEnter player name: ")
    if player_name.upper() == "ADMIN":
        print("\nThis player can not be modified")
        input("Enter a key to continue: ")
    elif player.Player.check_player_name(player_name):
        os.system("cls")
        print(26 * "-", "MODIFY PLAYER", 27 * "-")
        try:
            option = int(input("\nField to be changed: 1 = PLAYER NAME / 2 = PLAYER PASSWORD / 3 = PLAYER SCORE: "))
            if 1 <= option <= 3:
                if option == 1:
                    modification = getinput.string_input_between("Player name", 3, 10)
                elif option == 2:
                    modification = getinput.string_input_between("Player password", 3, 10)
                else:
                    while True:
                        try:
                            modification = int(input("Player score: "))
                            if modification < 0:
                                print("\nScore is too low")
                            else:
                                break
                        except ValueError:
                            print("\nIncorrect format")
                player.Player.modify_player(player_name, option, modification)
            else:
                print("\nIncorrect question ID")
                input("Enter a key to continue: ")
        except ValueError:
            print("\nIncorrect format")
            input("Enter a key to continue: ")
    else:
        print("\nPlayer doesn't exist")
        input("Enter a key to continue: ")


def show_player_options():
    while True:
        os.system("cls")
        print(25 * "-", "PLAYER OPTIONS", 25 * "-")
        print("1. ADD NEW PLAYER")
        print("2. MODIFY PLAYER")
        print("3. DELETE PLAYER")
        print("4. GO BACK")
        print(66 * "-")

        choice = getinput.int_input_between(1, 4)
        if choice == 1:
            add_new_player(1)
        elif choice == 2:
            modify_existing_player()
        elif choice == 3:
            delete_existing_player()
        else:
            break


def check_existing_player():
    os.system("cls")
    print(25 * "-", "EXISTING PLAYER", 24 * "-")

    player_name = input("\nEnter player name: ")
    player_password = input("Enter player password: ")

    if player.Player.check_player(player_name, player_password):
        existing_player = player.Player(player_name, player_password)
        return existing_player
    else:
        print("\nPlayer name or password incorrect")
        input("Enter a key to continue: ")


def add_new_player(option):
    os.system("cls")
    print(27 * "-", "NEW PLAYER", 27 * "-")

    player_name = getinput.string_input_between("Player name", 3, 10)
    player_password = getinput.string_input_between("Passowrd", 5, 15)

    if player.Player.check_player_name(player_name):
        print("\nPlayer name already exists")
        input("Enter a key to continue: ")
    else:
        new_player = player.Player(player_name, player_password)
        new_player.add_player()
        if option == 0:
            return new_player


def show_login():
    while True:
        os.system("cls")
        print(27 * "-", "PLAYER MENU", 26 * "-")
        print("1. EXISTING PLAYER")
        print("2. ADD NEW PLAYER")
        print("3. EXIT")
        print(66 * "-")

        choice = getinput.int_input_between(1, 3)

        if choice == 1:
            current_player = check_existing_player()
            if current_player is not None:
                break
        elif choice == 2:
            current_player = add_new_player(0)
            if current_player is not None:
                break
        elif choice == 3:
            exit()

    return current_player
