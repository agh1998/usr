import sqlite3

with sqlite3.connect("users.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE usersFav(usr TEXT, fav TEXT, UNIQUE(usr,fav))""")
	c.execute("""CREATE TABLE usersHis(usr TEXT, his TEXT, UNIQUE(usr,his))""")
	c.close()
