from program import database
import mysql.connector


class Player:
    # Constructor with player atributes
    def __init__(self, player_name, player_password):
        self.player_name = player_name
        self.player_password = player_password
        self.player_score = 0

    # Method to add player to the database
    def add_player(self):
        dbcon = None
        cursor = None

        try:
            sql = "INSERT INTO player VALUES(%s, %s, %s)"
            val = (self.player_name, self.player_password, self.player_score)

            dbcon = database.connectdb()

            cursor = dbcon.cursor()
            cursor.execute(sql, val)

            dbcon.commit()
            cursor.close()
            dbcon.close()
            print("\nPlayer added successfully")

        except mysql.connector.Error:
            print("\nError trying to add player")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    # Method to check if player exists
    def check_player(self):
        dbcon = None
        cursor = None

        try:
            sql = "SELECT * FROM player WHERE player_name = %s AND player_password = %s"
            val = (self.player_name, self.player_password)

            dbcon = database.connectdb()

            cursor = dbcon.cursor()
            cursor.execute(sql, val)

            row = cursor.fetchone()

            if row is not None:
                return True

        except mysql.connector.Error:
            print("Error trying to find player")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def get_player_score(current_player):
        dbcon = None
        cursor = None

        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute("SELECT player_score FROM player WHERE player_name = '{}'".format(current_player.player_name))
            result = cursor.fetchone()

            return result[0]

        except mysql.connector.Error:
            print("Error trying to print score")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    # Method to update user score
    @staticmethod
    def update_player_score(points, current_player):
        dbcon = None
        cursor = None

        try:
            sql = "UPDATE player SET player_score = player_score + %s WHERE player_name = %s"
            val = (points, current_player.player_name)

            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute(sql, val)
            dbcon.commit()

        except mysql.connector.Error:
            print("Error trying to find player")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()
