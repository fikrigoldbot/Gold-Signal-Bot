from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_TOKEN = "7578653757:AAGyM99MMy_ffcP7FRLpvw6cL5zMiscACm8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Gold signals bot is running.")

if _name_ == "_main_":
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running... Press Ctrl+C to stop.")
    app.run_polling()
