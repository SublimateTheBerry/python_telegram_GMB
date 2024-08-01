import telebot
from telebot import types
import sqlite3
import config

# Инициализация бота
bot = telebot.TeleBot(config.BOT_TOKEN)

# Подключение к базе данных
conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы пользователей, если она не существует
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL
    )
''')

# Функция для обработки новых участников
@bot.channel_post_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    if message.from_user.id in config.ADMIN_IDS:
        new_user = message.new_chat_members[0]
        cursor.execute('INSERT INTO users (id, username) VALUES (?, ?)', (new_user.id, new_user.username))
        conn.commit()
        bot.reply_to(message, f"Пользователь {new_user.username} добавлен в базу данных.")

# Функция для обработки удалённых участников
@bot.channel_post_handler(content_types=['left_chat_member'])
def handle_left_member(message):
    if message.from_user.id in config.ADMIN_IDS:
        left_user = message.left_chat_member
        cursor.execute('DELETE FROM users WHERE id = ?', (left_user.id,))
        conn.commit()
        bot.reply_to(message, f"Пользователь {left_user.username} удалён из базы данных.")

# Запуск поллинга
bot.polling(none_stop=True)
