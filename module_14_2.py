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

try:
    for i in range(1, 11):
        cursor.execute('''INSERT INTO Users (username, email, age, balance)
                        VALUES (?, ?, ?, ?)''',
                        (f'User{i}', f'example{i}@gmail.com', 10 * i, 1000))

    # Обновление balance у каждой 2-й записи начиная с 1-й на 500
    for i in range(1, 11, 2):
        cursor.execute('''UPDATE Users SET balance = 500
                        WHERE id = ?''', (i,))
    for i in range(2, 11, 3):
        cursor.execute('''DELETE FROM Users
                        WHERE id = ?''', (i,))
    cursor.execute('''DELETE FROM Users
                    WHERE id = 6''')

    cursor.execute('''SELECT COUNT(*) FROM Users''')
    total_users = cursor.fвetchone()[0]

    cursor.execute('''SELECT SUM(balance) FROM Users''')
    all_balances = cursor.fetchone()[0]


    print(all_balances / total_users)

except sqlite3.Error as e:
    print(f"Ошибка при работе с базой данных: {e}")

conn.commit()
conn.close()
