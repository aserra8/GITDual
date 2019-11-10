import os
from program import database
import mysql.connector


# Function to print leaderboard
def show_player_leaderboard():
    counter = 0
    dbcon = None
    cursor = None

    try:
        sql = "SELECT player_name, player_score FROM player ORDER BY player_score DESC"

        dbcon = database.connectdb()

        cursor = dbcon.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        os.system("cls")
        print("\nPOSITION\t\t\tTEAM NAME\t\t\t\tSCORE")
        print(76 * "-")
        for row in result:
            if row[0] != "ADMIN":
                counter += 1
                print(counter, "\t\t\t\t", row[0], "\t\t\t\t\t", row[1])
        print(76 * "-")

        input("\nEnter a key to continue: ")

    except mysql.connector.Error:
        print("\nError fetching data from MySQL table")

    finally:
        if dbcon.is_connected():
            cursor.close()
            dbcon.close()
