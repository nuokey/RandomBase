from tkinter import *
from tkinter.ttk import *
import sqlite3
import mimesis
import os

def select_surname():
	global surnames_box, labels
	for i in cursor.execute(f'SELECT * FROM users WHERE surname = "{surnames_box.get()}"'):
		user = i

	for i in range(len(user)):
		try:
			labels[i]['text'] = user[i]
		except:
			pass

root = Tk()
root.geometry('250x250')
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

labels = []

for i in range(7):
	label = Label(root, text = '')
	label.place(x = 10, y = i * 20 + 50, width = 230)
	labels.append(label)

root.mainloop()