import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

openai.api_key = "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"
TELEGRAM_TOKEN = "8181071639:AAHHUfI9dwUvVuve7wqd-E2SEJ6GBMlNly8"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    reply = response['choices'][0]['message']['content']
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot is running...")
app.run_polling()