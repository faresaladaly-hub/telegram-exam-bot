import os
import telebot
import openai

# قراءة المفاتيح من Railway
TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

# إعداد البوت
bot = telebot.TeleBot(TOKEN)

# إعداد OpenAI
openai.api_key = OPENAI_KEY


# رسالة البداية
@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(
        msg,
        "👋 أهلاً بك في بوت المذاكرة\n"
        "اكتب سؤالك أو أرسل موضوع تريد شرحه."
    )


# الرد على أي رسالة
@bot.message_handler(func=lambda m: True)
def chat(msg):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "أنت مساعد دراسي يساعد الطلاب في شرح الدروس بطريقة بسيطة."
                },
                {
                    "role": "user",
                    "content": msg.text
                }
            ]
        )

        answer = response["choices"][0]["message"]["content"]

        bot.reply_to(msg, answer)

    except Exception as e:
        bot.reply_to(msg, "حدث خطأ حاول مرة أخرى")


# تشغيل البوت
bot.infinity_polling()
