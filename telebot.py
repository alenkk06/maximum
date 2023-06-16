import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5686738585:AAHObtMwdsCIauntKpRKybuRqxgCkHHK6V8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message, res = False):
    welcome_text = """
    Привет! Я умею рассказывать стихи,знаю много интересных фактовl, могу показать милых котиков и посоветовать игры!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True, one_time_keyboard = False)
    button1 = telebot.types.KeyboardButton('ФАКТ')
    button2 = telebot.types.KeyboardButton('СТИХ')
    button3 = telebot.types.KeyboardButton('КОТ')
    button4 = telebot.types.KeyboardButton('СТИКЕР')
    button5 = telebot.types.KeyboardButton('ИГРЫ')
    button6 = telebot.types.KeyboardButton ('СТРАТЕГИЧЕСКИЕ')
    button7 = telebot.types.KeyboardButton ('УЖАСЫ')
    button8 = telebot.types.KeyboardButton('РОЛЕВЫЕ')
    button9 = telebot.types.KeyboardButton('ФАЙТИНГОВЫЕ')
    keyboard.add(button1,button2,button3,button4,button5)
    bot.send_message(message.chat.id, welcome_text,reply_murkup = keyboard)

@bot.message_handler(commands=['facts'])
def send_facts(message):
    response = requests.get('https://i-fact.ru/').content
    html = BeautifulSoup(response, 'html.parser')
    fact= random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и всё стихотворенье..."
    bot.send_message(message.chat.id, poem_text)

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_rnumber = str(random.randint(1,10))
    cat_img = open ('img.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@@bot.message_handler(commands=['stiker'])
def send_stiker(message):
    bot.send_stiker(message.chat.id, "CAACAgTAAxkBAAEGyAFjlcn6NwXCN0gfFcJfQ-iv-usiUAAC1CIAAvhtsEgTy0IAAWSuHYgrBA")
     
@bot.message_handler(commands=['games.strateg'])
def strateg_games(message):
     strateg_text = "Вот 5 интересных стратегических игр: 'Strategic Command: European Theater', 'Sid Meier's Civilization 6', 'RimWorld', 'World of Tanks Blitz', 'Frostpunk."
     bot.send_message(message.chat.id, strateg_text)
     keyboard = telebot.types.InlineKeyboardButton (row_width=1)
     button_url = telebot.types.InlineKeyboarButton ('Перейти', url ='https://vgtimes.ru/')
     bot.send_message(message.chat.id, 'Больше игр по ссылке ниже', reply_markup=keyboard)

@bot.message_handler(commands=['games.horrors'])
def horrors_games(message):
     horrorsl_text = "Вот 5 интересных страшных игр: 'Phasmophobia', 'The Quarry', '7 Days To Die', 'Dead by Daylight', 'Doom."
     bot.send_message(message.chat.id,horrors_text)
     keyboard = telebot.types.InlineKeyboardButton (row_width=1)
     button_url = telebot.types.InlineKeyboarButton ('Перейти', url ='https://vgtimes.ru/games/')
     bot.send_message(message.chat.id, 'Больше игр по ссылке ниже', reply_markup=keyboard)

@bot.message_handler(commands=['games.roals'])
def roals_games(message):
     roals_text = "Вот 5 интересных ролевых игр: 'Cyberpunk 2077', 'Hogwarts Legacy', 'Genshin Impact ', 'NieR Automata', 'Fallout 4'."
     bot.send_message(message.chat.id, roals_text)
     keyboard = telebot.types.InlineKeyboardButton (row_width=1)
     button_url = telebot.types.InlineKeyboarButton ('Перейти', url ='https://vgtimes.ru/games/')
     bot.send_message(message.chat.id, 'Больше игр по ссылке ниже', reply_markup=keyboard)

@bot.message_handler(commands=['games.fight'])
def fight_games(message):
     fight_text = "Вот 5 интересных файтинговых игр: 'Mortal Kombat', 'Dead Island 2', 'Tekken 7 ', 'BlazBlue: Calamity Trigger', 'Injustice 2'."
     bot.send_message(message.chat.id, fight_text)
     keyboard = telebot.types.InlineKeyboardButton (row_width=1)
     button_url = telebot.types.InlineKeyboarButton ('Перейти', url ='https://vgtimes.ru/games/')
     bot.send_message(message.chat.id, 'Больше игр по ссылке ниже', reply_markup=keyboard)


@bot.message_handler(commands = 'games'])
def answer(message):
     games_text = "Какой жанр компьютерных игр вы предпочитаете?"
     if message.text.strip()== 'СТРАТЕГИЧЕСКИЕ':
         send_games.strateg(message)
     elif message.text.strip()== 'РОЛЕВЫЕ':
         send_games.roals(message)
     elif message.text.strip()== 'УЖАСЫ':
         send_games.horrors(message)
     elif message.text.strip()== 'Файтинговые':
         send_games.fight(message)

bot.message_handler(content_types = ["text"])
def answer(message):
    if message.text.srtrip() == 'ФАКТ':
        send_fact(message)
    elif message.text.strip() == 'СТИХОТВОРЕНИЕ':
        send_poem(message)
    elif message.text.strip() == 'КОТИКИ':
        send_cat(message)
    elif message.text.strip() == 'СТИКЕР':
            send_stiker(message)
    elif message.text.strip() == 'ИГРЫ':
        send_games.text(message)

bot.polling()


