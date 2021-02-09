from tkinter import *
import sqlite3
import mimesis

root = Tk()

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXIST users (
	id INT,
	surname TEXT,
	name TEXT,
	lastname TEXT,
	age INT,
	birthday TEXT,
	birthtown TEXT,
	tele_number INT,
	email TEXT
)''')
db.commit()

root.mainloop()