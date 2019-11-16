import os
import mysql.connector
from classes import player
from program import database


class Question:
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
                if not Question.__check_completed_question(row[0], current_player.player_name):
                    while True:
                        os.system("cls")
                        print("{:<64}{:>8}{:>3}".format("QUESTION", "POINTS: ", row[4]))
                        print(75 * "-")
                        print("\n" + row[2] + "\n")
                        print(75 * "-" + "\n")

                        user_answer = input("ANSWER: ")
                        points = row[4]
                        if user_answer.casefold() == row[3].casefold():
                            if not Question.__check_completed_question(row[0], current_player.player_name):
                                player.Player.update_player_score(points, current_player, 0)
                                Question.__add_completed_question(row[0], current_player.player_name)
                                os.system("cls")
                                print(30 * "-", "CORRECT ANSWER", 30 * "-")
                                print("\nQuestion points: ", row[4])
                                print("Current team score: ", player.Player.get_player_score(current_player))
                                input("\nEnter a key to continue: ")
                                break
                            else:
                                print("\nQuestion has already been completed")
                                input("\nEnter a key to continue: ")
                        else:
                            while True:
                                try:
                                    player.Player.update_player_score(points, current_player, 1)
                                    os.system("cls")
                                    print(29 * "-", "INCORRECT ANSWER", 29 * "-")
                                    print("\nPenalty points: -{}".format(round((row[4]*5)/100)))
                                    print("Current team score:", player.Player.get_player_score(current_player))
                                    choice = int(input("\nIncorrect answer. Continue? 1 = YES / 2 = NO: "))
                                    if choice == 1 or choice == 2:
                                        break
                                    print("\nIncorrect option")
                                except ValueError:
                                    print("\nIncorrect format")

                        if choice == 2:
                            break
                if choice == 2:
                    break
            if choice != 2:
                os.system("cls")
                print("{:>50}".format("CHALLENGE COMPLETED"))
                print(75 * "-")
                input("\nEnter a key to continue: ")

        except mysql.connector.Error:
            print("\nException trying to find questions")
            input("Enter a key to continue: ")

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
            print("{:<10}{:<75}{:30}{:>5}".format("ID", "CONTENT", "ANSWER", "SCORE"))
            print(120 * "-")

            for row in result:
                print("{:<10}{:<75}{:30}{:>5}".format(row[0], row[2], row[3], row[4]))

            print(120 * "-")

        except mysql.connector.Error:
            print("\nException while listing questions")
            input("Enter a key to continue: ")

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
            input("Enter a key to continue: ")

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

            cursor.execute("DELETE FROM question_completed WHERE question_completed_question_id = '{}'"
                           .format(question_id))
            cursor.execute("DELETE FROM question WHERE question_id = '{}'".format(question_id))

            dbcon.commit()

            print("\nQuestion deleted successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error as ex:
            print("\nException while trying to delete question: '{}'".format(ex))
            input("Enter a key to continue: ")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def __add_completed_question(question_id, player_name):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            sql = "INSERT INTO question_completed VALUES(%s, %s)"
            var = (question_id, player_name)

            cursor.execute(sql, var)
            dbcon.commit()

        except mysql.connector.Error:
            print("\nError trying to add question")
            input("Enter a key to continue: ")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

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
    def __check_completed_question(question_id, player_name):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            sql = ("SELECT * FROM question_completed WHERE question_completed_question_id = %s AND "
                   "question_completed_player_name = %s")
            var = (question_id, player_name)

            cursor.execute(sql, var)

            row = cursor.fetchone()

            if row is not None:
                return True

        except mysql.connector.Error:
            print("\nException while trying to find question")
            input("Enter a key to continue: ")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def check_question(question_id, challenge_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            sql = "SELECT * FROM question WHERE question_id = %s AND question_challenge_id = %s"
            var = (question_id, challenge_id)
            cursor.execute(sql, var)

            row = cursor.fetchone()

            if row is not None:
                return True

        except mysql.connector.Error:
            print("\nException while trying to find question")
            input("Enter a key to continue: ")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()
