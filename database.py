import sqlite3

def create_connection():
    """Создать соединение с базой данных."""
    conn = sqlite3.connect('users.db')
    return conn

def create_table():
    """Создать таблицу пользователей."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user_id, username):
    """Добавить пользователя в базу данных."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (id, username) VALUES (?, ?)', (user_id, username))
    conn.commit()
    conn.close()

def remove_user(user_id):
    """Удалить пользователя из базы данных."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()

def get_user(user_id):
    """Получить пользователя из базы данных."""
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user
