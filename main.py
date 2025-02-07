
### - 04.02.25
### - 05.02.25
### - 06.02.25

### - 7261984695:AAEFzfQ-89_P5CSq9KJiABf49WLxEFw4o34
import telebot  # Импорт библиотеки для работы с Telegram API
from flask import Flask  # Импорт Flask для создания веб-приложения
from telebot import types  # Импорт типов для создания кнопок в Telegram
from flasgger import Swagger  # Импорт Flasgger для генерации Swagger документации
from threading import Thread  # Импорт для работы с потоками
import logging  # Импорт для логирования
from datetime import datetime  # Импорт для работы с датами и временем
import time  # Импорт для работы со временем

import os  # Импорт для работы с файловой системой



# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Инициализация бота с токеном
bot = telebot.TeleBot('7261984695:AAEFzfQ-89_P5CSq9KJiABf49WLxEFw4o34')

# Инициализация Flask приложения
app = Flask(__name__)
swagger = Swagger(app)  # Инициализация Swagger для документации API

@app.route('/start', methods=['GET'])
def start():
    """Start endpoint
    ---
    responses:
      200:
        description: Приветствие
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
    """
    return {"message": "Добро пожаловать в API бота deadlinetaskbot!"}

# Определение маршрута для Swagger UI
@app.route('/swagger', methods=['GET'])
def swagger_ui():
    return app.send_static_file('index.html')  # Возвращаем HTML-страницу Swagger UI

# Определение маршрута для swagger.yaml
@app.route('/swagger.yaml', methods=['GET'])
def swagger_yaml():
    return app.send_static_file('swagger.yaml')  # Возвращаем файл спецификации

# Множество для хранения уникальных пользователей
unique_users = set()
last_reported_date = datetime.now().date()  # Переменная для хранения последней отчетной даты

# Определение маршрута для приветственного сообщения
@app.route('/api/v1/welcome', methods=['GET'])
def welcome():
    """Welcome message
    ---
    responses:
      200:
        description: Welcome message
    """
    return "Добро пожаловать в API бота deadlinetaskbot !"  # Возвращаем приветственное сообщение

# Определение маршрута для проверки статуса бота
@app.route('/api/v1/status', methods=['GET'])
def status():
    """Check bot status
    ---
    responses:
      200:
        description: Bot is running
    """
    return "Бот deadlinetaskbot работает!"  # Возвращаем сообщение о статусе бота

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name  # Получаем имя пользователя
    user_id = message.from_user.id  # Получаем ID пользователя
    welcome_text = f"Добрый день, {user_first_name}! Это тестовое задание."  # Формируем приветственное сообщение
    logging.info(f"Пользователь {user_first_name} (ID: {user_id}) вошел в чат.")  # Логируем вход пользователя

    try:
        bot.send_message(message.chat.id, welcome_text)  # Отправляем приветственное сообщение
        show_buttons(message.chat.id)  # Показываем кнопки
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения: {e}")  # Логируем ошибку

