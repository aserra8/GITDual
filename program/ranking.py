import os
from program import database
import mysql.connector


# Function to print leaderboard
def show_player_leaderboard():
    counter = 0
    dbcon = None
    cursor = None

    try:
        dbcon = database.connectdb()
        cursor = dbcon.cursor()
        cursor.execute("SELECT player_name, player_score FROM player ORDER BY player_score DESC")

        result = cursor.fetchall()

        os.system("cls")
        print("{:<20}{:<40}{:>15}".format("POSITION", "TEAM NAME", "SCORE"))
        print(75 * "-")

        for row in result:
            if row[0] != "ADMIN":
                counter += 1
                print("{:<20}{:<40}{:>15}".format(counter, row[0], row[1]))

        print(75 * "-")
        input("\nEnter a key to continue: ")

    except mysql.connector.Error:
        print("\nError fetching data from MySQL table")

    finally:
        if dbcon.is_connected():
            cursor.close()
            dbcon.close()
