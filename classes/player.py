import os
import mysql.connector
from program import database


class Player:
    def __init__(self, player_name, player_password):
        self.player_name = player_name
        self.player_password = player_password
        self.player_score = 0

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

            print("\nPlayer added successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nError trying to add player")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def delete_player(player_name):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute("DELETE FROM player WHERE player_name = '{}'".format(player_name))

            dbcon.commit()

            print("\nPlayer deleted successfully")
            input("Enter a key to continue: ")

        except mysql.connector.Error:
            print("\nException while trying to delete player")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def modify_player(player_name, option, modification):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            if option == 1:
                sql = "UPDATE player SET player_name = %s WHERE player_name = %s"
                var = (modification, player_name)
                cursor.execute(sql, var)
            elif option == 2:
                sql = "UPDATE player SET player_password = %s WHERE player_name = %s"
                var = (modification, player_name)
                cursor.execute(sql, var)
            elif option == 3:
                sql = "UPDATE player SET player_score = %s WHERE player_name = %s"
                var = (modification, player_name)
                cursor.execute(sql, var)

            dbcon.commit()

        except mysql.connector.Error:
            print("\nException while trying to modify player")

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def check_player_name(player_name):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            cursor.execute("SELECT player_score FROM player WHERE player_name = '{}'".format(player_name))

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
    def check_player(player_name, player_password):
        dbcon = None
        cursor = None
        try:
            sql = "SELECT * FROM player WHERE player_name = %s AND player_password = %s"
            val = (player_name, player_password)

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

    @staticmethod
    def update_player_score(points, current_player, option):
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()

            if option == 0:
                sql = "UPDATE player SET player_score = player_score + %s WHERE player_name = %s"
                val = (points, current_player.player_name)
                cursor.execute(sql, val)
            else:
                if not Player.get_player_score(current_player) == 0:
                    sql = "UPDATE player SET player_score = player_score - ((%s * 5)/100) WHERE player_name = %s"
                    val = (points, current_player.player_name)
                    cursor.execute(sql, val)

            dbcon.commit()

        except mysql.connector.Error:
            print("Error trying to update player score")
            return True

        finally:
            if dbcon.is_connected():
                cursor.close()
                dbcon.close()

    @staticmethod
    def list_players():
        dbcon = None
        cursor = None
        try:
            dbcon = database.connectdb()
            cursor = dbcon.cursor()
            cursor.execute("SELECT * FROM player")

            result = cursor.fetchall()

            os.system("cls")
            print("{:<30}{:<30}{:>10}".format("USER NAME", "PASSWORD", "SCORE"))
            print(70 * "-")

            for row in result:
                print("{:<30}{:<30}{:>10}".format(row[0], row[1], row[2]))

            print(70 * "-")

        except mysql.connector.Error:
            print("\nException while listing users")
        finally:
            if dbcon.is_connected:
                cursor.close()
                dbcon.close()
