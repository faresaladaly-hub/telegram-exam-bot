import os
import telebot
import requests

TOKEN = os.getenv("BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg,"👋 أهلاً بك في بوت المذاكرة\nاكتب سؤالك.")

@bot.message_handler(func=lambda m: True)
def chat(msg):
    try:

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_KEY}"

        data = {
            "contents":[
                {
                    "parts":[
                        {"text": msg.text}
                    ]
                }
            ]
        }

        response = requests.post(url,json=data)
        result = response.json()

        answer = result["candidates"][0]["content"]["parts"][0]["text"]

        bot.reply_to(msg,answer)

    except Exception as e:
        print(e)
        bot.reply_to(msg,"حدث خطأ حاول مرة أخرى")

bot.infinity_polling(skip_pending=True)
