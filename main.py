import sqlite3

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect("alkanchiki.db")
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Story (
id INTEGER PRIMARY KEY,
alkan TEXT NOT NULL
)
''')

# Добавляем нового пользователя
cursor.execute('INSERT INTO Story (alkan) VALUES (?)', ['Бутан'])
cursor.execute('INSERT INTO Story (alkan) VALUES (?)', ['Пропан'])
cursor.execute('INSERT INTO Story (alkan) VALUES (?)', ['Метан'])

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()

# Создаем подключение к базе данных (файл my_database.db будет создан)
connection = sqlite3.connect("alkanchiki.db")
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute('SELECT * FROM Story')
alakanchiki = cursor.fetchall()
print(type(alakanchiki))
# Выводим результаты
for alakn in alakanchiki:
  print(alakn)

print("jopa")
print("jopa2")
print("jopa3")
