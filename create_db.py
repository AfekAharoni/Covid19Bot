import sqlite3


def create_db():
    """ Creating 'covid19' database
    """
    try:
        connection = sqlite3.connect('covid19.db')
        cursor = connection.cursor()
        cursor.execute(""" CREATE TABLE IF NOT EXISTS covid19 (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        daily_man_sick TEXT, 
        daily_infection_coefficient TEXT,
        man_vaccine TEXT,
        man_total_vaccine TEXT,
        date TEXT)
        """)
    # id - number of row
    # daily_man_sick - number of sick in a day
    # daily_man_bad_sick - number of bad sick in a day
    # daily_man_death - number of death in a day
    # date - the date of the day
        print("DB created successfully!")
    except sqlite3.Error as e:
        print(f"Oops, The error '{e} occurred!")
    connection.commit()
    connection.close()


def main():
    create_db()


if __name__ == '__main__':
    main()
