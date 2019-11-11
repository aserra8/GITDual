import os
from classes import question, challenge, getinput
from program import challenges


# TODO (BUG) Delete and modify allow to select questions from other challenges!!!
def delete_existing_question(challenge_id):
    if challenge.Challenge.contains_questions(challenge_id):
        question.Question.list_questions(challenge_id)
        try:
            question_id = int(input("\nEnter question ID: "))
            if not question.Question.check_question(question_id):
                print("\nIncorrect question ID")
                input("Enter a key to continue: ")
            else:
                question.Question.delete_question(question_id)
        except ValueError:
            print("\nIncorrect format")
            input("Enter a key to continue: ")
    else:
        print("\nThis challenge doesn't contain any question")
        input("Enter a key to continue: ")


def modify_existing_question(challenge_id):
    if not challenge.Challenge.contains_questions(challenge_id):
        print("\nThis challenge doesn't contain any question")
        input("Enter a key to continue: ")
    else:
        question.Question.list_questions(challenge_id)
        try:
            question_id = int(input("\nEnter question ID: "))
            if question.Question.check_question(question_id):
                os.system("cls")
                print(30 * "-", "MODIFY QUESTION", 30 * "-")
                try:
                    option = int(input("\nField to be changed: 1 = CONTENT / 2 = ANSWER / 3 = SCORE"))
                    if 1 <= option <= 3:
                        if option == 1:
                            while True:
                                modification = input("\nQuestion: ")
                                if len(modification) < 5:
                                    print("\nQuestion is too short")
                                elif len(modification) > 75:
                                    print("\nQuestion is too long")
                                else:
                                    break
                        elif option == 2:
                            while True:
                                modification = input("Answer: ")
                                if modification == "":
                                    print("\nAnswer is not valid")
                                elif len(modification) > 30:
                                    print("\nAnswer is too long")
                                else:
                                    break
                        else:
                            while True:
                                try:
                                    modification = int(input("Score [100-500]: "))
                                    if modification < 100:
                                        print("\nScore is too low")
                                    elif modification > 500:
                                        print("\nScore is too high")
                                    else:
                                        break
                                except ValueError:
                                    print("\nIncorrect format")
                        question.Question.modify_question(question_id, option, modification)
                    else:
                        print("\nIncorrect question ID")
                        input("Enter a key to continue: ")
                except ValueError:
                    print("\nIncorrect format")
                    input("Enter a key to continue: ")
            else:
                print("\nIncorrect question ID")
                input("Enter a key to continue: ")
        except ValueError:
            print("\nIncorrect format")
            input("Enter a key to continue: ")


# Function to add a new question to the database
def add_new_question(challenge_id):
    os.system("cls")
    print(30 * "-", "NEW QUESTION", 30 * "-")
    while True:
        content = input("\nQuestion: ")
        if len(content) < 5:
            print("\nQuestion is too short")
        elif len(content) > 75:
            print("\nQuestion is too long")
        else:
            break

    while True:
        answer = input("Answer: ")
        if answer == "":
            print("\nAnswer is not valid")
        elif len(answer) > 30:
            print("\nAnswer is too long")
        else:
            break

    while True:
        try:
            score = int(input("Score [100-500]: "))
            if score < 100:
                print("\nScore is too low")
            elif score > 500:
                print("\nScore is too high")
            else:
                break
        except ValueError:
            print("\nIncorrect format")

    while True:
        try:
            choice = int(input("\nDo you want to add this question? 1 = YES / 2 = NO: "))
            if choice == 1:
                new_question = question.Question(challenge_id, content, answer, score)
                new_question.add_question()
                break
            elif choice == 2:
                break
            else:
                print("\nIncorrect option")
        except ValueError:
            print("\nIncorrect format")


# Function to show question menu
def show_question_options(challenge_id):
    while True:
        os.system("cls")
        print(30 * "-", "QUESTION MENU", 30 * "-")
        print("1. ADD NEW QUESTION")
        print("2. MODIFY QUESTION")
        print("3. DELETE QUESTION")
        print("4. MAIN MENU")
        print(75 * "-")

        choice = getinput.getinput_between(1, 4)

        if choice == 1:
            add_new_question(challenge_id)
        elif choice == 2:
            modify_existing_question(challenge_id)
        elif choice == 3:
            delete_existing_question(challenge_id)
        else:
            break
