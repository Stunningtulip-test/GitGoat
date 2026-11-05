"""Intentional SQL injection fixture for branch-scanning tests."""

import sqlite3


def find_user():
    username = input("Username: ")
    with sqlite3.connect(":memory:") as connection:
        connection.execute("CREATE TABLE users (name TEXT)")
        connection.execute("INSERT INTO users VALUES ('alice'), ('bob')")
        query = f"SELECT name FROM users WHERE name = '{username}'"
        return connection.execute(query).fetchall()


if __name__ == "__main__":
    print(find_user())
