import sqlite3
conn = sqlite3.connect("lunch.db")
c = conn.cursor()
# c.execute("CREATE TABLE lunch(name TEXT, price REAL)")
# c.execute("INSERT INTO lunch VALUES('짜장면', 1000)")
