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
        questions.show_question_options(challenge_id)
    else:
        print("\nIncorrect ID")
        input("Enter a key to continue: ")
        show_challenge_options()


def delete_existing_challenge():
    challenge_id = None
    challenge.Challenge.list_challenge()
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if not challenge.Challenge.check_challenge(challenge_id):
            print("\nChallenge doesn't exist")
            input("Enter a key to continue: ")
            show_challenge_options()
    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")
        show_challenge_options()

    if challenge.Challenge.contains_questions(challenge_id):
        print("\nChallenge contains questions. Delete anyways? 1 = YES / 2 = NO")
        while True:
            try:
                choice = int(input("\nEnter your choice: "))
                if choice == 1:
                    break
                if choice == 2:
                    show_challenge_options()
                print("\nOption is not valid")

            except ValueError:
                print("\nIncorrect format")

    challenge.Challenge.delete_challenge(challenge_id)
    show_challenge_options()


def modify_existing_challenge():
    challenge_id = None

    challenge.Challenge.list_challenge()
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if not challenge.Challenge.check_challenge(challenge_id):
            print("\nIncorrect challenge ID")
            input("Enter a key to continue: ")
            show_challenge_options()
    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")
        show_challenge_options()

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


# Function to add a new challenge ID
def add_new_challenge():
    os.system("cls")
    print(30 * "-", "NEW CHALLENGE", 30 * "-")
    challenge_id = None
    try:
        challenge_id = int(input("\nEnter challenge ID: "))
        if challenge.Challenge.check_challenge(challenge_id):
            print("\nChallenge ID already exists")
            input("Enter a key to continue: ")
            show_challenge_options()
        elif len(str(challenge_id)) != 3:
            print("\nChallenge ID must be a three digit number")
            input("Enter a key to continue: ")
            show_challenge_options()

    except ValueError:
        print("\nIncorrect format")
        input("Enter a key to continue: ")
        show_challenge_options()

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
    questions.show_question_options(challenge_id)


def show_challenge_options():
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
        enter_existing_challenge()
    elif choice == 2:
        add_new_challenge()
    elif choice == 3:
        modify_existing_challenge()
    elif choice == 4:
        delete_existing_challenge()
