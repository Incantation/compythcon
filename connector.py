import sqlite3
from sqlite3 import Error

def create_connection(path):
    connection = 1
    try:
        connection = sqlite3.connect(path)
        print("Connection to COMP/CON successful")
    except Error as e:
        print(e)
    return connection

