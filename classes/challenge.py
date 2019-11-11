import os
import mysql.connector
from program import database


# Class to store challenges data
class Challenge:
    # Constructor with challenge atributes
    def __init__(self, challenge_id, challenge_description):
        self.challenge_id = challenge_id
        self.challenge_description = challenge_description

    @staticmethod
    def list_challenge():
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()
            cursor.execute("SELECT * FROM challenge")

            result = cursor.fetchall()

            os.system("cls")
            print("{:<15}{:<50}".format("ID", "DESCRIPTION"))
            print(65 * "-")

            for row in result:
                print("{:<15}{:<50}".format(row[0], row[1]))

            print(65 * "-")

        except mysql.connector.Error:
            print("\nException while listing questions")
        finally:
            if dbcon.is_connected:
                cursor.close()
                dbcon.close()

    # Method to check if a challenge contains questions
    @staticmethod
    def contains_questions(challenge_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()
            cursor.execute("SELECT * FROM question WHERE question_challenge_id = '{}'".format(challenge_id))

            row = cursor.fetchone()

            if row is not None:
                return True

        except mysql.connector.Error:
            print("\nException while checking challenge")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def modify_challenge(challenge_id, modification):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            sql = "UPDATE challenge SET challenge_description = %s WHERE challenge_id = %s"
            var = (modification, challenge_id)
            cursor.execute(sql, var)

            dbcon.commit()

            print("\nChallenge modified successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nException while trying to modify challenge")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    # Method to delete challenge and questions if it has any
    @staticmethod
    def delete_challenge(challenge_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute("DELETE FROM question WHERE question_challenge_id = '{}'".format(challenge_id))
            cursor.execute("DELETE FROM challenge WHERE challenge_id = '{}'".format(challenge_id))

            dbcon.commit()

            print("\nChallenge deleted successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nException while trying to delete challenge")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    # Method to add new challenge to database
    def add_challenge(self):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            sql = "INSERT INTO challenge VALUES(%s, %s)"
            var = (self.challenge_id, self.challenge_description)

            cursor.execute(sql, var)
            dbcon.commit()

            print("\nChallenge successfully added")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nException while trying to add challenge")
            input("Enter a key to continue: ")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    # Method to check if challenge already exists in database
    @staticmethod
    def check_challenge(challenge_id):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()
            cursor.execute("SELECT challenge_id FROM challenge WHERE challenge_id = '{}'".format(challenge_id))

            row = cursor.fetchone()

            if row is not None:
                return True

        except mysql.connector.Error:
            print("\nException while trying to find challenge")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()
