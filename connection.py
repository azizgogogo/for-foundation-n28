import mysql.connector


def dbConnection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "foundation"
    )

    return connection
                          
