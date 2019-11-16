import os
from classes import question, challenge, getinput


def delete_existing_question(challenge_id):
    if challenge.Challenge.contains_questions(challenge_id):
        question.Question.list_questions(challenge_id)
        try:
            question_id = int(input("\nEnter question ID: "))
            if not question.Question.check_question(question_id, challenge_id):
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
            if question.Question.check_question(question_id, challenge_id):
                os.system("cls")
                print(30 * "-", "MODIFY QUESTION", 30 * "-")
                try:
                    print("\nField to be changed: 1 = CONTENT / 2 = ANSWER / 3 = SCORE")
                    option = int(input("Enter your choice: "))
                    if 1 <= option <= 3:
                        if option == 1:
                            modification = getinput.string_input_between("Question", 5, 75)
                        elif option == 2:
                            modification = getinput.string_input_between("Answer", 1, 30)
                        else:
                            while True:
                                try:
                                    modification = int(input("\nEnter score [100 - 500]: "))
                                    if 100 <= modification <= 500:
                                        break
                                    else:
                                        print("\nScore is not valid")
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


def add_new_question(challenge_id):
    os.system("cls")
    print(30 * "-", "NEW QUESTION", 30 * "-")

    content = getinput.string_input_between("Question", 5, 75)
    answer = getinput.string_input_between("Answer", 1, 30)
    while True:
        try:
            score = int(input("\nEnter score [100 - 500]: "))
            if 100 <= score <= 500:
                break
            else:
                print("\nScore is not valid")
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


def show_question_options(challenge_id):
    while True:
        os.system("cls")
        print(30 * "-", "QUESTION MENU", 30 * "-")
        print("1. ADD NEW QUESTION")
        print("2. MODIFY QUESTION")
        print("3. DELETE QUESTION")
        print("4. GO BACK")
        print(75 * "-")

        choice = getinput.int_input_between(1, 4)

        if choice == 1:
            add_new_question(challenge_id)
        elif choice == 2:
            modify_existing_question(challenge_id)
        elif choice == 3:
            delete_existing_question(challenge_id)
        else:
            break
