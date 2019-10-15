import telebot

import constants
from constants import *
import time
from telebot import types
import json
from threading import Thread
tb = telebot.TeleBot(TOKEN)
import schedule
import datetime
week = {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"}
@tb.message_handler(commands=['start', 'help'])
def upper(message):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    mark_up.add(
                types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
    mark_up.add(types.InlineKeyboardButton('Когда ближайший кружок?', callback_data="circles"))
    tb.send_message(ID,'Дарова это я',reply_markup=mark_up)
    tb.send_sticker(ID,'CAADAgADnQADJd8wHsUtGwlDuZeKFgQ')

@tb.message_handler(content_types=['sticker'])
def s(message):
    print(message)
@tb.callback_query_handler(func=lambda call: True)
def query_handler(call):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    mark_up.add(
                types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
    mark_up.add(types.InlineKeyboardButton('Мои кружки', callback_data="circles"))
    with open("shedule.json", "r") as read_file:
        lessons = json.load(read_file)
    with open("rings.json", "r") as read_file:
        rings = json.load(read_file)
    with open("circles.json", "r") as read_file:
        table = json.load(read_file)
    date = int(datetime.datetime.today().weekday()) +1
    day = week[date]
    if call.data== "tommorow_lessons":
        sms = 'На завтра у тебя:' +'\n'
        sms += '*' + week[date] + '*' + ':' +'\n'
        i = 0
        for value in lessons[day]:
            i +=1
            sms += str(i) + ') ' + value + '\n'
        tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
        tb.send_sticker(ID,'CAADAgADjAEAAiXfMB7wJbXMz_7HwxYE')
    if call.data == 'circles':
        sms = 'В неделе у тебя:' + '\n'
        for key in table:
            sms += '*' + key + '*' + ':' + '\n'
            sms += table[key][0] + '\n'
            sms += table[key][1] + '\n'
            sms += '\n'
        tb.send_message(ID, sms, reply_markup=mark_up,parse_mode='Markdown')
        tb.send_sticker(ID, 'CAADAgADrQADJd8wHq-igYr5nyYUFgQ')
def morning():
    date = int(datetime.datetime.today().weekday())
    day = week[date]
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    mark_up.add(
        types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
    mark_up.add(types.InlineKeyboardButton('Мои кружки', callback_data="circles"))

    with open("shedule.json", "r") as read_file:
        lessons = json.load(read_file)
    with open("rings.json", "r") as read_file:
        rings = json.load(read_file)
    with open("circles.json", "r") as read_file:
        table = json.load(read_file)
    sms = '*' + 'Доброе утро брат!' + '*' + '\n'
    sms += 'На сегодня у тебя:' + '\n'
    sms += '*' + week[date] + '*' + ':' + '\n'
    i = 0
    for value in lessons[day]:
        i += 1
        sms += str(i) + ') ' + value + '\n'
    if day in table:
        sms += 'А ещё репет, дада не забывай:' + '\n'
        for key in table:
            sms += '*' + key + '*' + ':' + '\n'
            sms += table[key][0] + '\n'
            sms += table[key][1] + '\n'
            sms += '\n'
        tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
        tb.send_sticker(ID, 'CAADAgADyAADJd8wHm0rHBfrhVxkFgQ')
    else:
        tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
        tb.send_sticker(ID, 'CAADAgADlwEAAiXfMB40_zuFZ8yBJhYE')
schedule.every().day.at("06:20").do(morning)
while True:
    schedule.run_pending()
tb.polling()