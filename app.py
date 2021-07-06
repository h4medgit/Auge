import telebot
import requests
bot = telebot.TeleBot('1814594340:AAFNobck0TZYUL_dzAmPqEyf5kUsNJFTTj4')

def ipfunc(ip):
    try:
        req = requests.get(f"http://ip-api.com/json/{ip}").json()
        return f"""
        Country: {req['country']}
        City: {req['city']}
        ISP: {req['isp']}
        """
    except KeyError:
        return "this is not a IP"

def countfunc(countryname):
    try:
        req = requests.get(f'https://restcountries.eu/rest/v2/name/{countryname}').json()
        return f"""
         populiation: {req[0]["population"]}
         Capital: {req[0]["capital"]}
         numbericCode: {req[0]["numericCode"]}
         Region: {req[0]["region"]}
         money symbol: {req[0]["currencies"][0]['name']}
        """
    except KeyError:
        return "this is not a country"

#start methods ===========================
@bot.message_handler(commands=['start'])
def hello(message):
    bot.reply_to(message, "hello. using /country for information about country or using /ip for information about IP")


#ip methods ==============================
@bot.message_handler(commands=['ip'])
def ipcommand(message):
    bot.reply_to(message, 'ok send me your IP')
    bot.register_next_step_handler(message, ipinfo)
def ipinfo(message):
    bot.reply_to(message, ipfunc(message.text))


#country methods ==========================
@bot.message_handler(commands=['country'])
def countryfunc(message):
        bot.reply_to(message, 'ok send me a country name and the end of your work please enter /start to working with IP information')
        bot.register_next_step_handler(message, countryfunc)
def countryfunc(message):
        bot.reply_to(message, countfunc(message.text))



bot.polling(none_stop=True)
