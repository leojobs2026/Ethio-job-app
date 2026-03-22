import telebot
import json
from telebot.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '8530857364:AAGKtW7Etj45QY7CNXoV3LxIv_SEWD_oNqE'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = InlineKeyboardMarkup()
    # ያንተ የ GitHub Pages ሊንክ
    link = "https://leojobs2026.github.io/Ethio-job-app/"
    markup.add(InlineKeyboardButton("🚀 Open Ethio-Job App", web_app=WebAppInfo(url=link)))
    bot.send_message(message.chat.id, "እንኳን በደህና መጡ! አፑን ለመክፈት ከታች ያለውን ይጫኑ።", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def handle_data(message):
    # አፑ መረጃ ሲልክ እዚህ ጋር ይቀበላል
    bot.send_message(message.chat.id, "🔐 የእርስዎ መግቢያ ኮድ፡ 1234")

bot.polling()
