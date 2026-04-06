import os
import random
import logging
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
    "https://i.pinimg.com/736x/d0/82/38/d08238f3ec694175cc365ddf162fdc5c.jpg",
    "https://i.pinimg.com/736x/92/88/7e/92887e32c05800795afb34761fa57034.jpg",
    "https://i.pinimg.com/736x/5a/8a/c4/5a8ac4b16551c11814c91ec043cc0cdc.jpg",
    "https://i.pinimg.com/1200x/9e/a4/a6/9ea4a61cf5c5604cdf49748c687840d4.jpg",
    "https://i.pinimg.com/736x/e7/23/af/e723af1bfefea9e20344c0c6339b3450.jpg",
    "https://i.pinimg.com/736x/cf/a5/98/cfa5982705f86d6faaed76cffb6da5cf.jpg",
    "https://i.pinimg.com/736x/75/ae/f5/75aef593e98cf7a4200ca5ff7a4d66e3.jpg",
    "https://i.pinimg.com/736x/09/e3/ff/09e3ffe1b7e15a6bea4490081746a8ed.jpg",
    "https://i.pinimg.com/1200x/94/fc/82/94fc82211a63669d84d692c94aa37af6.jpg",
    "https://i.pinimg.com/736x/5d/f0/13/5df01375342a74bca38d8dc70bd2db18.jpg",
    "https://i.pinimg.com/736x/5b/d8/63/5bd863504d6b517776cd135087a79a23.jpg",
    "https://i.pinimg.com/736x/da/46/33/da46334c6f771d7e8fb2f9e1df27abf7.jpg",
    "https://i.pinimg.com/1200x/ed/c3/a0/edc3a0ed76e7f9c73634188e2a55da69.jpg",
    "https://i.pinimg.com/474x/9b/3b/a3/9b3ba321540c55c62469d6cca74723c6.jpg",
    "https://i.pinimg.com/736x/25/90/14/2590143746ba8733bb9729e792aa0d9f.jpg",
    "https://i.pinimg.com/736x/d3/fd/5f/d3fd5fc2ebe513da3ddd0e0fb1931d51.jpg",
    "https://i.pinimg.com/736x/2e/ae/65/2eae659a7b56bab80dfe0a2a24a58f77.jpg",
    "https://i.pinimg.com/736x/b9/b9/bb/b9b9bbca1b8502c35f00eafc42f0f6bf.jpg",
    "https://i.pinimg.com/736x/9b/0b/7b/9b0b7b66590e603f626214c99caf953d.jpg",
    "https://i.pinimg.com/1200x/2b/87/c2/2b87c27c7cce5c2ec7d7159988c07a65.jpg",
    "https://i.pinimg.com/736x/91/5f/1b/915f1b4b6f22b40f53a5b9f5e9b87361.jpg",
    "https://i.pinimg.com/736x/b9/37/68/b937680251bfe4533d5568a9192782dd.jpg",
    "https://i.pinimg.com/736x/27/9f/78/279f78acd0d780074d9124a0d5acb77f.jpg",
    "https://i.pinimg.com/736x/b4/0f/f7/b40ff7aeb1c88407140cb1d6359fefe9.jpg",
    "https://i.pinimg.com/736x/f7/8a/38/f78a38a772006d1ed39557b28d2e050a.jpg",
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

def main():
    print("Запуск бота...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот успешно запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
