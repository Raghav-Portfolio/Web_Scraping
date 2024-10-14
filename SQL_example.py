import sqlite3

#Query certain columns
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
# cursor.execute("SELECT * FROM events WHERE band = 'Lions'")
cursor.execute("SELECT * FROM events WHERE date = '2088.10.15'")
rows = cursor.fetchall()
print(rows)

#INSERT new rows
new_rows = [('Cats', 'Cat City', '2058.11.19'), ('Camel', 'Camel Town', '2088.10.15')]
cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)