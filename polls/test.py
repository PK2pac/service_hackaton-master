import telebot
import sqlite3
from .models import *

types = ['конференции', 'конкурсы', 'выставки и встречи', 'праздники', 'концерты', 'фестивали']

def send_newsletter(event):
    bot = telebot.TeleBot('411438977:AAHARyyJYYD5LCsdMzS7h9VjuF6QEMNRlMI')
    #conn = sqlite3.connect('./db.sqlite3')
    #cursor = conn.cursor()
    #cursor.execute('SELECT * FROM subscribers')
    #result = cursor.fetchall()

    result = Subsriber.objects.all().values('subscriber_id')
    message = 'Новое меропритие:\n{}\nНачало: {}\nОкончание: {}\nАдрес: {}\nКонтакты: {}'.format(event[0], event[1], event[2], event[3], event[4])

    for s in result:
        bot.send_message(s['subscriber_id'], message)
        bot.send_message(s['subscriber_id'], 'Чтобы отписаться --> /subscribe_off')
