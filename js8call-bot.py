import configparser
import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import json
import socket
import time
import asyncio
import threading

# Read config file
config = configparser.ConfigParser()
config.sections()
config.read('./config/config.ini')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure Telegram Bot
bot = Bot(token=config['DEFAULT']['TelegramToken'])
dp = Dispatcher(bot)


### JS8Call-Bot ###

async def start_js8call_bot():
    reader, writer = await asyncio.open_connection(config['DEFAULT']['Host'], config['DEFAULT']['Port'])

    while True:
        command = await reader.read(65500)
        if not command:
            break
        # print(command)
        commandD = command.decode()
        if 'RX.DIRECTED' in commandD:
            commandS = commandD.split('\n')
            for i in range(len(commandS)-1):
            # print(x)
                rxd = json.loads(commandS[i])
                params = rxd['params']
                # print(params)
                try:
                    if params['TO'] == config['DEFAULT']['Callsign']:
                        send_to_telegram(str(params['OFFSET']) + " -> " + config['DEFAULT']['Callsign'] + " : " + params['TEXT'])
                        print(f"-> RX_DIRECTED : ", params)
                        if '/HELP' in params['TEXT']:
                            send("TX.SEND_MESSAGE", params['FROM'] + ">COMMANDS: /HELP /WEATHER")
                        elif '/WEATHER' in params['TEXT']:
                            OPENWEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"
                            complete_url = OPENWEATHER_URL + "appid=" + config['DEFAULT']['OpenWeatherToken'] + "&q=" + config['DEAFULT']['WheaterLocation']
                            response = requests.get(complete_url)
                            x = response.json()
                            if x["cod"] != "404":
                                y = x["main"]
                                send("TX.SEND_MESSAGE", params['FROM'] + ">WEATHER IS : TEMP = " + str(y["temp"]) + " , PRESS = " + str(y["pressure"]) + " , HUM = " + str(y["humidity"]))
                    else:
                        print(f"-> RX_DIRECTED : ", params)
                        send_to_telegram(str(params['OFFSET']) + " -> RX_DIR : " + params['TEXT'])
                except KeyError:
                    pass

        elif 'RX.ACTIVITY' in commandD:
            commandS = commandD.split('\n')
            print(len(commandS))
            for i in range(len(commandS)-1):
                print(commandS[i])
                x = json.loads(commandS[i])
                print(f"-> RX_ACTIVITY : ", commandS[i])
                send_to_telegram(str(x['params']['OFFSET']) + " -> RX_ACT : " + x['value'])

        try:
            data = json.loads(commandD)
        except ValueError:
            data = {}
        if not data:
            continue
        if data['value'] == 'on':
            continue
        elif data['value'] == 'off':
            continue

# Convert JS8CALL message
def to_message(typ, value='', params=None):
    if params is None:
        params = {}
    return json.dumps({'type': typ, 'value': value, 'params': params})

# Send message to JS8CALL
def send(*args, **kwargs):
    client_socket = socket.socket()  # instantiate
    client_socket.connect((config['DEFAULT']['Host'], int(config['DEFAULT']['Port'])))
    params = kwargs.get('params', {})
    if '_ID' not in params:
        params['_ID'] = '{}'.format(int(time.time()*1000))
        kwargs['params'] = params
    message = to_message(*args, **kwargs)
    print('outgoing message:', message)
    client_socket.send((message + '\n').encode()) # remember to send the newline at the end :)


### Telegram-Bot ###

# Send message to Telegram Group
def send_to_telegram(message):
    TELEGRAM_URL = f'https://api.telegram.org/bot{config["DEFAULT"]["TelegramToken"]}/sendMessage'
    try:
        response = requests.post(TELEGRAM_URL, json={'chat_id': config['DEFAULT']['ChatId'], 'text': message})
        # print(response.text)
    except Exception as e:
        print(e)

# Bot commando /start and /help
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Bot commands:\n\nReply to callsign : /rc <callsign> <message>\nSend standard CQ : /cq\nSend custom CQ : /ccq <message>\nSend HeartBeat : /hb\n")

# Bot command for reply to callsign in JS8CALL /rc <callsign> <message> 
@dp.message_handler(commands=['rc'])
async def reply_to_js8(message: types.Message):
    text = message['text']
    textS = text.split(' ', 2)
    send("TX.SEND_MESSAGE", textS[1] + ">TLGR ->" + textS[2])
    await message.reply("Message sending..")

#Bot command for send standard CQ in JS8CALL /cq 
@dp.message_handler(commands=['cq'])
async def reply_to_js8(message: types.Message):
    send("TX.SEND_MESSAGE", "@ALLCALL CQ DX " + config['DEFAULT']['Locator']) 
    await message.reply("CQ sending..")

#Bot command for send custom CQ in JS8CALL /ccq <message>
@dp.message_handler(commands=['ccq'])
async def reply_to_js8(message: types.Message):
    text = message['text']
    textS = text.split(' ', 2)
    send("TX.SEND_MESSAGE", "@ALLCALL " + textS[2] + " " + config['DEFAULT']['Locator']) 
    await message.reply("Custom CQ sending..")

#Bot command for send HeartBeat in JS8CALL /cq
@dp.message_handler(commands=['hb'])
async def reply_to_js8(message: types.Message):
    locator = config['DEFAULT']['Locator']
    locatorMod = locator[:6-2]
    send("TX.SEND_MESSAGE", "@HB HEARTBEAT " + locatorMod) 
    await message.reply("HeartBeat sending..")

# Starting JS8Call-Bot en Telegram-Bot
threading.Thread(target=asyncio.run, args=(start_js8call_bot(),),daemon=True).start()
threading.Thread(target=executor.start_polling(dp, skip_updates=True,),daemon=True).start()
