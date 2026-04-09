import os
import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8753589559:AAHrBEVTHJwpzdmiJhMf5S3Bxx8H57wUUUI"

messages = [
    "Я люблю тебя больше чем бесконечно",
    "Ты самая умная на всей планете",
    "Ты моя сладенькая булочка",
    "Хочу поскорее тебя обнять",
    "Скучаю по тебе",
    "Ты лучшая",
    "Ты самая прекрасная",
    "Ты сегодня сногсшибательна",
    "Ты все можешь",
    "У тебя все получится",
    "Я горжусь тобой",
    "Ты самая красивая девушка на свете",
    "Твоя улыбка делает мой день лучше",
]

image_urls = [
    "https://i.pinimg.com/736x/4a/10/50/4a10507bf058a0df0a8fbd70e9107364.jpg",
    "https://i.pinimg.com/736x/fd/b4/1b/fdb41b9985defa09ae2159ade38f0dc8.jpg",
]

button = ReplyKeyboardMarkup([['ТЫК']], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Нажми на кнопку ТЫК", reply_markup=button)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'ТЫК':
        message = random.choice(messages)
        if random.random() < 0.5:
            image = random.choice(image_urls)
            await update.message.reply_photo(photo=image, caption=message)
        else:
            await update.message.reply_text(message)
    else:
        await update.message.reply_text("Нажми на кнопку ТЫК", reply_markup=button)

def main():
    print("Запуск бота...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Очищаем вебхук перед запуском
    import asyncio
    asyncio.get_event_loop().run_until_complete(app.bot.delete_webhook(drop_pending_updates=True))
    
    print("Бот успешно запущен! Жду сообщений...")
    app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
