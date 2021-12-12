import sqlite3
from sqlite3.dbapi2 import Connection, connect

DATABASE = 'stwl.db'

connent = sqlite3.connect(DATABASE)
cursor = connent.cursor()

sql  = '''
    CREATE TABLE IF NOT EXISTS companies ( 
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
'''
cursor.execute(sql)

sql = '''
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
        company TEXT NOT NULL
    )
'''
cursor.execute(sql)

sql = "INSERT INTO companies(name) values(?)"

cursor.execute(sql , ("Microsoft",))

connect.commit()

cursor.execute(sql , ("Google",))

connect.commit()

sql = "INSERT INTO courses(name, category, company_id) values(?, ?, ?)"

cursor.execute(sql , ("Python", "Programming", 1))

connect.commit()

companies = connect.execute("SELECT count(id) FROM companies")

print(*companies)
