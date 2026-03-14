import os
import telebot
import requests

TOKEN = os.getenv("BOT_TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "👋 أهلاً بك في بوت المذاكرة\nاكتب سؤالك.")

@bot.message_handler(func=lambda m: True)
def chat(msg):
    try:
        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

        headers = {
            "Content-Type": "application/json"
        }

        params = {
            "key": GEMINI_KEY
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": msg.text}
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, params=params, json=data)
        result = response.json()

        if "candidates" in result:
            answer = result["candidates"][0]["content"]["parts"][0]["text"]
        else:
            print(result)
            answer = "حدث خطأ من Gemini"

        bot.reply_to(msg, answer)

    except Exception as e:
        print(e)
        bot.reply_to(msg, "حدث خطأ حاول مرة أخرى")

bot.infinity_polling(skip_pending=True)
