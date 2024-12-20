import telebot
import random
import json
import os

# Инициализация бота с вашим токеном
API_TOKEN = '8193378867:AAFMyclzhCUZq_2gSXDMK7Hc94wnEDxwNF8'
bot = telebot.TeleBot(API_TOKEN)

# Файл для хранения статистики
STATISTICS_FILE = 'statistics.json'

# Загрузка статистики из файла, если он существует
if os.path.exists(STATISTICS_FILE):
    with open(STATISTICS_FILE, 'r') as f:
        statistics = json.load(f)
else:
    statistics = {
        'numbers': {i: 0 for i in range(1, 101)},
        'games': 0,
        'wins': 0
    }

# Функция для сохранения статистики в файл
def save_statistics():
    with open(STATISTICS_FILE, 'w') as f:
        json.dump(statistics, f)

# Хранение состояния игры для каждого пользователя
user_games = {}

@bot.message_handler(commands=['start'])
def start_game(message):
    bot.send_message(message.chat.id, "Привет! Я загадаю число от 1 до 100. Попробуй угадать его за 3 попытки!")
    start_new_game(message.chat.id)

def start_new_game(chat_id):
    number_to_guess = random.randint(1, 100)
    user_games[chat_id] = {
        'number': number_to_guess,
        'attempts': 0,
        'max_attempts': 3
    }
    statistics['numbers'][number_to_guess] += 1
    save_statistics()
    
    bot.send_message(chat_id, "Я загадал число. У тебя есть 3 попытки!")

@bot.message_handler(func=lambda message: message.chat.id in user_games)
def guess_number(message):
    chat_id = message.chat.id
    user_game = user_games[chat_id]
    
    try:
        guess = int(message.text)
    except ValueError:
        bot.send_message(chat_id, "Пожалуйста, введи число.")
        return

    user_game['attempts'] += 1

    if guess < user_game['number']:
        bot.send_message(chat_id, "Загаданное число больше.")
    elif guess > user_game['number']:
        bot.send_message(chat_id, "Загаданное число меньше.")
    else:
        bot.send_message(chat_id, "Поздравляю! Ты угадал число!")
        statistics['games'] += 1
        statistics['wins'] += 1
        save_statistics()
        del user_games[chat_id]
        return

    if user_game['attempts'] >= user_game['max_attempts']:
        bot.send_message(chat_id, f"Ты не угадал. Загаданное число было {user_game['number']}.")
        statistics['games'] += 1
        del user_games[chat_id]
        save_statistics()
    else:
        bot.send_message(chat_id, f"Попробуй еще раз! У тебя осталось {user_game['max_attempts'] - user_game['attempts']} попыток.")

@bot.message_handler(commands=['stats'])
def show_statistics(message):
    total_games = statistics['games']
    total_wins = statistics['wins']
    if total_games > 0:
        win_percentage = (total_wins / total_games) * 100
    else:
        win_percentage = 0

    most_popular_number = max(statistics['numbers'], key=statistics['numbers'].get)

    stats_message = (
        f"Общее количество игр: {total_games}\n"
        f"Количество побед: {total_wins}\n"
        f"Процент побед: {win_percentage:.2f}%\n"
        f"Самый популярный загаданное число: {most_popular_number} (загадано {statistics['numbers'][most_popular_number]} раз)"
    )
    
    bot.send_message(message.chat.id, stats_message)

# Запуск бота
bot.polling(none_stop=True)
