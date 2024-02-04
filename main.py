import telebot
import time
import schedule
import csv
import pytz
from datetime import datetime
from pogoda_parse import get_pogoda_zavtra
from parse_currency import parse_cur
from background import keep_alive

TOKEN = "6672245147:AAHiRaF4avoR0zvZB_Y0YYQn51sKBJTRx_k"
time_format = '%Y-%m-%d %H:%M:%S'
csv_fn = 'log.csv'
msk_tz = pytz.timezone('Europe/Moscow')

bot = telebot.TeleBot(TOKEN)
chat_id_AZ = 162345276
chat_id_Vesely = -1001828849304
chat_id = chat_id_AZ
pogoda_time = "21:30:00"


def send_message():
    last_time = chten_log()
    if last_time.day != datetime.now(tz=msk_tz).day:
        msg = get_pogoda_zavtra()
        # msg += f'\nПоследняя запись в логе: {last_time}'
        msg += f'\nКурсы валют: {parse_cur()}'
        cur_time_str = datetime.now(tz=msk_tz).strftime(time_format)
        zapis_log(cur_time_str)
        bot.send_message(chat_id_AZ, msg, parse_mode='html')


def zapis_log(tm):
    with open(csv_fn, 'a',  newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        zapis = [tm]
        writer.writerow(zapis)


def chten_log():
    with open(csv_fn, 'r',  newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for f in reader:
            res = datetime.strptime(f[0], time_format)
        return res


# schedule.every(15).seconds.do(send_message)

keep_alive()

schedule.every().day.at(pogoda_time, tz=msk_tz).do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)