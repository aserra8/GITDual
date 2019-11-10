import mysql
import mysql.connector


# Function to connect to database
def connectdb():
    try:
        dbconnection = mysql.connector.connect(
            host="localhost",
            user="admin",
            passwd="Patata123",
            database="project",
        )

        return dbconnection

    except mysql.connector.Error:
        print("\nError while connecting to the database")

