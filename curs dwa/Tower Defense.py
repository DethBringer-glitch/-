import telebot
from telebot import types
import Tower_Defense_2
game = Tower_Defense_2.Game()


bot = telebot.TeleBot("7200079765:AAHVuz4tXoNQdK4NwlepkD39NTI9KnnpnSo")

stage = ['❏', '❏', '❏', '❏']

pole = f'―――                    ―――  ◘ \n     {stage[0]}    │     {stage[1]}     │  \n             │              │  \n     {stage[2]}    │     {stage[3]}     │  \n                 ―――  '

stag1 = '―――                    ―――  ◘ \n     §      │     ❏     │  \n             │              │  \n     ❏    │     ❏     │  \n                 ―――  '

stag2 = '―――                    ―――  ◘ \n     ❏    │     §      │  \n             │              │  \n     ❏    │     ❏     │  \n                 ―――  '

stag3 = '―――                    ―――  ◘ \n     ❏    │     ❏     │  \n             │              │  \n     §      │     ❏     │  \n                 ―――  '

stag4 = '―――                    ―――  ◘ \n     ❏    │     ❏     │  \n             │              │  \n     ❏    │     §      │  \n                 ―――  '

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет, напиши /help для получения списка всех комманд')
@bot.message_handler(commands=['run'])
def run(message):
    global pole, stage
    stage = ['❏', '❏', '❏', '❏']

    pole = f'―――                    ―――  ◘ \n     {stage[0]}    │     {stage[1]}     │  \n             │              │  \n     {stage[2]}    │     {stage[3]}     │  \n                 ―――  '
    bot.send_message(message.chat.id, 'Хорошо сейчас начну игру.')
    bot.send_message(message.chat.id, pole)
    game.fight()
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '/run - начать игру. \n'
                                      '/guards - ставит стража на выбранную позицию. \n'
                                      '/wall - пополняет hp ворот. \n'
                                      '/next_wave - следующая волна противников.')
@bot.message_handler(commands=['guards'])
def guards(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('Поставить стража на 1 позицию')
    btn2 = types.KeyboardButton('Поставить стража на 2 позицию')
    btn3 = types.KeyboardButton('Поставить стража на 3 позицию')
    btn4 = types.KeyboardButton('Поставить стража на 4 позицию')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,'Выбери позицию для стража.', reply_markup=markup)
@bot.message_handler(commands=['wall'])
def wall(message):
    bot.send_message(message.chat.id, 'Ремонтирую ворота.')
@bot.message_handler(commands=['next_wave'])
def next_wave(message):
    bot.send_message(message.chat.id,
    'Следующая волна противников надвигается. Приготовьтесь!')

@bot.message_handler(content_types=['text'])
def text(message):
    global pole
    if message.text == 'Поставить стража на 1 позицию':
        stage[0] = '§'
        pole = f'―――                    ―――  ◘ \n     {stage[0]}    │     {stage[1]}     │  \n             │              │  \n     {stage[2]}    │     {stage[3]}     │  \n                 ―――  '
        bot.send_message(message.chat.id, pole)
        game.guards_add(1)
    if message.text == 'Поставить стража на 2 позицию':
        stage[1] = '§'
        pole = f'―――                    ―――  ◘ \n     {stage[0]}    │     {stage[1]}     │  \n             │              │  \n     {stage[2]}    │     {stage[3]}     │  \n                 ―――  '
        bot.send_message(message.chat.id, pole)
    if message.text == 'Поставить стража на 3 позицию':
        stage[2] = '§'
        pole = f'―――                    ―――  ◘ \n     {stage[0]}    │     {stage[1]}     │  \n             │              │  \n     {stage[2]}    │     {stage[3]}     │  \n                 ―――  '
        bot.send_message(message.chat.id, pole)
    if message.text == 'Поставить стража на 4 позицию':
        stage[3] = '§'
        pole = f'―――                    ―――  ◘ \n     {stage[0]}    │     {stage[1]}     │  \n             │              │  \n     {stage[2]}    │     {stage[3]}     │  \n                 ―――  '
        bot.send_message(message.chat.id, pole)


bot.polling(True)