from tkinter import *
import sqlite3
import mimesis

root = Tk()

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute('DELETE FROM users')
# for i in range(20):
#     cursor.execute(f'INSERT INTO users VALUES ()')
db.commit()

root.mainloop()