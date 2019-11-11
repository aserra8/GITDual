import os
import mysql.connector
from classes import player
from program import database


# Class to store questions data
class Question:
    # Constructor with questions atributes
    def __init__(self, question_challenge_id, question_content, question_answer, question_score):
        self.question_challenge_id = question_challenge_id
        self.question_content = question_content
        self.question_answer = question_answer
        self.question_score = question_score

    @staticmethod
    def get_questions(question_challenge_id, current_player):
        dbcon = None
        cursor = None
        choice = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute("SELECT * FROM question WHERE question_challenge_id = '{}'".format(question_challenge_id))
            result = cursor.fetchall()

            for row in result:
                choice = 0
                while True:
                    os.system("cls")
                    print("{:<64}{:>8}{:>3}".format("QUESTION", "POINTS: ", row[4]))
                    print(75 * "-")
                    print("\n" + row[2] + "\n")
                    print(75 * "-" + "\n")

                    user_answer = input("ANSWER: ")
                    if user_answer.casefold() == row[3].casefold():
                        points = row[4]
                        player.Player.update_player_score(points, current_player)
                        os.system("cls")
                        print(30 * "-", "CORRECT ANSWER", 30 * "-")
                        print("\nQuestion points: ", row[4])
                        print("Current team score: ", player.Player.get_player_score(current_player))
                        input("\nEnter a key to continue: ")
                        break
                    else:
                        while True:
                            try:
                                choice = int(input("\nIncorrect answer. Continue? 1 = YES / 2 = NO: "))
                                if choice == 1 or choice == 2:
                                    break
                                print("\nIncorrect option")
                            except ValueError:
                                print("\nIncorrect format")

                    if choice == 2:
                        break

            if choice != 2:
                os.system("cls")
                print("\t\t\tCHALLENGE COMPLETED\n", 74 * "-")
                input("\nEnter a key to continue: ")

        except mysql.connector.Error:
            print("\nException trying to find questions")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def list_questions(challenge_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()
            cursor.execute("SELECT * FROM question WHERE question_challenge_id = '{}'".format(challenge_id))

            result = cursor.fetchall()

            os.system("cls")
            print("{:<15}{:<75}{:>5}".format("ID", "CONTENT", "SCORE"))
            print(95 * "-")

            for row in result:
                print("{:<15}{:<75}{:>5}".format(row[0], row[2], row[4]))

            print(95 * "-")

        except mysql.connector.Error:
            print("\nException while listing questions")

        finally:
            if dbcon.is_connected:
                cursor.close()
                dbcon.close()

    @staticmethod
    def modify_question(question_id, option, modification):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            if option == 1:
                sql = "UPDATE question SET question_content = %s WHERE question_id = %s"
                var = (modification, question_id)
                cursor.execute(sql, var)
            elif option == 2:
                sql = "UPDATE question SET question_answer = %s WHERE question_id = %s"
                var = (modification, question_id)
                cursor.execute(sql, var)
            elif option == 3:
                sql = "UPDATE question SET question_score = %s WHERE question_id = %s"
                var = (modification, question_id)
                cursor.execute(sql, var)

            dbcon.commit()

            print("\nQuestion modified successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nException while trying to modify question")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def delete_question(question_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute("DELETE FROM question WHERE question_id = '{}'".format(question_id))

            dbcon.commit()

            print("\nQuestion deleted successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nException while trying to delete question")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    # Method to add question to the database
    def add_question(self):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            sql = "INSERT INTO question VALUES(default, %s, %s, %s, %s)"
            var = (self.question_challenge_id, self.question_content, self.question_answer, self.question_score)

            cursor.execute(sql, var)
            dbcon.commit()

            print("\nQuestion successfully added")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nError trying to add question")
            input("Enter a key to continue: ")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def check_question(question_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()
            cursor.execute("SELECT * FROM question WHERE question_id = '{}'".format(question_id))

            row = cursor.fetchone()

            if row is not None:
                return True

        except mysql.connector.Error:
            print("\nException while trying to find question")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()
