import os
import random
import logging
import asyncio
import threading
from aiohttp import web
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TELEGRAM_TOKEN")
if not TOKEN:
    TOKEN = "8753589559:AAHrBEVTHJwpzdmiJhMf5S3Bxx8H57wUUUI"

logging.basicConfig(level=logging.INFO)

messages = [
    "Я люблю тебя больше чем бесконечно",
    "Ты всегда будешь моей зайкой!",
    "А ты у меня любименькая",
    "Ты прям омага бэби",
    "Я бы тебя жеско поцеловал в щечку",
    "Ты моя сладенькая булочка",
    "!!!DANGER!!! КРИТИЧЕСКОЕ ПОВРЕЖДЕНИЕ ЦЕНТРАЛЬНОЙ НЕРВНОЙ СИСТЕМЫ ПРИ ВИДЕ СЛИШКОМ КРАСИВОЙ ЖЕНЩИНЫ !!!DANGER!!!",
    "Мухехехехех ну урвал себе))))",
    "Смотрю на тебя и чувствую напряжение какое то снизу)",
    "Ты слишком хороша сегодня (и вчера и позавчера кстати тоже)",
    "Ты самая умная на всей планете",
    "Никогда не грусти, солнце",
    "Ты моя девятьсот десятая",
    "Хочу поскорее тебя обнять",
    "Ты милашка)",
    "Все наладится",
    "У тебя есть я и моя любоф",
    "Скучаю по тебе",
    "Ты лучшая",
    "Ты самая прекрасная",
    "А ты сегодня секси)))",
    "Может уже зацелуешь меня?",
    "Твои ножкам завидовали все американские звезды))",
    "С тобой не сравится ни одна звезда на всем небосклоне",
    "Ты сегодня сногсшибательна",
    "Ты как всегда самая афигительная)",
    "Я падаю без сознания от твоих фото",
    "Ты моя мордочка)",
    "Forever",
    "Вместе навсегда",
    "Мой самый лучший день, это день когда я встретил тебя",
    "Ты самое лучшее, что со мной случалось",
    "И как тебе удается быть такой невероятно красивой???",
    "Ты сегодня горяча)",
    "Я бы подарил тебе все цветы мира",
    "Поцеловать тебя что ли?)",
    "Твои волосы как отдельный вид кайфа",
    "Твоя попи должна быть вне закона)",
    "Я бы хотел видеть тебя рядом с собой по утрам",
    "А некоторые ночи я никогда не забуду)))",
    "Да вы сегодня как всегда прекрасны!",
    "Кого благодарить за такую девушку как вы?)",
    "ТЫ ПРОСТО ТОП!",
    "Ты все можешь!",
    "Улыбниииись",
    "У тебя все получится",
    "Я горжусь тобой",
    "Ты самая крутая",
    "А ты вкурсе, что я от тебя без ума?",
    "Ты самая красивая девушка на свете",
    "Твоя улыбка делает мой день лучше",
    "Ты невероятно умная и талантливая",
    "Я счастлив, что ты у меня есть",
    "Твои глаза сводят меня с ума",
    "Ты делаешь этот мир ярче",
    "Ты мое вдохновение каждый день",
    "С тобой даже дождливый день становится солнечным",
    "Ты лучшая девушка в моей жизни",
    "Каждый день с тобой - подарок",
    "Твоя доброта безгранична",
    "Ты сильная и смелая, я восхищаюсь тобой",
    "Ты самая нежная и ласковая",
    "Желаю тебе океан счастья и радости",
    "Пусть сегодня у тебя будет отличное настроение",
    "Желаю тебе легкого и продуктивного дня",
    "Пусть все твои мечты сбываются",
    "Желаю тебе здоровья и энергии на все дела",
    "Пусть удача всегда идет с тобой рядом",
    "Желаю тебе море улыбок и приятных сюрпризов"
]

image_urls = [
    "https://i.pinimg.com/736x/4a/10/50/4a10507bf058a0df0a8fbd70e9107364.jpg",
    "https://i.pinimg.com/736x/fd/b4/1b/fdb41b9985defa09ae2159ade38f0dc8.jpg",
    "https://i.pinimg.com/1200x/28/67/ab/2867abf48012a829bbb1d845a3bee86e.jpg",
    "https://i.pinimg.com/1200x/4b/45/96/4b45960814148dc74e6745cf49dafeb8.jpg",
    "https://i.pinimg.com/736x/c3/b5/c4/c3b5c4e47e19502326185dd7d91f92ec.jpg",
    "https://i.pinimg.com/736x/3e/73/be/3e73be3ac1ef6e0da015e9dc85a399d8.jpg",
    "https://i.pinimg.com/736x/d1/8d/4c/d18d4c0dd8246864bd4c41c8374477b4.jpg",
    "https://i.pinimg.com/736x/ee/a2/34/eea234bf184d35eb92a97dd8b9092f21.jpg",
    "https://i.pinimg.com/736x/29/20/66/2920664039230f4123a4488a39aa3612.jpg",
    "https://i.pinimg.com/736x/db/91/fb/db91fb81b78db11fa35b6d3a7ecad888.jpg",
]

button = ReplyKeyboardMarkup([['ТЫК']], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Привет, {user_name}!\n\nНажми на кнопку ТЫК", reply_markup=button)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'ТЫК':
        message = random.choice(messages)
        chance = random.random()
        
        if chance < 0.5 and image_urls:
            try:
                image = random.choice(image_urls)
                await update.message.reply_photo(photo=image, caption=message)
            except Exception as e:
                print(f"Ошибка картинки: {e}")
                await update.message.reply_text(message)
        else:
            await update.message.reply_text(message)
    else:
        await update.message.reply_text('Нажми на кнопку ТЫК', reply_markup=button)

# Веб-сервер для Render (чтобы бот не засыпал)
async def health_check(request):
    return web.Response(text="Bot is running")

async def start_web_server():
    port = int(os.environ.get("PORT", 8000))
    app = web.Application()
    app.router.add_get('/', health_check)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()
    print(f"Веб-сервер запущен на порту {port}")
    await asyncio.Event().wait()

def run_web_server():
    asyncio.run(start_web_server())

# Запуск бота и веб-сервера
if __name__ == "__main__":
    # Запускаем веб-сервер в отдельном потоке
    web_thread = threading.Thread(target=run_web_server, daemon=True)
    web_thread.start()
    
    # Запускаем бота
    print("Запуск бота...")
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот успешно запущен!")
    application.run_polling()
