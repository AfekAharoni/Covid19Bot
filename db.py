import sqlite3


def create_connection(path):
    """ This function connect to the path given
    :param path: path to connect
    :return: connection
    :rtype: string
    """
    try:
        connection = sqlite3.connect(path)
        print("Connection to DB successful!")
    except sqlite3.Error as e:
        print(f"Oops, The error {e} occurred!")
    return connection


def execute_on_db(connection, query):
    """ This function execute query on the connection
    :param connection: connection parameter
    :param query: content
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully!")
    except sqlite3.Error as e:
        print(f"Oops, The error {e} occurred!")


def execute_read_query(connection, query):
    """ This function return content from query
    :param connection: connection parameter
    :param query: content from query needed
    :return: content
    :rtype: list
    """
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except sqlite3.Error as e:
        print(f"Oops, The error '{e} occurred!")



def close_connection(connection):
    """ This function close the connection
    :param connection: connection parameter
    """
    try:
        connection.close()
        print("The connection DB closed")
    except sqlite3.Error as e:
        print(f"Oops, The error {e} occurred!")
