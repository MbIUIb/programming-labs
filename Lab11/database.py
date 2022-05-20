from typing import Sequence
from itertools import chain
import sqlite3


class Database:
    def __init__(self):
        self.db = sqlite3.connect('Data/database.db')
        self.cursor = self.db.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(id INTEGER, login TEXT, password TEXT)""")

    def commit(self):
        self.db.commit()

    def close(self):
        self.db.close()

    def num_of_users(self):
        self.cursor.execute("""SELECT * FROM users""")
        return len(self.cursor.fetchall())

    def get_user_logins(self):
        self.cursor.execute("""SELECT login FROM users""")
        return self.cursor.fetchall()

    def new_user(self, login, password):
        login = (login, )

        if login not in self.get_user_logins():
            user_id = self.num_of_users()+1
            query = """INSERT INTO users (id, login, password) VALUES(?, ?, ?)"""
            values = (user_id, login, password)
            self.cursor.execute(query, values)
            return 1
        return 0

    def authentication(self, login, password):
        login = (login, )

        user_password = self.cursor.execute("""SELECT password FROM users WHERE login == ?""", login).fetchone()
        if user_password == None:
            return 'login error'

        if password == user_password[0]:
            id = self.cursor.execute("""SELECT id FROM users WHERE login == ?""", login).fetchone()[0]
            return 'successful'
        return 'password error'

    def get_id(self, login: Sequence):
        return self.cursor.execute("""SELECT id FROM users WHERE login == ?""", login).fetchone()[0]

