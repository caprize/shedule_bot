import telebot
import threading
import constants
from constants import *
import time
from telebot import types
import json
from threading import Thread


tb = telebot.TeleBot(TOKEN, threaded=False)
import schedule
import datetime
from threading import Thread
import work_with_file
import pytz

offset = datetime.timedelta(hours=3)
datetime.timezone(offset, name='МСК')
@tb.message_handler(commands=['start', 'help'])
def upper(message):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    mark_up.add(types.InlineKeyboardButton('Расписание на сегодня', callback_data="today_lessons"),
                types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
    tb.send_message(ID, 'Дарова это я', reply_markup=mark_up)
    tb.send_sticker(ID, 'CAADAgADnQADJd8wHsUtGwlDuZeKFgQ')


@tb.message_handler(content_types=['sticker'])
def s(message):
    print(message)


@tb.callback_query_handler(func=lambda call: True)
def query_handler(call):
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    mark_up.add(types.InlineKeyboardButton('Расписание на сегодня', callback_data="today_lessons"),
                types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
    mark_up.add(types.InlineKeyboardButton('Мои кружки', callback_data="circles"))
    with open("schedule.json", "r") as read_file:
        lessons = json.load(read_file)
    with open("rings.json", "r") as read_file:
        rings = json.load(read_file)
    with open("circles.json", "r") as read_file:
        table = json.load(read_file)
    date = int(datetime.datetime.today().weekday())
    month = (datetime.datetime.today().month)
    day = datetime.datetime.today().day
    if day in chet[month]["Четные"]:
        koef = "Четные"
    else:
        koef = "Нечетные"
    day = week[date]
    if call.data == "tommorow_lessons":
        if day != 'Суббота':
            if day == "Воскресенье":
                day = datetime.datetime.today().day
                if (day+1) in chet[month]["Четные"]:
                    koef = "Четные"
                else:
                    koef = "Нечетные"
                day = "Понедельник"
                date = 0
            else:
                date += 1
                day = week[date]
            sms = 'На завтра у тебя:' + '\n'
            sms += '*' + week[date] + '*' + ':' + '\n'
            i = 0
            for value in lessons[day][koef]:
                i += 1
                if str(value) == "nan (nan)":
                    continue
                sms += str(i) + ') ' + str(value) + "  //  " + rings[str(i)] + '\n'

            tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
            tb.send_sticker(ID, 'CAADAgADjAEAAiXfMB7wJbXMz_7HwxYE')
            # tb.edit_message_text(sms, ID, inline_message_id=call.message,reply_markup=mark_up, parse_mode='Markdown')


        else:
            mark_up = types.InlineKeyboardMarkup(row_width=2)
            mark_up.add(types.InlineKeyboardButton('Расписание на сегодня', callback_data="today_lessons"))
            mark_up.add(types.InlineKeyboardButton('Мои кружки', callback_data="circles"))
            tb.send_message(ID, '*У тебя завтра выходной, отдыхай. Заслужил братишка!*', reply_markup=mark_up,
                            parse_mode='Markdown')
            tb.send_sticker(ID, 'CAADAgADrwADJd8wHpOt467UzX9gFgQ')
            # tb.edit_message_text('*У тебя завтра выходной, отдыхай. Заслужил братишка!*',  ID, call.message.message_id, reply_markup=mark_up, parse_mode='Markdown')
    if call.data == 'circles':
        sms = 'В неделе у тебя:' + '\n'
        for key in table:
            sms += '*' + key + '*' + ':' + '\n'
            sms += table[key][0] + '\n'
            sms += table[key][1] + '\n'
            sms += '\n'
        tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
        tb.send_sticker(ID, 'CAADAgADrQADJd8wHq-igYr5nyYUFgQ')
    if call.data == 'today_lessons':
        mark_up = types.InlineKeyboardMarkup(row_width=2)
        mark_up.add(
            types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
        mark_up.add(types.InlineKeyboardButton('Мои кружки', callback_data="circles"))
        if day != 'Воскресенье':
            sms = 'Сегодня  у тебя:' + '\n'
            sms += '*' + week[date] + '*' + ':' + '\n'
            i = 0

            for value in lessons[day][koef]:
                i += 1
                if str(value) == "nan (nan)":
                    continue
                sms += str(i) + ') ' + str(value) + "  //  " + rings[str(i)] + '\n'
            tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
            tb.send_sticker(ID, 'CAADAgADlwEAAiXfMB40_zuFZ8yBJhYE')
        else:
            tb.send_message(ID, '*У тебя сегодня выходной, отдыхай. Заслужил братишка!*', reply_markup=mark_up,
                            parse_mode='Markdown')
            tb.send_sticker(ID, 'CAADAgADmQEAAiXfMB4NKXhC2J6hwxYE')


def morning():
    date = int(datetime.datetime.today().weekday())
    month = (datetime.datetime.today().month)
    day = datetime.datetime.today().day
    if day in chet[month]["Четные"]:
        koef = "Четные"
    else:
        koef = "Нечетные"
    day = week[date]
    mark_up = types.InlineKeyboardMarkup(row_width=2)
    mark_up.add(
        types.InlineKeyboardButton('Расписание на завтра', callback_data="tommorow_lessons"))
    mark_up.add(types.InlineKeyboardButton('Мои кружки', callback_data="circles"))
    if day != 'Воскресенье':
        with open("schedule.json", "r") as read_file:
            lessons = json.load(read_file)
        with open("rings.json", "r") as read_file:
            rings = json.load(read_file)
        with open("circles.json", "r") as read_file:
            table = json.load(read_file)
        sms = 'Сегодня  у тебя:' + '\n'
        sms += '*' + week[date] + '*' + ':' + '\n'
        i = 0
        for value in lessons[day][koef]:
            i += 1
            if str(value) == "nan (nan)":
                continue
            sms += str(i) + ') ' + str(value) + "  //  " + rings[str(i)] + '\n'
        # if day in table:
        #     sms += 'А ещё репет, дада не забывай:' + '\n'
        #     for key in table:
        #         sms += '*' + key + '*' + ':' + '\n'
        #         sms += table[key][0] + '\n'
        #         sms += table[key][1] + '\n'
        #         sms += '\n'
        #     tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
        #     tb.send_sticker(ID, 'CAADAgADyAADJd8wHm0rHBfrhVxkFgQ')

        tb.send_message(ID, sms, reply_markup=mark_up, parse_mode='Markdown')
        tb.send_sticker(ID, 'CAADAgADlwEAAiXfMB40_zuFZ8yBJhYE')
    else:
        tb.send_message(ID, '*У тебя сегодня выходной, отдыхай. Заслужил братишка!*', reply_markup=mark_up,
                        parse_mode='Markdown')
        tb.send_sticker(ID, 'CAADAgADrgADJd8wHrYWgXrRjs3PFgQ')

import  subprocess
def scd():
    while True:
        now = (datetime.datetime.now())
        date = "%d" % now.hour
        sec = "%d" % now.second
        min = "%d" % now.minute
        if date == "7" and sec == "0" and min == "20":
            morning()
        subprocess.Popen(['python3', 'get_file.py'])
        time.sleep(30)




thread1 = Thread(target=scd)
thread1.start()
tb.polling()
