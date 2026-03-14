import telebot
from openai import OpenAI

TOKEN = "PUT_TELEGRAM_TOKEN"
OPENAI_KEY = "PUT_OPENAI_KEY"

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg,"أرسل كتاب أو سلايدات واسألني منها")

@bot.message_handler(func=lambda m: True)
def chat(msg):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":msg.text}]
    )
    bot.reply_to(msg,response.choices[0].message.content)

bot.infinity_polling()
