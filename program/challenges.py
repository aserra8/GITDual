import os
from classes import question, challenge, getinput
from program import questions


def show_challenges_list(current_player):
    challenge.Challenge.list_challenge()
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if challenge.Challenge.check_challenge(challenge_id):
            if challenge.Challenge.contains_questions(challenge_id):
                question.Question.get_questions(challenge_id, current_player)
            else:
                print("\nThis challenge doesn't contain any question")
                input("Enter a key to continue: ")
        else:
            print("\nIncorrect ID")
            input("Enter a key to continue: ")
    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")


# Function to check if challenge ID already exists
def enter_existing_challenge():

    challenge.Challenge.list_challenge()
    while True:
        try:
            challenge_id = int(input("\nEnter challenge ID: "))
            break
        except ValueError:
            print("\nIncorrect option")

    if challenge.Challenge.check_challenge(challenge_id):
        return challenge_id
    else:
        print("\nIncorrect ID")
        input("Enter a key to continue: ")


def delete_existing_challenge():
    choice = None
    challenge.Challenge.list_challenge()
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if challenge.Challenge.check_challenge(challenge_id):
            if challenge.Challenge.contains_questions(challenge_id):
                print("\nChallenge contains questions. Delete anyways? 1 = YES / 2 = NO")
                while True:
                    try:
                        choice = int(input("\nEnter your choice: "))
                        if choice == 1 or choice == 2:
                            break
                        print("\nOption is not valid")
                    except ValueError:
                        print("\nIncorrect format")

            if choice != 2:
                challenge.Challenge.delete_challenge(challenge_id)
        else:
            print("\nChallenge doesn't exist")
            input("Enter a key to continue: ")
    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")


def modify_existing_challenge():

    challenge.Challenge.list_challenge()
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if challenge.Challenge.check_challenge(challenge_id):
            os.system("cls")
            print(30 * "-", "MODIFY CHALLENGE", 30 * "-")

            while True:
                modification = input("\nNew description: ")
                if len(modification) < 3:
                    print("\nChallenge description is too short")
                elif len(modification) > 30:
                    print("\nChallenge description is too long")
                else:
                    break

            challenge.Challenge.modify_challenge(challenge_id, modification)
        else:
            print("\nIncorrect challenge ID")
            input("Enter a key to continue: ")
    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")


# Function to add a new challenge ID
def add_new_challenge():
    os.system("cls")
    print(30 * "-", "NEW CHALLENGE", 30 * "-")
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if not challenge.Challenge.check_challenge(challenge_id):
            if len(str(challenge_id)) != 3:
                print("\nChallenge ID must be a three digit number")
                input("Enter a key to continue: ")
            else:
                while True:
                    challenge_description = input("\nEnter challenge description: ")
                    if len(challenge_description) < 3:
                        print("\nChallenge description is too short")
                    elif len(challenge_description) > 30:
                        print("\nChallenge description is too long")
                    else:
                        break

                new_challenge = challenge.Challenge(challenge_id, challenge_description)
                new_challenge.add_challenge()
                return challenge_id
        else:
            print("\nChallenge ID already exists")
            input("Enter a key to continue: ")

    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")


def show_challenge_options():
    while True:
        os.system("cls")
        print(30 * "-", "CHALLENGE OPTIONS", 30 * "-")
        print("1. ENTER EXISTING CHALLENGE")
        print("2. ADD NEW CHALLENGE")
        print("3. MODIFY CHALLENGE")
        print("4. DELETE CHALLENGE")
        print("5. GO BACK")
        print(79 * "-")

        choice = getinput.getinput_between(1, 5)

        if choice == 1:
            challenge_id = enter_existing_challenge()
            if challenge_id is not None:
                questions.show_question_options(challenge_id)
        elif choice == 2:
            challenge_id = add_new_challenge()
            if challenge_id is not None:
                questions.show_question_options(challenge_id)
        elif choice == 3:
            modify_existing_challenge()
        elif choice == 4:
            delete_existing_challenge()
        else:
            break
