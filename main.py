from tkinter import *
from tkinter.ttk import *
import sqlite3
import mimesis
import os

def select_surname():
	pass

root = Tk()
person = mimesis.Person('en')
address = mimesis.Address()
try:
	os.remove('data.db')
except:
	pass

db = sqlite3.connect('data.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE users (
	id INT,
	surname TEXT,
	name TEXT,
	lastname TEXT,
	age INT,
	birthday INT,
	birthtown TEXT,
	tele_number INT,
	email TEXT
)''')

print(dir(person))
surnames = []
for i in range(20):
	age = person.age()
	surname = person.surname()
	surnames.append(surname)
	cursor.execute(f'INSERT INTO users VALUES ({i}, "{surname}", "{person.name()}", "{person.name()}", {age}, {2021 - age}, "{address.city()}", "{person.telephone()}", "{person.email()}")')

db.commit()

surnames_box = Combobox(root, values = surnames)
surnames_box.place(x = 10, y = 10, width = 100)

surnames_button = Button(root, text = 'Select', command = select_surname)
surnames_button.place(x = 115, y = 10)

name_button = 

root.mainloop()