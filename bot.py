import os
import telebot
from openai import OpenAI

TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg,"اهلا 👋 اكتب سؤالك")

@bot.message_handler(func=lambda m: True)
def chat(msg):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":msg.text}]
    )

    bot.reply_to(msg,response.choices[0].message.content)

bot.infinity_polling()
