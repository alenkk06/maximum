import telebot
import requests
import random
from bs4 import BeautifulSoup

token = '5686738585:AAHObtMwdsCIauntKpRKybuRqxgCkHHK6V8'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    welcome_text = """
    Привет! Я умею рассказывать стихи,знаю много интересных фактов и могу показать милых котиков!
    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 2, resize_keyboard = True, one_time_keyboard = False)
    button1 = telebot.types.KeyboardButton('ФАКТ')
    button2 = telebot.types.KeyboardButton('СТИХ')
    button3 = telebot.types.KeyboardButton('КОТ')
    keyboard.add(button1,button2,button3 )
    bot.send_message(message.chat.id, welcome_text,reply_markup = keyboard)

@bot.message_handler(commands=['fact'])
def send_fact(message):
    response = requests.get('https://i-fact.ru/').content
    html = BeautifulSoup(response, 'html.parser')
    fact= random.choice(html.find_all(class_='p-2 clearfix'))
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(message.chat.id, fact_link)

@bot.message_handler(commands=['poem'])
def send_poem(message):
    poem_text = "Муха села на варенье, вот и всё стихотворенье..."
    bot.send_message(message.chat.id, poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup (row_width=1)
    button_url = telebot.types.InlineKeyboardMarkup ('Перейти', url ='https:stihi.ru/')

@bot.message_handler(commands=['cat'])
def send_cat(message):
    cat_rnumber = str(random.randint(1,10))
    cat_img = open ('img.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)
    
@bot.message_handler(content_types=['text'])
def answers(message):
    if message.text.strip()== 'фАКТ':
        send_fact(message)
    elif message.text.strip()== 'СТИХ':
        send_poem(message)
    elif message.text.strip()== 'КОТ':
        send_cat(message)
        

bot.polling()
