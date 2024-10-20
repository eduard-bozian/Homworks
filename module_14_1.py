import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)''')

for i in range(1, 11):
    cursor.execute('''INSERT INTO Users (username, email, age, balance)
                    VALUES (?, ?, ?, ?)''',
                    (f'User{i}', f'example{i}@gmail.com', 10 * i, 1000))

for i in range(1, 11, 2):
    cursor.execute('''UPDATE Users SET balance = 500
                    WHERE id = ?''', (i,))

for i in range(2, 11, 3):
    cursor.execute('''DELETE FROM Users
                    WHERE id = ?''', (i,))

cursor.execute('''SELECT username, email, age, balance
                FROM Users
                WHERE age != 60''')

for row in cursor.fetchall():
    print(f'Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}')
conn.commit()
conn.close()