# Функция для отображения кнопок
def show_buttons(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем разметку для кнопок
    button1 = types.KeyboardButton("Резюме на Павла Л.")  # Кнопка для резюме
    button2 = types.KeyboardButton("Кнопка [2]")  # Вторая кнопка
    button3 = types.KeyboardButton("Кнопка [3]")  # Третья кнопка
    markup.add(button1, button2, button3)  # Добавляем кнопки в разметку
    bot.send_message(chat_id, "Выберите кнопку:", reply_markup=markup)  # Отправляем сообщение с кнопками

# Обработчик всех сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_first_name = message.from_user.first_name  # Получаем имя пользователя
    user_id = message.from_user.id  # Получаем ID пользователя

    try:
        if message.text == "Резюме на Павла Л.":  # Проверяем, нажал ли пользователь на кнопку резюме
            logging.info(f"Пользователь {user_first_name} (ID: {user_id}) запросил резюме.")  # Логируем запрос резюме
            bot.send_message(message.chat.id,
                             "Вот Ваше резюме: https://docs.google.com/document/d/1H6FX_7SnMH5eeiCXuNOfFX241o4beCyXLdIZZbkYzD8/edit?usp=sharing")  # Отправляем ссылку на резюме
        else:
            bot.send_message(message.chat.id, f"Вы нажали: {message.text}")  # Отправляем сообщение о нажатой кнопке
    except Exception as e:
        logging.error(f"Ошибка при обработке сообщения от пользователя {user_first_name} (ID: {user_id}): {e}")  # Логируем ошибку

# Обработчик команды /stop
@bot.message_handler(commands=['stop'])
def stop_bot(message):
    user_first_name = message.from_user.first_name  # Получаем имя пользователя
    user_id = message.from_user.id  # Получаем ID пользователя
    logging.info(f"Пользователь {user_first_name} (ID: {user_id}) вышел из бота deadlinetaskbot.")  # Логируем выход пользователя
    bot.send_message(message.chat.id, "Вы вышли из бота deadlinetaskbot. Спасибо за использование!")  # Отправляем сообщение о выходе

# Функция для запуска Flask-приложения
def run_flask():
    app.run(host='0.0.0.0', port=5000)  # Запускаем Flask на всех интерфейсах

# Функция для отчетности о количестве пользователей
def report_user_count():
    global last_reported_date  # Объявляем переменную как глобальную
    while True:
        now = datetime.now()  # Получаем текущее время
        if now.date() != last_reported_date:  # Проверяем, изменился ли день
            last_reported_date = now.date()  # Обновляем дату
            logging.info(f"Количество уникальных пользователей за {last_reported_date}: {len(unique_users)}")  # Логируем количество пользователей
            unique_users.clear()  # Очищаем множество для следующего дня
        time.sleep(3600)  # Проверяем каждый час

# Функция для запуска Flask-приложения
# def run_flask():
#     app.run(host='0.0.0.0', port=5000)  # Запускаем Flask на всех интерфейсах

# Главная точка входа программы
if __name__ == "__main__":
    Thread(target=run_flask).start()  # Запускаем Flask в отдельном потоке
    Thread(target=report_user_count).start()  # Запускаем процесс отчетности в отдельном потоке
    bot.polling(none_stop=True)  # Запускаем бота



































### - КОД РАБОТАЕТ И ПРОГРУЖЕН НА КОСТИНГ


# import telebot
# from flask import Flask
# from telebot import types
# from flasgger import Swagger
#
# # Замените 'YOUR_BOT_TOKEN' на токен Вашего бота
# bot = telebot.TeleBot('7261984695:AAEFzfQ-89_P5CSq9KJiABf49WLxEFw4o34')
#
# app = Flask(__name__)
# swagger = Swagger(app)
#
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     user_first_name = message.from_user.first_name
#     welcome_text = f"Добрый день, {user_first_name}! Это тестовое задание."
#     try:
#         bot.send_message(message.chat.id, welcome_text)
#         show_buttons(message.chat.id)
#     except Exception as e:
#         print(f"Ошибка при отправке сообщения: {e}")
#
# def show_buttons(chat_id):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton("Резюме Павла Л.")
#     button2 = types.KeyboardButton("Кнопка 2")
#     button3 = types.KeyboardButton("Кнопка 3")
#     markup.add(button1, button2, button3)
#     bot.send_message(chat_id, "Выберите кнопку:", reply_markup=markup)
#
# @bot.message_handler(func=lambda message: True)
# def handle_message(message):
#     try:
#         if message.text == "Резюме Павла Л.":
#             bot.send_message(message.chat.id, "Вот Ваше резюме: https://docs.google.com/document/d/1H6FX_7SnMH5eeiCXuNOfFX241o4beCyXLdIZZbkYzD8/edit?usp=sharing")
#         else:
#             bot.send_message(message.chat.id, f"Вы нажали: {message.text}")
#     except Exception as e:
#         print(f"Ошибка при обработке сообщения: {e}")
#
# if __name__ == "__main__":
#     bot.polling(none_stop=True)