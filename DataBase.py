import sqlite3


class DataBase:
    def __init__(self):     # инициалзация 
        name = "shop.db"
        self.db = sqlite3.connect(f"{name}")
        cur = self.db.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Shop (
            id integer primary key,
            name TEXT,
            address TEXT,
            country TEXT
            )
        """)

        self.db.commit()
        cur.close()

    def get_from_shop(self):    # чтение данных из БД
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Shop""")
        records = cur.fetchall()
        cur.close()
        return records

    def update_shop(self, id, name, address, country):   # обновление данных
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f""" UPDATE Shop set name="{name}", address="{address}", country="{country}" WHERE id={id}""")
        self.db.commit()
        cur.close()

    def delete_from_shop(self, id):     # удаление данных
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Shop WHERE id={id}""")
        self.db.commit()
        cur.close()

    def add_in_shop(self, name, address, country):      # добавление данных
        cur = self.db.cursor()
        cur.execute("INSERT INTO Shop VALUES (NULL, ?, ?, ?)", (name, address, country))
        self.db.commit()
        cur.close()
