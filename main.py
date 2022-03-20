from turtle import width
import telebot
from performer import *

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    start_asnwer = """
    Hi! If you want to find the localization of an IP address. You are welcome!

Don't be afraid to write /help for more details.
    """
    bot.send_message(message.chat.id, start_asnwer)

@bot.message_handler(commands=['help'])
def start(message):
    start_asnwer = """
    I see you need help.
Commands:
    /ip x.x.x.x - localization of ip address (where x.x.x.x is IP)
    /domain google.com - ip address of domain (for example google.com)

Informaion:
    Bot created by Nikita Smolenskyi

    GitHub: https://github.com/NikitaArd

    """
    bot.send_message(message.chat.id, start_asnwer)


@bot.message_handler(commands=['ip'])
def ip_loc(message):
    ip_adress = recoup(str(message.text), '/ip ')
    try:
        response, htmllink, pnglink = ip_location(ip_adress)
        image = open(pnglink, 'rb')
        doc = open(htmllink, 'rb')
        bot.send_photo(message.chat.id, image, caption=response)
        bot.send_document(message.chat.id, doc, caption='It is full map file. You can download it and open in your browser.')
        doc.close()
        image.close()
        cleaner(htmllink, pnglink)
    except:
        bot.send_message(message.chat.id, 'Ops, It looks like this adress is invalid.')

@bot.message_handler(commands=['domain'])
def hostname(message):
    domain_name = recoup(str(message.text), '/domain ')
    ip_adress = host_ip_recognize(domain_name)
    bot.send_message(message.chat.id, f'The ip adress of {domain_name} is {ip_adress}')

while True:
    bot.polling(none_stop=True)