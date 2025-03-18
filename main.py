import logging
import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

# Список URL с мотивационными
MOTIVATIONAL_IMAGES = [
    "https://cs12.pikabu.ru/post_img/2021/02/05/5/161250729511611800.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUNvgfADAZ8PjvlHPUHNVu-wTPDMokJ_j7oQ&s",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQAN4GS6LDQG4D1ApfQNInANk44m41wCYq1Q&s"
]

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Получить мотивашку", callback_data='get_motiv')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message:
        await update.message.reply_text(
            "Привет! Я Генератор мотивашек.\nНажми кнопку ниже, чтобы получить мотивационную картинку.",
            reply_markup=reply_markup
        )

# Обработчик нажатия кнопки
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    # Обязательно отвечаем на callback, чтобы Telegram не думал, что бот завис
    await query.answer()
    if query.data == 'get_motiv':
        image_url = random.choice(MOTIVATIONAL_IMAGES)
        await query.message.reply_photo(photo=image_url)

def main():

    token = '7959923428:AAEmQ5uQKNVJW7ZOeCHIGYgYfK6BGcE33kg'
    application = Application.builder().token(token).build()

    # Регистрируем обработчики команд и кнопок
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))

    # Запускаем бота (run_polling запускает цикл обработки обновлений)
    application.run_polling()

if __name__ == '__main__':
    main()