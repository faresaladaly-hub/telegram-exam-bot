import os
import telebot
import openai



TOKEN = os.getenv("BOT_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg,"👋 أهلاً بك في بوت المذاكرة\nاكتب سؤالك أو أرسل موضوع تريد شرحه")

@bot.message_handler(func=lambda m: True)
def chat(msg):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":"أنت مساعد دراسي يساعد الطلاب في شرح الدروس وحل الأسئلة."},
                {"role":"user","content": msg.text}
            ]
        )

        answer = response.choices[0].message.content
        bot.reply_to(msg, answer)

    except Exception as e:
        bot.reply_to(msg, "حدث خطأ حاول مرة أخرى")

bot.infinity_polling()
