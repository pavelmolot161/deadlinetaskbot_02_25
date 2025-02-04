### - 04.02.25
### - 7261984695:AAEFzfQ-89_P5CSq9KJiABf49WLxEFw4o34

import telebot
from telebot import types

# Замените 'YOUR_BOT_TOKEN' на токен Вашего бота
bot = telebot.TeleBot('7261984695:AAEFzfQ-89_P5CSq9KJiABf49WLxEFw4o34')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = message.from_user.first_name
    welcome_text = f"Добрый день, {user_first_name}! Это тестовое задание."
    try:
        bot.send_message(message.chat.id, welcome_text)
        show_buttons(message.chat.id)
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")

def show_buttons(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Резюме Павла Л.")
    button2 = types.KeyboardButton("Кнопка 2")
    button3 = types.KeyboardButton("Кнопка 3")
    markup.add(button1, button2, button3)
    bot.send_message(chat_id, "Выберите кнопку:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        if message.text == "Резюме Павла Л.":
            bot.send_message(message.chat.id, "Вот Ваше резюме: https://docs.google.com/document/d/1H6FX_7SnMH5eeiCXuNOfFX241o4beCyXLdIZZbkYzD8/edit?usp=sharing")
        else:
            bot.send_message(message.chat.id, f"Вы нажали: {message.text}")
    except Exception as e:
        print(f"Ошибка при обработке сообщения: {e}")

if __name__ == "__main__":
    bot.polling(none_stop=True)