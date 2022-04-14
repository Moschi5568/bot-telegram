import sqlite3

def prof(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_select_query = """SELECT * from it_tehnology"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        for row in records:
            print("num", row[0])
            print("Профессия", row[1])
            print("Зарплата", row[2])
            print("Контактные данные", row[3])
            print("Сайт", row[4])
            print("Адресс", row[4], end="\n\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
